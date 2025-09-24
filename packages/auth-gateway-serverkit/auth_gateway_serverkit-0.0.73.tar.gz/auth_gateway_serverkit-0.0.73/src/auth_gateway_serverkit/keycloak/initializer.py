"""Keycloak server initialization module for the auth gateway serverkit."""
import os
import json
import asyncio
import aiohttp
from ..logger import init_logger
from .config import settings
from .client_api import (
    get_admin_token, get_client_uuid, create_realm, set_frontend_url, create_client, create_realm_roles,
    add_audience_protocol_mapper, enable_edit_username, remove_default_scopes, create_resource,
    create_policy, create_permission, get_resource_id
)
from .cleanup_api import cleanup_authorization_config
from .utils import create_dynamic_permission_name


logger = init_logger("serverkit.keycloak.initializer")


async def check_keycloak_connection():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(settings.SERVER_URL) as response:
                if response.status == 200:
                    logger.info("Successfully connected to Keycloak server")
                    return True
                else:
                    logger.error(f"Failed to connect to Keycloak server. Status: {response.status}")
                    return False
    except aiohttp.ClientError as e:
        logger.error(f"Failed to connect to Keycloak server: {e}")
        return False


async def process_json_config(admin_token, client_uuid, cleanup_and_build=True):
    """
    Process authorization configuration from multiple files:
    - roles.json: Contains realm_roles and policies (global/shared)
    - services/*.json: Contains resources and permissions (service-specific)

    This function ensures proper Keycloak permissions configuration by creating only one
    permission per resource with all relevant policies combined to avoid implicit AND logic.

    :param admin_token: Admin token for authentication
    :param client_uuid: Client UUID
    :param cleanup_and_build: Whether to delete existing configuration before creating new one
    :return: True if successful, False otherwise
    """
    authorization_dir = os.path.join(os.getcwd(), "authorization")
    services_dir = os.path.join(authorization_dir, "services")

    # Check if authorization directory exists
    if not os.path.exists(authorization_dir):
        logger.error("Authorization directory not found")
        return False

    # Load global configuration (roles and policies)
    roles_file = os.path.join(authorization_dir, "roles.json")
    if not os.path.exists(roles_file):
        logger.error("roles.json file not found")
        return False

    with open(roles_file, 'r') as file:
        global_config = json.load(file)

    # Load service-specific configurations (resources and permissions)
    service_configs = []
    if os.path.exists(services_dir):
        for filename in os.listdir(services_dir):
            if filename.endswith('.json'):
                service_file = os.path.join(services_dir, filename)
                with open(service_file, 'r') as file:
                    service_config = json.load(file)
                    service_configs.append({
                        'name': filename[:-5],  # Remove .json extension
                        'config': service_config
                    })
                logger.info(f"Loaded service configuration: {filename}")

    # Combine configurations
    combined_config = {
        "realm_roles": global_config.get("realm_roles", []),
        "policies": global_config.get("policies", []),
        "resources": [],
        "permissions": []
    }

    # Collect resources from all service files
    for service in service_configs:
        service_resources = service['config'].get("resources", [])
        combined_config["resources"].extend(service_resources)
        logger.info(f"Added {len(service_resources)} resources from {service['name']} service")

    # CRITICAL FIX: Handle overlapping resources by merging their policies
    # First collect all resources and their associated policies
    resource_policies_map = {}

    for service in service_configs:
        service_permissions = service['config'].get("permissions", [])

        for permission in service_permissions:
            perm_policies = permission.get('policies', [])
            perm_resources = permission.get('resources', [])

            # For each resource, collect ALL policies that should apply to it
            for resource_name in perm_resources:
                if resource_name not in resource_policies_map:
                    resource_policies_map[resource_name] = set()

                resource_policies_map[resource_name].update(perm_policies)

    # Now group resources by their FINAL combined policy set
    policy_to_resources_map = {}

    for resource_name, policies in resource_policies_map.items():
        policies_key = tuple(sorted(policies))  # Create unique key for this policy combination

        if policies_key not in policy_to_resources_map:
            policy_to_resources_map[policies_key] = {
                'policies': list(policies),
                'resources': []
            }

        policy_to_resources_map[policies_key]['resources'].append(resource_name)

    # Create permissions by FINAL POLICY COMBINATION
    consolidated_permissions = []
    for i, (policies_key, policy_info) in enumerate(policy_to_resources_map.items(), 1):
        policies = policy_info['policies']
        resources = policy_info['resources']

        # Create dynamic permission name that works with any policy names
        permission_name = create_dynamic_permission_name(policies)

        consolidated_permission = {
            'name': permission_name,
            'description': f"Access permission for {', '.join(policies)}",
            'policies': policies,
            'resources': resources
        }

        consolidated_permissions.append(consolidated_permission)

    # Update combined config with consolidated permissions
    combined_config["permissions"] = consolidated_permissions

    logger.info(f"Combined configuration: {len(combined_config['realm_roles'])} roles, {len(combined_config['policies'])} policies, {len(combined_config['resources'])} resources, {len(consolidated_permissions)} consolidated permissions")

    # Step 1: Cleanup existing configuration if requested
    if cleanup_and_build:
        logger.info("Starting cleanup of existing authorization configuration...")
        cleanup_success = await cleanup_authorization_config(combined_config, admin_token, client_uuid)
        if not cleanup_success:
            logger.error("Failed to cleanup existing configuration")
            return False

        # Step 2: Create resources and collect their IDs
        resource_ids = {}
        resources_to_create = combined_config.get("resources", [])
        if resources_to_create:
            logger.info(f"Creating {len(resources_to_create)} resources...")
            for resource in resources_to_create:
                success = await create_resource(
                    resource['name'],
                    resource['displayName'],
                    resource['url'],
                    admin_token,
                    client_uuid
                )
                if not success:
                    logger.error(f"Failed to create resource: {resource['name']}")
                    return False

                # Retrieve resource ID from Keycloak
                resource_id = await get_resource_id(resource['name'], admin_token, client_uuid)
                if resource_id:
                    resource_ids[resource['name']] = resource_id
                else:
                    logger.error(f"Failed to retrieve resource ID for: {resource['name']}")
                    return False
            logger.info("All resources created successfully")

        # Step 3: Create policies
        policies_to_create = combined_config.get("policies", [])
        if policies_to_create:
            logger.info(f"Creating {len(policies_to_create)} policies...")
            for policy in policies_to_create:
                success = await create_policy(
                    policy['name'],
                    policy['description'],
                    policy['roles'],
                    admin_token,
                    client_uuid
                )
                if not success:
                    logger.error(f"Failed to create policy: {policy['name']}")
                    return False
            logger.info("All policies created successfully")

        # Step 4: Create consolidated permissions (one per resource with combined policies)
        permissions_to_create = combined_config.get("permissions", [])
        if permissions_to_create:
            logger.info(f"Creating {len(permissions_to_create)} consolidated permissions...")
            for permission in permissions_to_create:
                resource_names = permission.get('resources', [])
                if not resource_names:
                    logger.error(f"No resources specified for permission '{permission['name']}'")
                    return False

                # Get resource IDs for all associated resources (should be only one per permission now)
                resource_ids_list = [resource_ids.get(name) for name in resource_names]
                if None in resource_ids_list:
                    missing_resources = [name for name, rid in zip(resource_names, resource_ids_list) if rid is None]
                    logger.error(f"Missing resource IDs for: {missing_resources}")
                    return False

                success = await create_permission(
                    permission['name'],
                    permission['description'],
                    permission['policies'],  # Combined policies for OR-based logic
                    resource_ids_list,
                    admin_token,
                    client_uuid
                )
                if not success:
                    logger.error(f"Failed to create permission: {permission['name']}")
                    return False
            logger.info("All consolidated permissions created successfully")

    logger.info("Authorization configuration processed successfully with proper OR-based permission logic")
    return True


async def initialize_keycloak_server(max_retries=30, retry_delay=5, cleanup_and_build=True):
    """
    Initialize Keycloak server with realm, client, and authorization configuration.

    :param max_retries: Maximum number of connection retry attempts
    :param retry_delay: Delay between retry attempts in seconds
    :param cleanup_and_build: Whether to delete existing authorization config before creating new one
    :return: True if successful, False otherwise
    """
    # 1) wait until Keycloak is up
    for attempt in range(1, max_retries + 1):
        if await check_keycloak_connection():
            break
        logger.warning(f"Attempt {attempt}/{max_retries} failed. Retrying in {retry_delay}s")
        await asyncio.sleep(retry_delay)
    else:
        logger.error("Failed to initialize Keycloak after multiple attempts")
        return False

    # 2) get admin token
    admin_token = await get_admin_token()
    if not admin_token:
        logger.error("Failed to get admin token")
        return False

    # 3) run all the "realm & client setup" steps in order
    steps = [
        (create_realm, (),                   "create realm"),
        (set_frontend_url, (),               "set Frontend URL"),
        (create_client, (),                  "create client"),
        (create_realm_roles, (),             "create realm roles"),
        (add_audience_protocol_mapper, (),   "add Audience Protocol Mapper"),
        (enable_edit_username, (),           "enable edit username"),
    ]
    for func, args, desc in steps:
        ok = await func(admin_token, *args)
        if not ok:
            logger.error(f"Failed to {desc}")
            return False

    # 4) fetch the client UUID
    client_uuid = await get_client_uuid(admin_token)
    if not client_uuid:
        logger.error("Failed to get client UUID")
        return False

    # 5) remove scopes and process JSON config
    post_steps = [
        (remove_default_scopes,    (client_uuid,), "remove unwanted default/optional scopes"),
        (process_json_config,      (client_uuid, cleanup_and_build), "process JSON configuration"),
    ]
    for func, args, desc in post_steps:
        ok = await func(admin_token, *args)
        if not ok:
            logger.error(f"Failed to {desc}")
            return False

    logger.info("Keycloak initialization completed successfully")
    return True
