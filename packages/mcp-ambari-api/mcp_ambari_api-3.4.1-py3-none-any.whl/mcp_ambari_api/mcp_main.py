"""
MCP tool definitions for Ambari REST API operations.

- Ambari API Documents: https://github.com/apache/ambari/blob/trunk/ambari-server/docs/api/v1/index.md
"""
from typing import Dict, Optional, List, Any, Set
import argparse
from fastmcp import FastMCP
from fastmcp.server.auth import StaticTokenVerifier
import os
import importlib.resources as pkg_resources
import asyncio  # Add this import at the top of the file to use asyncio.sleep
import logging
import json
from mcp_ambari_api.functions import (
    format_timestamp,
    format_single_host_details,
    make_ambari_request,
    make_ambari_metrics_request,
    AMBARI_CLUSTER_NAME,
    AMBARI_METRICS_BASE_URL,
    log_tool,
    format_alerts_output,
    get_current_time_context,
    safe_timestamp_compare,
    resolve_metrics_time_range,
    metrics_map_to_series,
    summarize_metric_series,
    fetch_latest_metric_value,
    get_component_hostnames,
    ensure_metric_catalog,
    canonicalize_app_id,
    get_metrics_for_app,
)
# from .functions import (
#     format_timestamp, 
#     format_single_host_details, 
#     make_ambari_request,
#     AMBARI_CLUSTER_NAME,
#     log_tool,
#     format_alerts_output,
#     get_current_time_context,
#     safe_timestamp_compare
# )

# Set up logging (initial level from env; may be overridden by --log-level)
logging.basicConfig(
    level=os.environ.get("MCP_LOG_LEVEL", "INFO"),
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger("AmbariService")

# =============================================================================
# Authentication Setup
# =============================================================================

# Check environment variables for authentication early
_auth_enable = os.environ.get("REMOTE_AUTH_ENABLE", "false").lower() == "true"
_secret_key = os.environ.get("REMOTE_SECRET_KEY", "")

# Initialize the main MCP instance with authentication if configured
if _auth_enable and _secret_key:
    logger.info("Initializing MCP instance with Bearer token authentication (from environment)")
    
    # Create token configuration
    tokens = {
        _secret_key: {
            "client_id": "ambari-api-client",
            "user": "admin",
            "scopes": ["read", "write"],
            "description": "Ambari API access token"
        }
    }
    
    auth = StaticTokenVerifier(tokens=tokens)
    mcp = FastMCP("ambari-api", auth=auth)
    logger.info("MCP instance initialized with authentication")
else:
    logger.info("Initializing MCP instance without authentication")
    mcp = FastMCP("ambari-api")

# =============================================================================
# Constants
# =============================================================================

HOST_FILTER_REQUIRED_COMPONENTS = {
    "datanode": "DATANODE",
    "nodemanager": "NODEMANAGER",
}

# =============================================================================
# Helper Functions
# =============================================================================

async def check_service_active_requests(cluster_name: str, service_name: str) -> List[Dict]:
    """
    Check if there are any active requests for a specific service.
    
    Args:
        cluster_name: Name of the cluster
        service_name: Name of the service to check
        
    Returns:
        List of active request information dictionaries for the service
    """
    try:
        endpoint = f"/clusters/{cluster_name}/requests?fields=Requests/id,Requests/request_status,Requests/request_context,Requests/start_time,Requests/progress_percent"
        response_data = await make_ambari_request(endpoint)
        
        if response_data is None or response_data.get("error"):
            return []
            
        all_requests = response_data.get("items", [])
        service_requests = []
        
        for request in all_requests:
            request_info = request.get("Requests", {})
            status = request_info.get("request_status", "")
            context = request_info.get("request_context", "")
            
            # Check if this is an active request for our service
            if (status in ["IN_PROGRESS", "PENDING", "QUEUED", "STARTED"] and 
                service_name.upper() in context.upper()):
                service_requests.append({
                    "id": request_info.get("id"),
                    "status": status,
                    "context": context,
                    "progress": request_info.get("progress_percent", 0)
                })
                
        return service_requests
    except Exception:
        return []

# =============================================================================
# MCP Tools
# =============================================================================


@mcp.tool(title="Dump Configurations")
@log_tool
async def dump_configurations(
    config_type: Optional[str] = None,
    service_filter: Optional[str] = None,
    filter: Optional[str] = None,
    summarize: bool = False,
    include_values: bool = True,
    limit: int = 0,
    max_chars: int = 30000,
) -> str:
    """Unified configuration introspection tool (supersedes get_configurations & list_configurations & dump_all_configurations).

    Modes:
      1) Single type values: specify config_type=<type>
      2) Bulk list (optionally narrowed by service_filter substring in type name)
      3) Filtering keys/types via filter substring

    Args:
        config_type: focus on one type's latest tag (other bulk params ignored except filter on keys)
        service_filter: substring to restrict bulk types (ignored if config_type provided)
        filter: substring applied to type names OR property keys
        summarize: bulk mode summary lines only (counts + sample keys, forces include_values False)
        include_values: include key=value pairs (bulk/full mode only)
        limit: max number of types to output in bulk mode (0 = unlimited)
        max_chars: truncate final output if exceeds
    """
    cluster_name = AMBARI_CLUSTER_NAME
    f_lc = filter.lower() if filter else None
    try:
        # Acquire desired configs mapping
        cluster_resp = await make_ambari_request(f"/clusters/{cluster_name}?fields=Clusters/desired_configs")
        desired_configs = cluster_resp.get("Clusters", {}).get("desired_configs", {}) if cluster_resp else {}
        if not desired_configs:
            return "No desired_configs found in cluster."\
 if config_type else "No configuration data found."  # single or bulk

        # SINGLE TYPE MODE
        if config_type:
            if config_type not in desired_configs:
                # fuzzy suggestions
                suggestions = [t for t in desired_configs.keys() if config_type.lower() in t.lower()][:8]
                return f"Config type '{config_type}' not found. Suggestions: {suggestions}" if suggestions else f"Config type '{config_type}' not found."
            tag = desired_configs[config_type].get("tag")
            if not tag:
                return f"Config type '{config_type}' has no tag info."
            cfg_resp = await make_ambari_request(f"/clusters/{cluster_name}/configurations?type={config_type}&tag={tag}")
            items = cfg_resp.get("items", []) if cfg_resp else []
            if not items:
                return f"No items for config type '{config_type}' (tag={tag})."
            props = items[0].get("properties", {}) or {}
            prop_attrs = items[0].get("properties_attributes", {}) or {}

            # key filtering
            if f_lc:
                props = {k: v for k, v in props.items() if f_lc in k.lower() or f_lc in config_type.lower()}
            lines = [f"CONFIG TYPE: {config_type}", f"Tag: {tag}", f"Keys: {len(props)}"]
            lines.append("Properties:")
            for k in sorted(props.keys()):
                v = props[k]
                v_disp = v.replace('\n', '\\n') if isinstance(v, str) else repr(v)
                lines.append(f"  {k} = {v_disp}")
            if prop_attrs:
                lines.append("\nAttributes:")
                for a_name, a_map in prop_attrs.items():
                    lines.append(f"  [{a_name}]")
                    for k, v in a_map.items():
                        if f_lc and f_lc not in k.lower():
                            continue
                        lines.append(f"    {k}: {v}")
            result = "\n".join(lines)
            if len(result) > max_chars:
                return result[:max_chars] + f"\n... [TRUNCATED {len(result)-max_chars} chars]"
            return result

        # BULK MODE
        type_names = sorted(desired_configs.keys())
        if service_filter:
            sf_lc = service_filter.lower()
            type_names = [t for t in type_names if sf_lc in t.lower()]
        emitted = 0
        blocks: List[str] = []
        for cfg_type in type_names:
            tag = desired_configs[cfg_type].get("tag")
            if not tag:
                continue
            cfg_resp = await make_ambari_request(f"/clusters/{cluster_name}/configurations?type={cfg_type}&tag={tag}")
            items = cfg_resp.get("items", []) if cfg_resp else []
            if not items:
                continue
            props = items[0].get("properties", {}) or {}

            # Skip if filter specified and neither type nor any key matches
            if f_lc and f_lc not in cfg_type.lower() and not any(f_lc in k.lower() for k in props.keys()):
                continue

            if summarize:
                sample = list(props.keys())[:5]
                blocks.append(f"[{cfg_type}] tag={tag} keys={len(props)} sample={sample}")
            else:
                if not include_values:
                    keys = [k for k in sorted(props.keys()) if (not f_lc or f_lc in k.lower() or f_lc in cfg_type.lower())]
                    blocks.append(f"[{cfg_type}] tag={tag} key_count={len(props)} keys={keys[:50]}")
                else:
                    lines = [f"[{cfg_type}] tag={tag} keys={len(props)}"]
                    for k in sorted(props.keys()):
                        if f_lc and f_lc not in k.lower() and f_lc not in cfg_type.lower():
                            continue
                        v = props[k]
                        v_disp = v.replace('\n', '\\n') if isinstance(v, str) else repr(v)
                        lines.append(f"  {k} = {v_disp}")
                    blocks.append("\n".join(lines))

            emitted += 1
            if limit and emitted >= limit:
                break

        if not blocks:
            return "No configuration data matched filter." if (filter or service_filter) else "No configuration data collected."

        header = [
            "AMBARI CONFIGURATION DUMP",
            f"cluster={cluster_name}",
            f"total_types_considered={len(desired_configs)}",
            f"types_output={emitted}",
            f"mode={'summarize' if summarize else ('full-values' if include_values else 'keys-only')}",
        ]
        if service_filter:
            header.append(f"service_filter='{service_filter}'")
        if filter:
            header.append(f"filter='{filter}'")
        result = "\n".join(header) + "\n\n" + "\n\n".join(blocks)
        if len(result) > max_chars:
            return result[:max_chars] + f"\n... [TRUNCATED {len(result)-max_chars} chars]"
        return result
    except Exception as e:
        return f"[ERROR] dump_configurations failed: {e}"

@mcp.tool()
@log_tool
async def get_cluster_info() -> str:
    """
    Retrieves basic information for an Ambari cluster.

    [Tool Role]: Dedicated tool for real-time retrieval of overall status and basic information for an Ambari cluster.

    [Core Functions]:
    - Retrieve cluster name, version, provisioning state, and security type
    - Provide formatted output for LLM automation and cluster monitoring

    [Required Usage Scenarios]:
    - When users request cluster info, status, or summary
    - When monitoring cluster health or auditing cluster properties
    - When users mention cluster overview, Ambari cluster, or cluster details

    Returns:
        Cluster basic information (success: formatted info, failure: English error message)
    """
    cluster_name = AMBARI_CLUSTER_NAME
    try:
        endpoint = f"/clusters/{cluster_name}"
        response_data = await make_ambari_request(endpoint)
        
        if "error" in response_data:
            return f"Error: Unable to retrieve information for cluster '{cluster_name}'. {response_data['error']}"
        
        cluster_info = response_data.get("Clusters", {})
        
        result_lines = [f"Information for cluster '{cluster_name}':"]
        result_lines.append("=" * 30)
        result_lines.append(f"Cluster Name: {cluster_info.get('cluster_name', cluster_name)}")
        result_lines.append(f"Version: {cluster_info.get('version', 'Unknown')}")
        
        if "provisioning_state" in cluster_info:
            result_lines.append(f"Provisioning State: {cluster_info['provisioning_state']}")
        
        if "security_type" in cluster_info:
            result_lines.append(f"Security Type: {cluster_info['security_type']}")
        
        return "\n".join(result_lines)
        
    except Exception as e:
        return f"Error: Exception occurred while retrieving cluster information - {str(e)}"

@mcp.tool()
@log_tool
async def get_active_requests() -> str:
    """
    Retrieves currently active (in progress) requests/operations in an Ambari cluster.
    Shows running operations, in-progress tasks, pending requests.
    
    [Tool Role]: Dedicated tool for monitoring currently running Ambari operations
    
    [Core Functions]:
    - Retrieve active/running Ambari operations (IN_PROGRESS, PENDING status)
    - Show real-time progress of ongoing operations
    - Monitor current cluster activity
    
    [Required Usage Scenarios]:
    - When users ask for "active requests", "running operations", "current requests"
    - When users ask for "request list", "operation list", "task list"
    - When users want to see "current tasks", "running tasks", "in progress operations"
    - When users mention "running", "in progress", "current activity"
    - When users ask about Ambari requests, operations, or tasks
    - When checking if any operations are currently running
    
    Returns:
        Active requests information (success: active request list, failure: error message)
    """
    cluster_name = AMBARI_CLUSTER_NAME
    try:
        # Get requests that are in progress only (remove PENDING as it may not be supported)
        endpoint = f"/clusters/{cluster_name}/requests?fields=Requests/id,Requests/request_status,Requests/request_context,Requests/start_time,Requests/progress_percent&Requests/request_status=IN_PROGRESS"
        response_data = await make_ambari_request(endpoint)
        
        if "error" in response_data:
            # If IN_PROGRESS also fails, try without status filter and filter manually
            endpoint_fallback = f"/clusters/{cluster_name}/requests?fields=Requests/id,Requests/request_status,Requests/request_context,Requests/start_time,Requests/progress_percent&sortBy=Requests/id.desc"
            response_data = await make_ambari_request(endpoint_fallback)
            
            if "error" in response_data:
                return f"Error: Unable to retrieve active requests for cluster '{cluster_name}'. {response_data['error']}"
        
        if "items" not in response_data:
            return f"No active requests found in cluster '{cluster_name}'."
        
        # Filter for active requests manually if needed
        all_requests = response_data["items"]
        active_requests = []
        
        for request in all_requests:
            request_info = request.get("Requests", {})
            status = request_info.get("request_status", "")
            if status in ["IN_PROGRESS", "PENDING", "QUEUED", "STARTED"]:
                active_requests.append(request)
        
        if not active_requests:
            return f"No active requests - All operations completed in cluster '{cluster_name}'."
        
        result_lines = [f"Active Requests for Cluster '{cluster_name}' ({len(active_requests)} running):"]
        result_lines.append("=" * 60)
        
        for i, request in enumerate(active_requests, 1):
            request_info = request.get("Requests", {})
            request_id = request_info.get("id", "Unknown")
            status = request_info.get("request_status", "Unknown")
            context = request_info.get("request_context", "No context")
            progress = request_info.get("progress_percent", 0)
            start_time = request_info.get("start_time", "Unknown")
            
            result_lines.append(f"{i}. Request ID: {request_id}")
            result_lines.append(f"   Status: {status}")
            result_lines.append(f"   Progress: {progress}%")
            result_lines.append(f"   Context: {context}")
            result_lines.append(f"   Started: {start_time}")
            result_lines.append("")
        
        result_lines.append("Tip: Use get_request_status(request_id) for detailed progress information.")
        
        return "\n".join(result_lines)
        
    except Exception as e:
        return f"Error: Exception occurred while retrieving active requests - {str(e)}"

@mcp.tool()
@log_tool
async def get_cluster_services() -> str:
    """
    Retrieves the list of services with status in an Ambari cluster.
    
    [Tool Role]: Dedicated tool for real-time retrieval of all running services and basic status information in an Ambari cluster
    
    [Core Functions]: 
    - Retrieve cluster service list with status via Ambari REST API
    - Provide service names, current state, and cluster information
    - Include detailed link information for each service
    - Display visual indicators for service status
    
    [Required Usage Scenarios]:
    - When users mention "service list", "cluster services", "Ambari services"
    - When cluster status check is needed
    - When service management requires current status overview
    - When real-time cluster information is absolutely necessary
    
    [Absolutely Prohibited Scenarios]:
    - General Hadoop knowledge questions
    - Service installation or configuration changes
    - Log viewing or performance monitoring
    - Requests belonging to other cluster management tools
    
    Returns:
        Cluster service list with status information (success: service list with status, failure: error message)
    """
    cluster_name = AMBARI_CLUSTER_NAME
    try:
        endpoint = f"/clusters/{cluster_name}/services?fields=ServiceInfo/service_name,ServiceInfo/state,ServiceInfo/cluster_name"
        response_data = await make_ambari_request(endpoint)
        
        if response_data is None:
            return f"Error: Unable to retrieve service list for cluster '{cluster_name}'."
        
        if "items" not in response_data:
            return f"No results: No services found in cluster '{cluster_name}'."
        
        services = response_data["items"]
        if not services:
            return f"No results: No services installed in cluster '{cluster_name}'."
        
        # Format results
        result_lines = [f"Service list for cluster '{cluster_name}' ({len(services)} services):"]
        result_lines.append("=" * 50)
        
        for i, service in enumerate(services, 1):
            service_info = service.get("ServiceInfo", {})
            service_name = service_info.get("service_name", "Unknown")
            state = service_info.get("state", "Unknown")
            service_href = service.get("href", "")
            
            result_lines.append(f"{i}. Service Name: {service_name} [{state}]")
            result_lines.append(f"   Cluster: {service_info.get('cluster_name', cluster_name)}")
            result_lines.append(f"   API Link: {service_href}")
            result_lines.append("")
        
        return "\n".join(result_lines)
        
    except Exception as e:
        return f"Error: Exception occurred while retrieving service list - {str(e)}"

@mcp.tool()
@log_tool
async def get_service_status(service_name: str) -> str:
    """
    Retrieves the status information for a specific service in an Ambari cluster.
    
    [Tool Role]: Dedicated tool for real-time retrieval of specific service status and state information
    
    [Core Functions]:
    - Retrieve specific service status via Ambari REST API
    - Provide detailed service state information (STARTED, STOPPED, INSTALLING, etc.)
    - Include service configuration and component information
    
    [Required Usage Scenarios]:
    - When users ask about specific service status (e.g., "HDFS status", "YARN state")
    - When troubleshooting service issues
    - When monitoring specific service health
    
    Args:
        service_name: Name of the service to check (e.g., "HDFS", "YARN", "HBASE")
    
    Returns:
        Service status information (success: detailed status, failure: error message)
    """
    cluster_name = AMBARI_CLUSTER_NAME
    try:
        endpoint = f"/clusters/{cluster_name}/services/{service_name}?fields=ServiceInfo/state,ServiceInfo/service_name,ServiceInfo/cluster_name"
        response_data = await make_ambari_request(endpoint)
        
        if response_data is None:
            return f"Error: Unable to retrieve status for service '{service_name}' in cluster '{cluster_name}'."
        
        service_info = response_data.get("ServiceInfo", {})
        
        result_lines = [f"Service Status for '{service_name}':"]
        result_lines.append("=" * 40)
        result_lines.append(f"Service Name: {service_info.get('service_name', service_name)}")
        result_lines.append(f"Cluster: {service_info.get('cluster_name', cluster_name)}")
        result_lines.append(f"Current State: {service_info.get('state', 'Unknown')}")
        
        # Add state description
        state = service_info.get('state', 'Unknown')
        state_descriptions = {
            'STARTED': 'Service is running and operational',
            'INSTALLED': 'Service is installed but not running',
            'STARTING': 'Service is in the process of starting',
            'STOPPING': 'Service is in the process of stopping',
            'INSTALLING': 'Service is being installed',
            'INSTALL_FAILED': 'Service installation failed',
            'MAINTENANCE': 'Service is in maintenance mode',
            'UNKNOWN': 'Service state cannot be determined'
        }
        
        if state in state_descriptions:
            result_lines.append(f"Description: {state_descriptions[state]}")
        
        return "\n".join(result_lines)
        
    except Exception as e:
        return f"Error: Exception occurred while retrieving service status - {str(e)}"

@mcp.tool()
@log_tool
async def get_service_components(service_name: str) -> str:
    """
    Retrieves detailed components information for a specific service in the Ambari cluster.

    [Tool Role]: Dedicated tool for retrieving service component details and host assignments.

    [Core Functions]:
    - List all components for a service, including state and category
    - Show host assignments and instance counts
    - Provide formatted output for LLM automation and troubleshooting

    [Required Usage Scenarios]:
    - When users request service component details or host info
    - When troubleshooting service health or scaling
    - When users mention component list, host assignments, or service breakdown

    Args:
        service_name: Name of the service (e.g., "HDFS", "YARN", "HBASE")

    Returns:
        Service components detailed information (success: formatted list, failure: English error message)
    """
    cluster_name = AMBARI_CLUSTER_NAME
    try:
        # Get detailed component information including host components
        endpoint = f"/clusters/{cluster_name}/services/{service_name}/components?fields=ServiceComponentInfo/component_name,ServiceComponentInfo/state,ServiceComponentInfo/category,ServiceComponentInfo/started_count,ServiceComponentInfo/installed_count,ServiceComponentInfo/total_count,host_components/HostRoles/host_name,host_components/HostRoles/state"
        response_data = await make_ambari_request(endpoint)
        
        if response_data is None:
            return f"Error: Unable to retrieve components for service '{service_name}' in cluster '{cluster_name}'."
        
        if "items" not in response_data:
            return f"No components found for service '{service_name}' in cluster '{cluster_name}'."
        
        components = response_data["items"]
        if not components:
            return f"No components found for service '{service_name}' in cluster '{cluster_name}'."
        
        result_lines = [f"Detailed Components for service '{service_name}':"]
        result_lines.append("=" * 60)
        result_lines.append(f"Total Components: {len(components)}")
        result_lines.append("")
        
        for i, component in enumerate(components, 1):
            comp_info = component.get("ServiceComponentInfo", {})
            comp_name = comp_info.get("component_name", "Unknown")
            comp_state = comp_info.get("state", "Unknown")
            comp_category = comp_info.get("category", "Unknown")
            
            # Component counts
            started_count = comp_info.get("started_count", 0)
            installed_count = comp_info.get("installed_count", 0)
            total_count = comp_info.get("total_count", 0)
            
            # Host components information
            host_components = component.get("host_components", [])
            
            result_lines.append(f"{i}. Component: {comp_name}")
            result_lines.append(f"   State: {comp_state}")
            result_lines.append(f"   Category: {comp_category}")
            
            # Add component state description
            state_descriptions = {
                'STARTED': 'Component is running',
                'INSTALLED': 'Component is installed but not running',
                'STARTING': 'Component is starting',
                'STOPPING': 'Component is stopping',
                'INSTALL_FAILED': 'Component installation failed',
                'MAINTENANCE': 'Component is in maintenance mode',
                'UNKNOWN': 'Component state is unknown'
            }
            
            if comp_state in state_descriptions:
                result_lines.append(f"   Description: {state_descriptions[comp_state]}")
            
            # Add instance counts if available
            if total_count > 0:
                result_lines.append(f"   Instances: {started_count} started / {installed_count} installed / {total_count} total")
            
            # Add host information
            if host_components:
                result_lines.append(f"   Hosts ({len(host_components)} instances):")
                for j, host_comp in enumerate(host_components[:5], 1):  # Show first 5 hosts
                    host_roles = host_comp.get("HostRoles", {})
                    host_name = host_roles.get("host_name", "Unknown")
                    host_state = host_roles.get("state", "Unknown")
                    result_lines.append(f"      {j}. {host_name} [{host_state}]")
                
                if len(host_components) > 5:
                    result_lines.append(f"      ... and {len(host_components) - 5} more hosts")
            else:
                result_lines.append("   Hosts: No host assignments found")
            
            result_lines.append("")
        
        # Add summary statistics
        total_instances = sum(len(comp.get("host_components", [])) for comp in components)
        started_components = len([comp for comp in components if comp.get("ServiceComponentInfo", {}).get("state") == "STARTED"])
        
        result_lines.append("Summary:")
        result_lines.append(f"  - Components: {len(components)} total, {started_components} started")
        result_lines.append(f"  - Total component instances across all hosts: {total_instances}")
        
        return "\n".join(result_lines)
        
    except Exception as e:
        return f"Error: Exception occurred while retrieving components for service '{service_name}' - {str(e)}"

@mcp.tool()
@log_tool
async def get_service_details(service_name: str) -> str:
    """
    Retrieves detailed status and configuration information for a specific service in the Ambari cluster.

    [Tool Role]: Dedicated tool for retrieving comprehensive service details, including state, components, and configuration.

    [Core Functions]:
    - Retrieve service state, component list, and configuration availability
    - Provide formatted output for LLM automation and troubleshooting

    [Required Usage Scenarios]:
    - When users request detailed service info or breakdown
    - When troubleshooting service health or auditing service setup
    - When users mention service details, service summary, or configuration status

    Args:
        service_name: Name of the service to check (e.g., "HDFS", "YARN", "HBASE")

    Returns:
        Detailed service information (success: comprehensive details, failure: English error message)
    """
    cluster_name = AMBARI_CLUSTER_NAME
    try:
        # First check if cluster exists
        cluster_endpoint = f"/clusters/{cluster_name}"
        cluster_response = await make_ambari_request(cluster_endpoint)
        
        if cluster_response is None:
            return f"Error: Cluster '{cluster_name}' not found or inaccessible. Please check cluster name and Ambari server connection."
        
        # Get detailed service information
        service_endpoint = f"/clusters/{cluster_name}/services/{service_name}?fields=ServiceInfo,components/ServiceComponentInfo"
        service_response = await make_ambari_request(service_endpoint)
        
        if service_response is None:
            return f"Error: Service '{service_name}' not found in cluster '{cluster_name}'. Please check service name."
        
        service_info = service_response.get("ServiceInfo", {})
        components = service_response.get("components", [])
        
        result_lines = [f"Detailed Service Information:"]
        result_lines.append("=" * 50)
        result_lines.append(f"Service Name: {service_info.get('service_name', service_name)}")
        result_lines.append(f"Cluster: {service_info.get('cluster_name', cluster_name)}")
        result_lines.append(f"Current State: {service_info.get('state', 'Unknown')}")
        
        # Add state description
        state = service_info.get('state', 'Unknown')
        state_descriptions = {
            'STARTED': 'Service is running and operational',
            'INSTALLED': 'Service is installed but not running', 
            'STARTING': 'Service is in the process of starting',
            'STOPPING': 'Service is in the process of stopping',
            'INSTALLING': 'Service is being installed',
            'INSTALL_FAILED': 'Service installation failed',
            'MAINTENANCE': 'Service is in maintenance mode',
            'UNKNOWN': 'Service state cannot be determined'
        }
        
        if state in state_descriptions:
            result_lines.append(f"Description: {state_descriptions[state]}")
        
        # Add component information
        if components:
            result_lines.append(f"\nComponents ({len(components)} total):")
            for i, component in enumerate(components, 1):
                comp_info = component.get("ServiceComponentInfo", {})
                comp_name = comp_info.get("component_name", "Unknown")
                result_lines.append(f"   {i}. {comp_name}")
        else:
            result_lines.append(f"\nComponents: No components found")
        
        # Add additional service info if available
        if "desired_configs" in service_info:
            result_lines.append(f"\nConfiguration: Available")
        
        result_lines.append(f"\nAPI Endpoint: {service_response.get('href', 'Not available')}")
        
        return "\n".join(result_lines)
        
    except Exception as e:
        return f"Error: Exception occurred while retrieving service details - {str(e)}"

@mcp.tool()
@log_tool
async def start_all_services() -> str:
    """
    Starts all services in an Ambari cluster (equivalent to "Start All" in Ambari Web UI).

    [Tool Role]: Dedicated tool for bulk starting all services in the cluster, automating mass startup.

    [Core Functions]:
    - Start all installed services simultaneously
    - Return request information for progress tracking
    - Provide clear success or error message for LLM automation

    [Required Usage Scenarios]:
    - When users request to "start all services", "start everything", "cluster startup"
    - When recovering cluster after maintenance or outage
    - When users mention mass startup, bulk start, or cluster bring-up

    Returns:
        Start operation result (success: request info, failure: English error message)
    """
    cluster_name = AMBARI_CLUSTER_NAME
    try:
        # First check cluster exists
        cluster_endpoint = f"/clusters/{cluster_name}"
        cluster_response = await make_ambari_request(cluster_endpoint)
        
        if cluster_response.get("error"):
            return f"Error: Cluster '{cluster_name}' not found or inaccessible. {cluster_response['error']}"
        
        # Try the standard bulk start approach first
        endpoint = f"/clusters/{cluster_name}/services"
        payload = {
            "RequestInfo": {
                "context": "Start All Services via MCP API",
                "operation_level": {
                    "level": "CLUSTER",
                    "cluster_name": cluster_name
                }
            },
            "Body": {
                "ServiceInfo": {
                    "state": "STARTED"
                }
            }
        }
        
        response_data = await make_ambari_request(endpoint, method="PUT", data=payload)
        
        if response_data.get("error"):
            # If bulk approach fails, try alternative approach
            alt_endpoint = f"/clusters/{cluster_name}/services?ServiceInfo/state=INSTALLED"
            alt_payload = {
                "ServiceInfo": {
                    "state": "STARTED"
                }
            }
            
            response_data = await make_ambari_request(alt_endpoint, method="PUT", data=alt_payload)
            
            if response_data.get("error"):
                return f"Error: Failed to start services in cluster '{cluster_name}'. {response_data['error']}"
        
        # Extract request information
        request_info = response_data.get("Requests", {})
        request_id = request_info.get("id", "Unknown")
        request_status = request_info.get("status", "Unknown")
        request_href = response_data.get("href", "")
        
        result_lines = [f"Start All Services Operation Initiated:"]
        result_lines.append("=" * 50)
        result_lines.append(f"Cluster: {cluster_name}")
        result_lines.append(f"Request ID: {request_id}")
        result_lines.append(f"Status: {request_status}")
        result_lines.append(f"Monitor URL: {request_href}")
        result_lines.append("")
        result_lines.append("Note: This operation may take several minutes to complete.")
        result_lines.append("    Use get_request_status(request_id) to track progress.")
        
        return "\n".join(result_lines)
        
    except Exception as e:
        return f"Error: Exception occurred while starting all services - {str(e)}"

@mcp.tool()
@log_tool
async def stop_all_services() -> str:
    """
    Stops all services in an Ambari cluster (equivalent to "Stop All" in Ambari Web UI).

    [Tool Role]: Dedicated tool for bulk stopping all services in the cluster, automating mass shutdown.

    [Core Functions]:
    - Stop all running services simultaneously
    - Return request information for progress tracking
    - Provide clear success or error message for LLM automation

    [Required Usage Scenarios]:
    - When users request to "stop all services", "stop everything", "cluster shutdown"
    - When cluster maintenance or troubleshooting requires mass shutdown
    - When users mention mass shutdown, bulk stop, or cluster halt

    Returns:
        Stop operation result (success: request info, failure: English error message)
    """
    cluster_name = AMBARI_CLUSTER_NAME
    try:
        # First, check if cluster is accessible
        cluster_endpoint = f"/clusters/{cluster_name}"
        cluster_response = await make_ambari_request(cluster_endpoint)
        
        if cluster_response.get("error"):
            return f"Error: Cluster '{cluster_name}' not found or inaccessible. {cluster_response['error']}"
        
        # Get all services that are currently STARTED
        services_endpoint = f"/clusters/{cluster_name}/services?ServiceInfo/state=STARTED"
        services_response = await make_ambari_request(services_endpoint)
        
        if services_response.get("error"):
            return f"Error retrieving services: {services_response['error']}"
        
        services = services_response.get("items", [])
        if not services:
            return "No services are currently running. All services are already stopped."
        
        # Try the standard bulk stop approach first
        stop_endpoint = f"/clusters/{cluster_name}/services"
        stop_payload = {
            "RequestInfo": {
                "context": "Stop All Services via MCP API",
                "operation_level": {
                    "level": "CLUSTER",
                    "cluster_name": cluster_name
                }
            },
            "Body": {
                "ServiceInfo": {
                    "state": "INSTALLED"
                }
            }
        }
        
        stop_response = await make_ambari_request(stop_endpoint, method="PUT", data=stop_payload)
        
        if stop_response.get("error"):
            # If bulk approach fails, try alternative approach
            alt_endpoint = f"/clusters/{cluster_name}/services?ServiceInfo/state=STARTED"
            alt_payload = {
                "ServiceInfo": {
                    "state": "INSTALLED"
                }
            }
            
            stop_response = await make_ambari_request(alt_endpoint, method="PUT", data=stop_payload)
            
            if stop_response.get("error"):
                return f"Error: Failed to stop services in cluster '{cluster_name}'. {stop_response['error']}"
        
        # Parse successful response
        request_info = stop_response.get("Requests", {})
        request_id = request_info.get("id", "Unknown")
        request_status = request_info.get("status", "Unknown")
        request_href = stop_response.get("href", "")
        
        result_lines = [
            "STOP ALL SERVICES INITIATED",
            "",
            f"Cluster: {cluster_name}",
            f"Request ID: {request_id}",
            f"Status: {request_status}",
            f"Monitor URL: {request_href}",
            "",
            "Note: This operation may take several minutes to complete.",
            "    Use get_request_status(request_id) to track progress."
        ]
        
        return "\n".join(result_lines)
        
    except Exception as e:
        return f"Error: Exception occurred while stopping all services - {str(e)}"

@mcp.tool()
@log_tool
async def start_service(service_name: str) -> str:
    """
    Starts a specific service in the Ambari cluster.

    [Tool Role]: Dedicated tool for automated start of Ambari services, ensuring safe and monitored startup.

    [Core Functions]:
    - Start the specified service and initiate Ambari request
    - Return request information for progress tracking
    - Provide clear success or error message for LLM automation

    [Required Usage Scenarios]:
    - When users request to "start" a service (e.g., "start HDFS", "start YARN")
    - When recovering stopped services
    - When maintenance or configuration changes require a service start
    - When users mention service start, bring up service, or automated start

    Args:
        service_name: Name of the service to start (e.g., "HDFS", "YARN", "HBASE")

    Returns:
        Start operation result (success: request info, failure: error message)
        - Success: Multi-line string with request ID, status, monitor URL, and instructions for progress tracking
        - Failure: English error message describing the problem
    """
    cluster_name = AMBARI_CLUSTER_NAME
    try:
        # Check if service exists and get current status
        service_endpoint = f"/clusters/{cluster_name}/services/{service_name}"
        service_check = await make_ambari_request(service_endpoint)
        
        if service_check is None or service_check.get("error"):
            return f"Error: Service '{service_name}' not found in cluster '{cluster_name}'."
        
        # Check current service state
        service_info = service_check.get("ServiceInfo", {})
        current_state = service_info.get("state", "UNKNOWN")
        
        # If service is already started, return appropriate message
        if current_state == "STARTED":
            return f"Service '{service_name}' is already running (state: {current_state}). No action needed."
        
        # Start the service
        payload = {
            "RequestInfo": {
                "context": f"Start Service {service_name} via MCP API"
            },
            "Body": {
                "ServiceInfo": {
                    "state": "STARTED"
                }
            }
        }
        
        response_data = await make_ambari_request(service_endpoint, method="PUT", data=payload)
        
        if response_data is None or response_data.get("error"):
            error_msg = response_data.get("error") if response_data else "Unknown error occurred"
            return f"Error: Failed to start service '{service_name}' - {error_msg}"
        
        # Extract request information safely
        request_info = response_data.get("Requests")
        if request_info is None:
            # If no Requests field, but no error, the service might have started immediately
            return f"Service '{service_name}' start command sent successfully. Previous state: {current_state}"
        
        request_id = request_info.get("id", "Unknown")
        request_status = request_info.get("status", "Unknown")
        request_href = response_data.get("href", "")
        
        result_lines = [
            f"START SERVICE: {service_name}",
            "",
            f"Cluster: {cluster_name}",
            f"Service: {service_name}",
            f"Previous State: {current_state}",
            f"Request ID: {request_id}",
            f"Status: {request_status}",
            f"Monitor URL: {request_href}",
            "",
            "Use get_request_status(request_id) to track progress."
        ]
        
        return "\n".join(result_lines)
        
    except Exception as e:
        return f"Error: Exception occurred while starting service '{service_name}' - {str(e)}"

@mcp.tool()
@log_tool
async def stop_service(service_name: str) -> str:
    """
    Stops a specific service in the Ambari cluster.

    [Tool Role]: Dedicated tool for automated stop of Ambari services, ensuring safe and monitored shutdown.

    [Core Functions]:
    - Stop the specified service and initiate Ambari request
    - Return request information for progress tracking
    - Provide clear success or error message for LLM automation

    [Required Usage Scenarios]:
    - When users request to "stop" a service (e.g., "stop HDFS", "stop YARN")
    - When maintenance or troubleshooting requires a service shutdown
    - When users mention service stop, shutdown, or automated stop

    Args:
        service_name: Name of the service to stop (e.g., "HDFS", "YARN", "HBASE")

    Returns:
        Stop operation result (success: request info, failure: error message)
        - Success: Multi-line string with request ID, status, monitor URL, and instructions for progress tracking
        - Failure: English error message describing the problem
    """
    cluster_name = AMBARI_CLUSTER_NAME
    try:
        # Check if service exists and get current status
        service_endpoint = f"/clusters/{cluster_name}/services/{service_name}"
        service_check = await make_ambari_request(service_endpoint)
        
        if service_check is None or service_check.get("error"):
            return f"Error: Service '{service_name}' not found in cluster '{cluster_name}'."
        
        # Check current service state
        service_info = service_check.get("ServiceInfo", {})
        current_state = service_info.get("state", "UNKNOWN")
        
        # If service is already stopped, return appropriate message
        if current_state in ["INSTALLED", "INSTALL_FAILED"]:
            return f"Service '{service_name}' is already stopped (state: {current_state}). No action needed."
        
        # Stop the service (set state to INSTALLED)
        payload = {
            "RequestInfo": {
                "context": f"Stop Service {service_name} via MCP API"
            },
            "Body": {
                "ServiceInfo": {
                    "state": "INSTALLED"
                }
            }
        }
        
        response_data = await make_ambari_request(service_endpoint, method="PUT", data=payload)
        
        if response_data is None or response_data.get("error"):
            error_msg = response_data.get("error") if response_data else "Unknown error occurred"
            return f"Error: Failed to stop service '{service_name}' - {error_msg}"
        
        # Extract request information safely
        request_info = response_data.get("Requests")
        if request_info is None:
            # If no Requests field, but no error, the service might have stopped immediately
            return f"Service '{service_name}' stop command sent successfully. Previous state: {current_state}"
        
        request_id = request_info.get("id", "Unknown")
        request_status = request_info.get("status", "Unknown")
        request_href = response_data.get("href", "")
        
        result_lines = [
            f"STOP SERVICE: {service_name}",
            "",
            f"Cluster: {cluster_name}",
            f"Service: {service_name}",
            f"Previous State: {current_state}",
            f"Request ID: {request_id}",
            f"Status: {request_status}",
            f"Monitor URL: {request_href}",
            "",
            "Use get_request_status(request_id) to track progress."
        ]
        
        return "\n".join(result_lines)
        
    except Exception as e:
        return f"Error: Exception occurred while stopping service '{service_name}' - {str(e)}"

@mcp.tool()
@log_tool
async def get_request_status(request_id: str) -> str:
    """
    Retrieves the status and progress of a specific Ambari request operation.
    
    [Tool Role]: Dedicated tool for real-time tracking and reporting of Ambari request status.
    
    [Core Functions]:
    - Query the status, progress, and context of a request by its ID
    - Provide detailed status (PENDING, IN_PROGRESS, COMPLETED, FAILED, etc.)
    - Show progress percentage and timing information
    - Return actionable status for automation and LLM integration
    
    [Required Usage Scenarios]:
    - When users ask for the status or progress of a specific operation/request
    - When monitoring or troubleshooting Ambari operations
    - When tracking bulk or individual service actions
    - When users mention request ID, operation status, or progress
    
    Args:
        request_id: ID of the Ambari request to check (int)
    
    Returns:
        Request status information (success: detailed status and progress, failure: error message)
        - Success: Multi-line string with request ID, status, progress, context, start/end time, and status description
        - Failure: English error message describing the problem
    """
    cluster_name = AMBARI_CLUSTER_NAME
    try:
        endpoint = f"/clusters/{cluster_name}/requests/{request_id}"
        response_data = await make_ambari_request(endpoint)
        
        if response_data.get("error"):
            return f"Error: Request '{request_id}' not found in cluster '{cluster_name}'."
        
        request_info = response_data.get("Requests", {})
        
        result_lines = [
            f"REQUEST STATUS: {request_id}",
            "",
            f"Cluster: {cluster_name}",
            f"Request ID: {request_info.get('id', request_id)}",
            f"Status: {request_info.get('request_status', 'Unknown')}",
            f"Progress: {request_info.get('progress_percent', 0)}%"
        ]
        
        if "request_context" in request_info:
            result_lines.append(f"Context: {request_info['request_context']}")
        
        if "start_time" in request_info:
            result_lines.append(f"Start Time: {request_info['start_time']}")
        
        if "end_time" in request_info:
            result_lines.append(f"End Time: {request_info['end_time']}")
        
        # Add status explanation
        status = request_info.get('request_status', 'Unknown')
        status_descriptions = {
            'PENDING': 'Request is pending execution',
            'IN_PROGRESS': 'Request is currently running',
            'COMPLETED': 'Request completed successfully',
            'FAILED': 'Request failed',
            'ABORTED': 'Request was aborted',
            'TIMEDOUT': 'Request timed out'
        }
        
        if status in status_descriptions:
            result_lines.append(f"Description: {status_descriptions[status]}")
        
        return "\n".join(result_lines)
        
    except Exception as e:
        return f"Error: Exception occurred while retrieving request status - {str(e)}"

@mcp.tool()
@log_tool
async def restart_service(service_name: str) -> str:
    """
    Restarts a specific service in an Ambari cluster (stop then start).

    [Tool Role]: Dedicated tool for automated restart of Ambari services, ensuring safe stop and start sequence.

    [Core Functions]:
    - Stop the specified service and wait for completion
    - Start the service and wait for completion
    - Return clear success or error message for LLM automation

    [Required Usage Scenarios]:
    - When users request to "restart" a service (e.g., "restart HDFS", "restart YARN")
    - When troubleshooting or recovering service issues
    - When maintenance or configuration changes require a restart
    - When users mention service restart, safe restart, or automated restart

    Args:
        service_name: Name of the service to restart (e.g., "HDFS", "YARN")

    Returns:
        Restart operation result (success: English completion message, failure: English error message)
        - Success: "Service '<service_name>' restart operation completed successfully."
        - Failure: "Error: ..." with details
    """
    cluster_name = AMBARI_CLUSTER_NAME

    try:
        # Check if service exists and get current status first
        service_endpoint = f"/clusters/{cluster_name}/services/{service_name}"
        service_check = await make_ambari_request(service_endpoint)
        
        if service_check is None or service_check.get("error"):
            return f"Error: Service '{service_name}' not found in cluster '{cluster_name}'."
        
        # Get current service state for better feedback
        service_info = service_check.get("ServiceInfo", {})
        initial_state = service_info.get("state", "UNKNOWN")
        
        # Check for existing active requests for this service
        active_requests = await check_service_active_requests(cluster_name, service_name)
        if active_requests:
            active_info = []
            for req in active_requests:
                active_info.append(f"Request ID {req['id']}: {req['context']} (Status: {req['status']}, Progress: {req['progress']}%)")
            
            return f"""Service '{service_name}' has active operations in progress. Please wait for completion before restarting.

Active operations:
{chr(10).join(active_info)}

Recommendation:
- Use get_request_status(request_id) to monitor progress
- Wait for completion before attempting restart
- Or check get_active_requests() for all cluster operations

Current service state: {initial_state}"""
        
        # Step 1: Stop the service
        logger.info("Stopping service '%s' (current state: %s)...", service_name, initial_state)
        stop_endpoint = f"/clusters/{cluster_name}/services/{service_name}"
        stop_payload = {
            "RequestInfo": {
                "context": f"Stop {service_name} service via MCP API",
                "operation_level": {
                    "level": "SERVICE",
                    "cluster_name": cluster_name,
                    "service_name": service_name
                }
            },
            "Body": {
                "ServiceInfo": {
                    "state": "INSTALLED"
                }
            }
        }

        stop_response = await make_ambari_request(stop_endpoint, method="PUT", data=stop_payload)

        if stop_response is None or stop_response.get("error"):
            error_msg = stop_response.get("error") if stop_response else "Unknown error occurred"
            return f"Error: Unable to stop service '{service_name}'. {error_msg}"

        # Extract stop request information safely
        stop_requests = stop_response.get("Requests")
        if stop_requests is None:
            # If service was already stopped, continue with start
            logger.info("Service '%s' may already be stopped, proceeding with start...", service_name)
            stop_request_id = "N/A (already stopped)"
        else:
            stop_request_id = stop_requests.get("id", "Unknown")
            if stop_request_id == "Unknown":
                return f"Error: Failed to retrieve stop request ID for service '{service_name}'."

            # Step 2: Wait for the stop operation to complete (print progress only for stop)
            while True:
                status_endpoint = f"/clusters/{cluster_name}/requests/{stop_request_id}"
                status_response = await make_ambari_request(status_endpoint)

                if status_response is None or status_response.get("error"):
                    error_msg = status_response.get("error") if status_response else "Unknown error occurred"
                    return f"Error: Unable to check status of stop operation for service '{service_name}'. {error_msg}"

                request_info = status_response.get("Requests", {})
                request_status = request_info.get("request_status", "Unknown")
                progress_percent = request_info.get("progress_percent", 0)

                if request_status == "COMPLETED":
                    break
                elif request_status in ["FAILED", "ABORTED"]:
                    return f"Error: Stop operation for service '{service_name}' failed with status '{request_status}'."

                logger.info("Stopping service '%s'... Progress: %d%%", service_name, progress_percent)
                await asyncio.sleep(2)  # Wait for 2 seconds before checking again

    # Step 3: Start the service (no progress output beyond capturing request id)
        start_endpoint = f"/clusters/{cluster_name}/services/{service_name}"
        start_payload = {
            "RequestInfo": {
                "context": f"Start {service_name} service via MCP API",
                "operation_level": {
                    "level": "SERVICE",
                    "cluster_name": cluster_name,
                    "service_name": service_name
                }
            },
            "Body": {
                "ServiceInfo": {
                    "state": "STARTED"
                }
            }
        }

        start_response = await make_ambari_request(start_endpoint, method="PUT", data=start_payload)

        if start_response is None or start_response.get("error"):
            error_msg = start_response.get("error") if start_response else "Unknown error occurred"
            return f"Error: Unable to start service '{service_name}'. {error_msg}"

        # Extract start request information safely
        start_requests = start_response.get("Requests")
        if start_requests is None:
            # If no Requests field, service might have started immediately
            logger.info("Service '%s' successfully restarted.", service_name)
            result_lines = [
                f"RESTART SERVICE: {service_name}",
                f"Stop Request ID: {stop_request_id}",
                f"Start Request ID: N/A (immediate)",
                "",
                f"Cluster: {cluster_name}",
                f"Service: {service_name}",
                f"Initial State: {initial_state}",
                f"Stop Status: COMPLETED",
                f"Start Status: Command sent successfully",
                "",
                f"Next: get_service_status(\"{service_name}\") to verify current state.",
            ]
            return "\n".join(result_lines)
        
        start_request_id = start_requests.get("id", "Unknown")
        start_status = start_requests.get("status", "Unknown")
        start_href = start_response.get("href", "")

        logger.info("Service '%s' successfully restarted.", service_name)
        result_lines = [
            f"RESTART SERVICE: {service_name}",
            f"Stop Request ID: {stop_request_id}",
            f"Start Request ID: {start_request_id}",
            "",
            f"Cluster: {cluster_name}",
            f"Service: {service_name}",
            f"Initial State: {initial_state}",
            f"Stop Status: COMPLETED",  # by this point stop loop exited on COMPLETED
            f"Start Status: {start_status}",
            f"Start Monitor URL: {start_href}",
            "",
            f"Next: get_request_status({start_request_id}) for updates." if start_request_id != "Unknown" else "Next: get_service_status(\"{service_name}\") to verify state soon.",
        ]
        return "\n".join(result_lines)

    except Exception as e:
        logger.error("Error occurred while restarting service '%s': %s", service_name, str(e))
        return f"Error: Service '{service_name}' restart operation failed: {str(e)}"

@mcp.tool()
@log_tool
async def restart_all_services() -> str:
    """
    Restarts all services in the Ambari cluster (stop all, then start all).

    [Tool Role]: Dedicated tool for automated bulk restart of all Ambari services, ensuring safe stop and start sequence.

    [Core Functions]:
    - Stop all running services and wait for completion
    - Start all services and wait for completion
    - Return clear success or error message for LLM automation

    [Required Usage Scenarios]:
    - When users request to "restart all services", "bulk restart", "cluster-wide restart"
    - When troubleshooting or recovering cluster-wide issues
    - When maintenance or configuration changes require a full restart

    Returns:
        Bulk restart operation result (success: English completion message, failure: English error message)
        - Success: "All services restart operation completed successfully."
        - Failure: "Error: ..." with details
    """
    cluster_name = AMBARI_CLUSTER_NAME
    try:
        # Step 1: Stop all services
        stop_result = await stop_all_services()
        if stop_result.startswith("Error"):
            return f"Error: Unable to stop all services. {stop_result}"

        # Extract stop request ID
        lines = stop_result.splitlines()
        stop_request_id = None
        for line in lines:
            if line.startswith("Request ID:"):
                stop_request_id = line.split(":", 1)[1].strip()
                break
        if not stop_request_id or stop_request_id == "Unknown":
            return f"Error: Failed to retrieve stop request ID for all services."

        # Wait for stop operation to complete (no progress output)
        while True:
            status_result = await get_request_status(stop_request_id)
            if status_result.startswith("Error"):
                return f"Error: Unable to check status of stop operation for all services. {status_result}"
            if "Status: COMPLETED" in status_result:
                break
            elif "Status: FAILED" in status_result or "Status: ABORTED" in status_result:
                return f"Error: Stop operation for all services failed. {status_result}"
            await asyncio.sleep(2)

        # Step 2: Start all services (capture request id)
        start_result = await start_all_services()
        if start_result.startswith("Error"):
            return f"Error: Unable to start all services. {start_result}"

        # Extract start request ID
        start_lines = start_result.splitlines()
        start_request_id = None
        for line in start_lines:
            if line.startswith("Request ID:"):
                start_request_id = line.split(":", 1)[1].strip()
                break
        if not start_request_id:
            start_request_id = "Unknown"

        summary_lines = [
            "RESTART ALL SERVICES", "",
            f"Stop Request ID: {stop_request_id}",
            f"Start Request ID: {start_request_id}",
            "",
            "Note: Start phase is now in progress; may take several minutes.",
        ]
        if start_request_id != "Unknown":
            summary_lines.append(f"Next: get_request_status({start_request_id}) for updates.")
        else:
            summary_lines.append("Next: get_active_requests to monitor overall progress.")
        return "\n".join(summary_lines)

    except Exception as e:
        return f"Error: All services restart operation failed: {str(e)}"

@mcp.tool()
@log_tool
async def list_hosts() -> str:
    """
    Retrieves the list of hosts in the Ambari cluster.

    [Tool Role]: Dedicated tool for listing all hosts registered in the Ambari cluster.

    [Core Functions]:
    - Query Ambari REST API for host list
    - Return host names and API links
    - Provide formatted output for LLM automation and cluster management

    [Required Usage Scenarios]:
    - When users request cluster host list or host details
    - When auditing or monitoring cluster nodes

    Returns:
        List of hosts (success: formatted list, failure: error message)
    """
    cluster_name = AMBARI_CLUSTER_NAME
    try:
        endpoint = f"/clusters/{cluster_name}/hosts"
        response_data = await make_ambari_request(endpoint)

        if response_data is None or "items" not in response_data:
            return f"Error: Unable to retrieve hosts for cluster '{cluster_name}'."

        hosts = response_data["items"]
        if not hosts:
            return f"No hosts found in cluster '{cluster_name}'."

        result_lines = [f"Host list for cluster '{cluster_name}' ({len(hosts)} hosts):"]
        result_lines.append("=" * 50)

        for i, host in enumerate(hosts, 1):
            host_info = host.get("Hosts", {})
            host_name = host_info.get("host_name", "Unknown")
            host_href = host.get("href", "")
            result_lines.append(f"{i}. Host Name: {host_name}")
            result_lines.append(f"   API Link: {host_href}")
            result_lines.append("")

        return "\n".join(result_lines)

    except Exception as e:
        return f"Error: Exception occurred while retrieving hosts - {str(e)}"

@mcp.tool()
@log_tool
async def get_host_details(host_name: Optional[str] = None) -> str:
    """
    Retrieves detailed information for a specific host or all hosts in the Ambari cluster.

    [Tool Role]: Dedicated tool for retrieving comprehensive host details including metrics, hardware info, and components.

    [Core Functions]:
    - If host_name provided: Query specific host information
    - If host_name not provided: Query all hosts and their detailed information
    - Return host hardware specs, state, metrics, and assigned components
    - Provide formatted output for LLM automation and cluster management

    [Required Usage Scenarios]:
    - When users request specific host details or host status
    - When users request all hosts details or cluster-wide host information
    - When auditing or monitoring individual or all cluster nodes
    - When troubleshooting host-specific issues

    Args:
        host_name: Name of the specific host to retrieve details for (optional, e.g., "bigtop-hostname0.demo.local")

    Returns:
        Detailed host information (success: formatted details, failure: error message)
    """
    cluster_name = AMBARI_CLUSTER_NAME
    try:
        # Single host mode
        if host_name is not None:
            return await format_single_host_details(host_name, cluster_name, show_header=True)
        
        # Multi-host mode (all hosts)
        hosts_endpoint = f"/clusters/{cluster_name}/hosts"
        hosts_response = await make_ambari_request(hosts_endpoint)

        if hosts_response is None or "items" not in hosts_response:
            return f"Error: Unable to retrieve host list for cluster '{cluster_name}'."

        hosts = hosts_response["items"]
        if not hosts:
            return f"No hosts found in cluster '{cluster_name}'."

        result_lines = [
            f"Detailed Information for All Hosts in Cluster '{cluster_name}' ({len(hosts)} hosts):",
            "=" * 80,
            ""
        ]

        # Process each host
        for i, host in enumerate(hosts, 1):
            host_info = host.get("Hosts", {})
            current_host_name = host_info.get("host_name", "Unknown")
            
            result_lines.append(f"[{i}/{len(hosts)}] HOST: {current_host_name}")
            result_lines.append("-" * 60)

            # Get formatted details for this host
            host_details = await format_single_host_details(current_host_name, cluster_name, show_header=False)
            
            if host_details.startswith("Error:"):
                result_lines.append(f"Error: Unable to retrieve details for host '{current_host_name}'")
            else:
                result_lines.append(host_details)
            
            result_lines.append("")

        # Summary
        result_lines.extend([
            "SUMMARY:",
            f"Total Hosts: {len(hosts)}"
        ])
        
        return "\n".join(result_lines)

    except Exception as e:
        return f"Error: Exception occurred while retrieving host details - {str(e)}"

@mcp.tool()
@log_tool
async def list_users() -> str:
    """List all users in the Ambari system.
    
    Returns a formatted list of all users with their basic information.
    """
    try:
        response = await make_ambari_request("/users")
        
        if "error" in response:
            return f"Error: Failed to retrieve users - {response['error']}"
        
        if "items" not in response or not response["items"]:
            return "No users found in the system."
        
        result_lines = []
        result_lines.append("=== AMBARI USERS ===\n")
        
        # Header
        result_lines.append(f"{'User Name':<20} {'HREF':<50}")
        result_lines.append("-" * 70)
        
        for user in response["items"]:
            user_info = user.get("Users", {})
            user_name = user_info.get("user_name", "N/A")
            href = user.get("href", "N/A")
            
            result_lines.append(f"{user_name:<20} {href:<50}")
        
        result_lines.append("\n" + "=" * 70)
        result_lines.append(f"Total Users: {len(response['items'])}")
        
        return "\n".join(result_lines)
        
    except Exception as e:
        return f"Error: Exception occurred while retrieving users - {str(e)}"

@mcp.tool()
@log_tool
async def get_user(user_name: str) -> str:
    """Get detailed information about a specific user.
    
    Args:
        user_name: The username to retrieve details for
        
    Returns:
        Detailed user information including profile, permissions, and authentication sources
    """
    try:
        if not user_name:
            return "Error: user_name parameter is required"
        
        response = await make_ambari_request(f"/users/{user_name}")
        
        if "error" in response:
            return f"Error: Failed to retrieve user '{user_name}' - {response['error']}"
        
        if "Users" not in response:
            return f"Error: Invalid response format for user '{user_name}'"
        
        user_info = response["Users"]
        result_lines = []
        result_lines.append(f"=== USER DETAILS: {user_name} ===\n")
        
        # Basic Information
        result_lines.append("BASIC INFORMATION:")
        result_lines.append(f"  User ID: {user_info.get('user_id', 'N/A')}")
        result_lines.append(f"  User Name: {user_info.get('user_name', 'N/A')}")
        result_lines.append(f"  Local User Name: {user_info.get('local_user_name', 'N/A')}")
        result_lines.append(f"  Display Name: {user_info.get('display_name', 'N/A')}")
        result_lines.append(f"  User Type: {user_info.get('user_type', 'N/A')}")
        result_lines.append("")
        
        # Status Information
        result_lines.append("STATUS:")
        result_lines.append(f"  Admin: {user_info.get('admin', False)}")
        result_lines.append(f"  Active: {user_info.get('active', 'N/A')}")
        result_lines.append(f"  LDAP User: {user_info.get('ldap_user', False)}")
        result_lines.append(f"  Consecutive Failures: {user_info.get('consecutive_failures', 'N/A')}")
        result_lines.append("")
        
        # Timestamps
        created_timestamp = user_info.get('created')
        if created_timestamp:
            result_lines.append("TIMESTAMPS:")
            result_lines.append(f"  Created: {format_timestamp(created_timestamp)}")
            result_lines.append("")
        
        # Groups
        groups = user_info.get('groups', [])
        result_lines.append("GROUPS:")
        if groups:
            for group in groups:
                result_lines.append(f"  - {group}")
        else:
            result_lines.append("  (No groups assigned)")
        result_lines.append("")
        
        # Authentication Sources
        sources = response.get('sources', [])
        result_lines.append("AUTHENTICATION SOURCES:")
        if sources:
            for source in sources:
                source_info = source.get('AuthenticationSourceInfo', {})
                result_lines.append(f"  Source ID: {source_info.get('source_id', 'N/A')}")
                result_lines.append(f"  HREF: {source.get('href', 'N/A')}")
        else:
            result_lines.append("  (No authentication sources)")
        result_lines.append("")
        
        # Privileges
        privileges = response.get('privileges', [])
        result_lines.append("PRIVILEGES:")
        if privileges:
            for privilege in privileges:
                result_lines.append(f"  - {privilege}")
        else:
            result_lines.append("  (No privileges assigned)")
        result_lines.append("")
        
        # Widget Layouts
        widget_layouts = response.get('widget_layouts', [])
        result_lines.append("WIDGET LAYOUTS:")
        if widget_layouts:
            result_lines.append(f"  Count: {len(widget_layouts)}")
        else:
            result_lines.append("  (No widget layouts)")
        
        result_lines.append("\n" + "=" * 50)
        
        return "\n".join(result_lines)
        
    except Exception as e:
        return f"Error: Exception occurred while retrieving user '{user_name}' - {str(e)}"

@mcp.tool()
@log_tool
async def get_alerts_history(
    mode: str = "current",
    cluster_name: Optional[str] = None,
    service_name: Optional[str] = None,
    host_name: Optional[str] = None,
    state_filter: Optional[str] = None,
    definition_name: Optional[str] = None,
    # current mode only
    maintenance_state: Optional[str] = None,
    # history mode only  
    from_timestamp: Optional[int] = None,
    to_timestamp: Optional[int] = None,
    # NEW: provide current time context for LLM calculations
    include_time_context: bool = False,
    limit: Optional[int] = None,
    page_size: int = 100,
    start_page: int = 0,
    format: str = "detailed"
) -> str:
    """
    Retrieve current alerts or alert history from Ambari cluster.

    [Tool Role]: Unified tool for retrieving both current/active alert status and historical alert events from Ambari cluster
    
    [Core Functions]:
    - Current mode: Retrieve current alerts for entire cluster, specific service, or specific host
    - History mode: Retrieve alert history for entire cluster, specific service, or specific host  
    - Support filtering by alert state (CRITICAL, WARNING, OK, UNKNOWN)
    - Support filtering by definition name
    - Current mode: Support filtering by maintenance state (ON, OFF)
    - History mode: Support filtering by time range with from_timestamp/to_timestamp
    - Support different output formats (detailed, summary, compact, groupedSummary for current)
    - History mode: Provide pagination support for large datasets
    - Provide current time context for LLM natural language time calculations

    [Required Usage Scenarios]:
    - Current mode: When users request current alerts, active alerts, or alert status
    - Current mode: When monitoring immediate cluster health
    - Current mode: When investigating current issues or troubleshooting active problems
    - History mode: When users request alert history, past alerts, or historical alert data
    - History mode: When monitoring alert trends or analyzing alert patterns
    - History mode: When investigating past alert incidents or troubleshooting
    - When users mention alert status, current problems, cluster health, alert events, alert timeline, or alert logs

    Args:
        mode: "current" for active alerts, "history" for past events (default: "current")
        cluster_name: Name of cluster (uses default if not specified)
        service_name: Filter by specific service name (e.g., HDFS, YARN)
        host_name: Filter by specific host name
        state_filter: Filter by alert state (CRITICAL, WARNING, OK, UNKNOWN)
        definition_name: Filter by alert definition name
        maintenance_state: Filter by maintenance state (ON, OFF) - current mode only
        from_timestamp: Start timestamp in milliseconds (Unix epoch) - history mode only
        to_timestamp: End timestamp in milliseconds (Unix epoch) - history mode only
        include_time_context: Add current time information for LLM natural language processing
        limit: Maximum number of alert entries to return
        page_size: Number of entries per page (default: 100) - history mode only
        start_page: Starting page number (default: 0) - history mode only
        format: Output format - 'detailed', 'summary', 'compact', or 'groupedSummary' (current mode only)

    Returns:
        Alert information (success: formatted alerts, failure: English error message)
    """
    target_cluster = cluster_name or AMBARI_CLUSTER_NAME
    
    # Validate mode
    if mode not in ["current", "history"]:
        return f"Error: Invalid mode '{mode}'. Valid modes: current, history"
    
    # Normalize and validate timestamp inputs early (accept str or int)
    def _coerce_ts(name, val):
        if val is None:
            return None
        try:
            # Allow strings like "1754524800000" and ints
            if isinstance(val, str):
                val = val.strip()
            return int(val)
        except Exception:
            raise ValueError(f"Invalid {name}: must be Unix epoch milliseconds as integer or numeric string")

    try:
        from_timestamp = _coerce_ts("from_timestamp", from_timestamp)
        to_timestamp = _coerce_ts("to_timestamp", to_timestamp)
    except ValueError as e:
        return f"Error: {e}"

    # Coerce numeric params that may arrive as strings from clients
    def _coerce_int(name, val, allow_none=True):
        if val is None and allow_none:
            return None
        try:
            if isinstance(val, str):
                val = val.strip()
            return int(val)
        except Exception:
            raise ValueError(f"Invalid {name}: must be an integer")

    try:
        limit = _coerce_int("limit", limit, allow_none=True)
        page_size = _coerce_int("page_size", page_size, allow_none=False)
        start_page = _coerce_int("start_page", start_page, allow_none=False)
    except ValueError as e:
        return f"Error: {e}"

    # Normalize limit=0 to None (meaning no limit)
    if limit == 0:
        limit = None

    # Coerce include_time_context if string
    if isinstance(include_time_context, str):
        include_time_context = include_time_context.strip().lower() in ("1", "true", "yes", "y")
    
    # Prepare current time context if requested
    current_time_context = ""
    if include_time_context:
        current_time_context = get_current_time_context()
        if current_time_context.startswith("Error:"):
            return current_time_context  # Return error immediately
    
    try:
        # Build the endpoint URL based on mode and scope
        if mode == "history":
            base_path = "alert_history"
        else:  # current
            base_path = "alerts"
            
        if host_name:
            endpoint = f"/clusters/{target_cluster}/hosts/{host_name}/{base_path}"
        elif service_name:
            endpoint = f"/clusters/{target_cluster}/services/{service_name}/{base_path}"
        else:
            endpoint = f"/clusters/{target_cluster}/{base_path}"
        
        # Build query parameters
        query_params = []
        
        # Handle special format cases for current mode
        if mode == "current" and format == "summary":
            query_params.append("format=summary")
        elif mode == "current" and format == "groupedSummary":
            query_params.append("format=groupedSummary")
        else:
            # Add field specification for full data
            field_prefix = "AlertHistory" if mode == "history" else "Alert"
            query_params.append(f"fields={field_prefix}/*")
            
            # Build predicate filters
            predicates = []
            
            # Common filters
            if state_filter:
                state_upper = state_filter.upper()
                valid_states = ["CRITICAL", "WARNING", "OK", "UNKNOWN"]
                if state_upper in valid_states:
                    predicates.append(f"{field_prefix}/state={state_upper}")
                else:
                    return f"Error: Invalid state filter '{state_filter}'. Valid states: {', '.join(valid_states)}"
            
            if definition_name:
                predicates.append(f"{field_prefix}/definition_name={definition_name}")
                
            # Mode-specific filters
            if mode == "current" and maintenance_state:
                maintenance_upper = maintenance_state.upper()
                valid_maintenance = ["ON", "OFF"]
                if maintenance_upper in valid_maintenance:
                    predicates.append(f"Alert/maintenance_state={maintenance_upper}")
                else:
                    return f"Error: Invalid maintenance state '{maintenance_state}'. Valid states: {', '.join(valid_maintenance)}"
            elif mode == "history":
                # For history mode, try timestamp filtering with both int and string formats
                if from_timestamp or to_timestamp:
                    # First attempt: use integer timestamps (standard approach)
                    if from_timestamp:
                        predicates.append(f"AlertHistory/timestamp>={from_timestamp}")
                    if to_timestamp:
                        predicates.append(f"AlertHistory/timestamp<={to_timestamp}")
                    
                    # Note: If this fails due to type mismatch, we'll handle it in the fallback logic
            
            # Combine predicates
            if predicates:
                predicate_string = "(" + ")&(".join(predicates) + ")"
                query_params.append(predicate_string)
            
            # Add sorting
            if mode == "current":
                query_params.append("sortBy=Alert/state.desc,Alert/latest_timestamp.desc")
            else:  # history
                query_params.append("sortBy=AlertHistory/timestamp.desc")
                # Add pagination for history mode
                query_params.append(f"from={start_page * page_size}")
                if page_size > 0:
                    query_params.append(f"page_size={page_size}")
        
        # Construct full URL
        if query_params:
            endpoint += "?" + "&".join(query_params)
        
        response_data = await make_ambari_request(endpoint)
        client_side_filter_needed = False
        
        if response_data is None or "error" in response_data:
            error_msg = response_data.get("error", "Unknown error") if response_data else "No response"
            # For history mode with timestamp filters, always retry without timestamp predicates
            if mode == "history" and (from_timestamp or to_timestamp):
                logger.warning("Timestamp filtering failed, retrying without timestamp filters")
                # Rebuild query without timestamp predicates
                fallback_query_params = []
                fallback_predicates = []

                # Add basic filters
                fallback_query_params.append(f"fields={field_prefix}/*")
                # Re-add non-timestamp filters
                if state_filter:
                    state_upper = state_filter.upper()
                    if state_upper in ["CRITICAL", "WARNING", "OK", "UNKNOWN"]:
                        fallback_predicates.append(f"{field_prefix}/state={state_upper}")
                if definition_name:
                    fallback_predicates.append(f"{field_prefix}/definition_name={definition_name}")
                # Combine fallback predicates
                if fallback_predicates:
                    fallback_predicate_string = "(" + ")&(".join(fallback_predicates) + ")"
                    fallback_query_params.append(fallback_predicate_string)
                # Add sorting and pagination
                fallback_query_params.append("sortBy=AlertHistory/timestamp.desc")
                fallback_query_params.append(f"from={start_page * page_size}")
                if page_size > 0:
                    fallback_query_params.append(f"page_size={page_size}")
                # Build fallback endpoint
                fallback_endpoint = endpoint.split('?')[0] + "?" + "&".join(fallback_query_params)
                # Try the fallback request
                response_data = await make_ambari_request(fallback_endpoint)
                if response_data is None or "error" in response_data:
                    fallback_error = response_data.get("error", "Unknown error") if response_data else "No response"
                    error_msg = f"Primary request failed (timestamp filter issue), fallback also failed: {fallback_error}"
                else:
                    # Successful fallback - we'll need to filter client-side
                    client_side_filter_needed = True
        
        # Final error check after all attempts
        if response_data is None or "error" in response_data:
            final_error = response_data.get("error", "Unknown error") if response_data else "No response"
            # Include time context info even on errors if requested
            if current_time_context.strip():
                return f"{current_time_context.strip()}\n\nError: Unable to retrieve {mode} alerts - {final_error}"
            else:
                return f"Error: Unable to retrieve {mode} alerts - {final_error}"        # Apply client-side filtering if needed (when server-side timestamp filtering failed)
        if mode == "history" and client_side_filter_needed and (from_timestamp or to_timestamp):
            logger.info("Applying client-side timestamp filtering due to server-side type mismatch")
            items = response_data.get("items", [])
            filtered_items = []
            
            for item in items:
                alert = item.get("AlertHistory", {})
                timestamp = alert.get("timestamp", 0)
                
                # Apply timestamp filters using safe comparison
                if from_timestamp and not safe_timestamp_compare(timestamp, from_timestamp, '>='):
                    continue
                if to_timestamp and not safe_timestamp_compare(timestamp, to_timestamp, '<='):
                    continue
                    
                filtered_items.append(item)
            
            # Replace items with filtered items
            response_data["items"] = filtered_items
            logger.info(f"Client-side filtering: {len(items)} -> {len(filtered_items)} items")
        
        # Handle current mode special format cases
        if mode == "current" and format == "summary":
            alerts_summary = response_data.get("alerts_summary", {})
            if not alerts_summary:
                return "No alert summary data available"
            
            result_lines = [
                f"Alert Summary for {target_cluster}",
                "=" * 40
            ]
            
            total_alerts = 0
            for state in ["CRITICAL", "WARNING", "OK", "UNKNOWN"]:
                state_info = alerts_summary.get(state, {})
                count = state_info.get("count", 0)
                maintenance_count = state_info.get("maintenance_count", 0)
                original_timestamp = state_info.get("original_timestamp", 0)
                
                total_alerts += count
                
                result_lines.append(f"{state}: {count} alerts")
                if maintenance_count > 0:
                    result_lines.append(f"  (Maintenance: {maintenance_count})")
                if original_timestamp > 0:
                    result_lines.append(f"  (Latest: {format_timestamp(original_timestamp)})")
            
            result_lines.extend([
                "",
                f"Total Alerts: {total_alerts}",
                f"API Endpoint: {response_data.get('href', 'Not available')}"
            ])
            
            return "\n".join(result_lines)
        
        elif mode == "current" and format == "groupedSummary":
            alerts_summary_grouped = response_data.get("alerts_summary_grouped", [])
            if not alerts_summary_grouped:
                return "No grouped alert summary data available"
            
            result_lines = [
                f"Grouped Alert Summary for {target_cluster}",
                "=" * 50,
                f"Alert Definitions: {len(alerts_summary_grouped)}",
                ""
            ]
            
            for group in alerts_summary_grouped:
                definition_id = group.get("definition_id", "Unknown")
                definition_name = group.get("definition_name", "Unknown")
                summary = group.get("summary", {})
                
                result_lines.append(f"Definition: {definition_name} (ID: {definition_id})")
                
                total_count = 0
                for state in ["CRITICAL", "WARNING", "OK", "UNKNOWN"]:
                    state_info = summary.get(state, {})
                    count = state_info.get("count", 0)
                    maintenance_count = state_info.get("maintenance_count", 0)
                    latest_text = state_info.get("latest_text", "")
                    
                    if count > 0:
                        result_lines.append(f"  {state}: {count}")
                        if maintenance_count > 0:
                            result_lines.append(f"    Maintenance: {maintenance_count}")
                        if latest_text:
                            text_display = latest_text if len(latest_text) <= 80 else latest_text[:77] + "..."
                            result_lines.append(f"    Latest: {text_display}")
                    
                    total_count += count
                
                result_lines.append(f"  Total: {total_count}")
                result_lines.append("")
            
            return "\n".join(result_lines)
        
        # Handle regular processing with unified formatting function
        items = response_data.get("items", [])
        
        # Prepare parameters for formatting function
        format_params = {
            'definition_name': definition_name,
            'maintenance_state': maintenance_state if mode == "current" else None,
            'from_timestamp': from_timestamp if mode == "history" else None,
            'to_timestamp': to_timestamp if mode == "history" else None,
            'limit': limit
        }
        
        # Add pagination info for history mode
        if mode == "history":
            # Coerce total_count to int to avoid comparison errors between str and int
            raw_total = response_data.get("itemTotal", len(items))
            try:
                total_count = int(raw_total)
            except (TypeError, ValueError):
                total_count = len(items)
            format_params['total_count'] = total_count
            format_params['page_size'] = page_size
            format_params['start_page'] = start_page
            format_params['api_href'] = response_data.get('href', 'Not available')
        else:
            # Add summary statistics for current mode
            state_counts = {}
            maintenance_count = 0
            for item in items:
                alert = item.get("Alert", {})
                state = alert.get("state", "UNKNOWN")
                maintenance = alert.get("maintenance_state", "OFF")
                
                state_counts[state] = state_counts.get(state, 0) + 1
                if maintenance == "ON":
                    maintenance_count += 1
            
            format_params['state_counts'] = state_counts
            format_params['maintenance_count'] = maintenance_count
            format_params['api_href'] = response_data.get('href', 'Not available')
        
        # Use unified formatting function
        formatted_output = format_alerts_output(
            items, mode, target_cluster, format, 
            host_name, service_name, state_filter, **format_params
        )
        
        # Add mode-specific footer information
        result_lines = formatted_output.split('\n')
        
        # Add current time context if requested
        if current_time_context.strip():
            result_lines.insert(0, current_time_context.strip())
            result_lines.insert(1, "")
        
        if mode == "current":
            # Add summary statistics
            result_lines.extend([
                "",
                "Summary:",
                f"  Total Alerts: {len(items)}",
                f"  In Maintenance: {format_params.get('maintenance_count', 0)}",
            ])
            
            for state in ["CRITICAL", "WARNING", "OK", "UNKNOWN"]:
                count = format_params.get('state_counts', {}).get(state, 0)
                if count > 0:
                    result_lines.append(f"  {state}: {count}")
        
        elif mode == "history":
            # Safely add pagination information if total_count > number of items
            try:
                total_count = int(format_params.get('total_count', 0))
            except (TypeError, ValueError):
                total_count = 0
            if total_count > len(items):
                total_pages = (total_count + page_size - 1) // page_size
                result_lines.extend([
                    "",
                    f"Pagination: Page {start_page + 1} of {total_pages} (total: {total_count} entries)",
                ])
        
        result_lines.append(f"\nAPI Endpoint: {format_params.get('api_href', 'Not available')}")
        
        return "\n".join(result_lines)
        
    except Exception as e:
        return f"Error: Exception occurred while retrieving {mode} alerts - {str(e)}"

@mcp.tool()
@log_tool
async def get_current_alerts(
    cluster_name: Optional[str] = None,
    service_name: Optional[str] = None,
    host_name: Optional[str] = None,
    state_filter: Optional[str] = None,
    definition_name: Optional[str] = None,
    maintenance_state: Optional[str] = None,
    format: str = "detailed"
) -> str:
    """
    Retrieve current alerts from Ambari cluster.
    
    DEPRECATED: This function is deprecated in favor of get_alerts_history with mode="current".
    This wrapper is maintained for backward compatibility.
    """
    return await get_alerts_history(
        mode="current",
        cluster_name=cluster_name,
        service_name=service_name,
        host_name=host_name,
        state_filter=state_filter,
        definition_name=definition_name,
        maintenance_state=maintenance_state,
        format=format
    )


async def get_alert_history(
    cluster_name: Optional[str] = None,
    service_name: Optional[str] = None,
    host_name: Optional[str] = None,
    state_filter: Optional[str] = None,
    definition_name: Optional[str] = None,
    from_timestamp: Optional[int] = None,
    to_timestamp: Optional[int] = None,
    limit: Optional[int] = None,
    page_size: int = 100,
    start_page: int = 0,
    format: str = "detailed"
) -> str:
    """
    Retrieve alert history from Ambari cluster.
    
    DEPRECATED: This function is deprecated in favor of get_alerts_history with mode="history".
    This wrapper is maintained for backward compatibility.
    """
    return await get_alerts_history(
        mode="history",
        cluster_name=cluster_name,
        service_name=service_name,
        host_name=host_name,
        state_filter=state_filter,
        definition_name=definition_name,
        from_timestamp=from_timestamp,
        to_timestamp=to_timestamp,
        limit=limit,
        page_size=page_size,
        start_page=start_page,
        format=format
    )


# Ambari Metrics (AMS) tools

@mcp.tool(title="List Ambari Metrics Metadata")
@log_tool
async def list_ambari_metrics_metadata(
    app_id: Optional[str] = None,
    metric_name_filter: Optional[str] = None,
    host_filter: Optional[str] = None,
    search: Optional[str] = None,
    limit: int = 50,
    include_dimensions: bool = False,
) -> str:
    """Retrieve metric metadata from Ambari Metrics service with optional filters."""
    catalog, lookup = await ensure_metric_catalog()
    canonical_app = canonicalize_app_id(app_id, lookup)
    resolved_app = None
    if canonical_app:
        resolved_app = lookup.get(canonical_app.lower(), canonical_app)

    params: Dict[str, str] = {}
    if resolved_app:
        params["appId"] = resolved_app
    elif app_id:
        params["appId"] = app_id
    if host_filter:
        params["hostname"] = host_filter

    # Use server-side metric name filtering when a single token is supplied
    if metric_name_filter and ',' not in metric_name_filter:
        params["metricName"] = metric_name_filter.strip()

    response = await make_ambari_metrics_request("/metrics/metadata", params=params or None)
    if response is None or isinstance(response, dict) and response.get("error"):
        error_msg = response.get("error", "Unable to reach Ambari Metrics API") if isinstance(response, dict) else "No response"
        return f"Error: Failed to retrieve metrics metadata - {error_msg}"

    raw_section = None
    if isinstance(response, dict):
        raw_section = response.get("metrics") or response.get("items") or response.get("Metrics")
    if raw_section is None:
        raw_section = response

    items: List[Dict] = []
    if isinstance(raw_section, dict):
        for metric_name, meta in raw_section.items():
            if isinstance(meta, dict):
                entry = dict(meta)
                entry.setdefault("metricname", metric_name)
                items.append(entry)
            elif isinstance(meta, list):
                for element in meta:
                    if isinstance(element, dict):
                        entry = dict(element)
                        entry.setdefault("metricname", metric_name)
                        items.append(entry)
                    else:
                        entry = {
                            "metricname": str(element),
                            "appid": metric_name,
                            "appId": metric_name,
                        }
                        items.append(entry)
            else:
                entry = {
                    "metricname": str(metric_name),
                    "appid": metric_name,
                    "appId": metric_name,
                    "value": meta,
                }
                items.append(entry)
    elif isinstance(raw_section, list):
        items = [entry for entry in raw_section if isinstance(entry, dict)]
    else:
        return "No metric metadata available from Ambari Metrics service."

    filters_applied: List[str] = []

    if metric_name_filter:
        tokens = [token.strip().lower() for token in metric_name_filter.split(',') if token.strip()]
        if tokens:
            def metric_matches(entry: Dict) -> bool:
                name = str(entry.get("metricname") or entry.get("metricName") or "").lower()
                return any(token in name for token in tokens)

            filtered = [entry for entry in items if metric_matches(entry)]
            if filtered:
                items = filtered
            filters_applied.append(f"metric~{metric_name_filter}")

    if host_filter:
        tokens = [token.strip().lower() for token in host_filter.split(',') if token.strip()]

        def host_matches(entry: Dict) -> bool:
            candidates = [
                str(entry.get("hostname", "")),
                str(entry.get("host", "")),
                str(entry.get("instanceId", "")),
                str(entry.get("instanceid", "")),
            ]
            haystack = " ".join(candidates).lower()
            return any(token in haystack for token in tokens)

        filtered = [entry for entry in items if host_matches(entry)]
        if filtered:
            items = filtered
        filters_applied.append(f"host~{host_filter}")

    search_lower = (search or "").strip().lower()
    if search_lower:
        def search_matches(entry: Dict) -> bool:
            haystack_parts = [
                str(entry.get("metricname") or entry.get("metricName") or ""),
                str(entry.get("appid") or entry.get("appId") or entry.get("application") or ""),
                str(entry.get("description") or entry.get("desc") or ""),
                str(entry.get("units") or entry.get("unit") or ""),
                str(entry.get("type") or entry.get("metricType") or ""),
            ]
            haystack = " ".join(part.lower() for part in haystack_parts if part)
            return search_lower in haystack

        filtered = [entry for entry in items if search_matches(entry)]
        if filtered:
            items = filtered
        filters_applied.append(f"search~{search_lower}")

    if not items:
        fallback_app = resolved_app or canonical_app
        if fallback_app:
            curated_metrics = catalog.get(fallback_app) or await get_metrics_for_app(fallback_app)
            limited_metrics = curated_metrics[:max(1, limit)] if limit > 0 else curated_metrics

            lines = [
                "Ambari Metrics Catalog (metadata fallback)",
                f"appId={fallback_app}",
                "",
                "Exact metric names available for this appId:",
            ]

            if limited_metrics:
                for metric in limited_metrics:
                    lines.append(f"  - {metric}")
                if limit > 0 and len(curated_metrics) > len(limited_metrics):
                    lines.append(
                        f"    … {len(curated_metrics) - len(limited_metrics)} additional metrics (increase limit)"
                    )
            else:
                lines.append("  <no cached metrics recorded>")

            component_name = HOST_FILTER_REQUIRED_COMPONENTS.get(fallback_app.lower())
            if component_name:
                component_hosts = await get_component_hostnames(component_name)
                lines.append("")
                if component_hosts:
                    preview_count = min(len(component_hosts), 10)
                    preview_hosts = ", ".join(component_hosts[:preview_count])
                    if len(component_hosts) > preview_count:
                        preview_hosts += f", ... (+{len(component_hosts) - preview_count} more)"
                    lines.append(f"{component_name} hosts ({len(component_hosts)}): {preview_hosts}")
                else:
                    lines.append(f"{component_name} hosts: none discovered via Ambari API.")

            lines.append("")
            lines.append(
                'Next: call query_ambari_metrics(metric_names="<exact_name>", app_id="%s", ...)' % fallback_app
            )
            lines.append("Hostname is optional; omit it for cluster-wide data or supply explicit hosts to narrow the scope.")

            if limit <= 0:
                lines.append("Note: limit<=0 → entire catalog was shown.")

            if filters_applied:
                lines.append("")
                lines.append(f"Applied filters: {', '.join(filters_applied)}")

            return "\n".join(lines)

        return "No metric metadata matched the provided filters."

    limited_items = items[:max(1, limit)] if limit > 0 else items

    lines: List[str] = [
        "Ambari Metrics Metadata",
        f"Endpoint: {AMBARI_METRICS_BASE_URL}/metrics/metadata",
    ]
    if filters_applied:
        lines.append(f"Filters: {', '.join(filters_applied)}")
    lines.append(f"Returned: {len(limited_items)} metric definitions (total matches: {len(items)})")
    lines.append("")

    for idx, entry in enumerate(limited_items, 1):
        metric_name = entry.get("metricname") or entry.get("metricName") or entry.get("name", "<unknown>")
        app = entry.get("appid") or entry.get("appId") or entry.get("application", "-")
        units = entry.get("units") or entry.get("unit", "-")
        metric_type = entry.get("type") or entry.get("metricType", "-")
        description = entry.get("description") or entry.get("desc") or ""
        scope = entry.get("hostname") or entry.get("instanceId") or entry.get("instanceid") or entry.get("group") or "cluster"

        lines.append(f"[{idx}] {metric_name}")
        lines.append(f"     appId={app} | type={metric_type} | units={units} | scope={scope}")
        if description:
            lines.append(f"     {description}")

        if include_dimensions:
            dimensions = entry.get("tags") or entry.get("metadata") or entry.get("dimensions") or {}
            if isinstance(dimensions, dict) and dimensions:
                dim_parts = [f"{key}={val}" for key, val in dimensions.items()]
                lines.append(f"     dimensions: {', '.join(dim_parts)}")
            supported_agg = (
                entry.get("temporalAggregator")
                or entry.get("temporalAggregations")
                or entry.get("supportedAggregations")
            )
            if supported_agg:
                lines.append(f"     aggregators: {supported_agg}")

        lines.append("")

    if limit > 0 and len(items) > len(limited_items):
        lines.append(f"… {len(items) - len(limited_items)} more metrics not shown (increase limit to view).")

    return "\n".join(lines)


@mcp.tool(title="List Common Metrics Catalog")
@log_tool
async def list_common_metrics_catalog(
    app_id: Optional[str] = None,
    search: Optional[str] = None,
    limit: int = 40,
    min_score: int = 6,
    include_description: bool = True,
) -> str:
    """List supported metrics per appId (exact names only)."""

    _ = (min_score, include_description)
    limit = max(1, limit)
    catalog, lookup = await ensure_metric_catalog()

    def resolve_targets(raw_values: List[str]) -> List[str]:
        ordered: List[str] = []
        seen_local: Set[str] = set()
        for value in raw_values:
            resolved = canonicalize_app_id(value, lookup)
            if not resolved:
                continue
            target = lookup.get(resolved.lower(), resolved)
            lowered = target.lower()
            if lowered in seen_local:
                continue
            seen_local.add(lowered)
            ordered.append(target)
        return ordered

    target_app_ids: List[str]
    if isinstance(app_id, str) and app_id.strip():
        app_token = app_id.strip()
        if app_token.lower() in {"all", "*"}:
            target_app_ids = sorted(catalog.keys())
        else:
            raw_targets = [item.strip() for item in app_token.split(',') if item.strip()]
            target_app_ids = resolve_targets(raw_targets or [app_token])
            if not target_app_ids:
                target_app_ids = sorted(catalog.keys())
    else:
        target_app_ids = sorted(catalog.keys())

    search_lower = (search or "").strip().lower()

    lines = [
        "Ambari Metrics Catalog (exact names)",
        f"Apps considered: {', '.join(target_app_ids)}",
        f"Search: {search or '—'}",
        "",
        "Exact metric names per appId:",
    ]

    matched = 0
    for app_name in target_app_ids:
        metrics = await get_metrics_for_app(app_name)
        catalog[app_name] = metrics
        if not metrics:
            continue
        filtered = [metric for metric in metrics if not search_lower or search_lower in metric.lower()]
        if not filtered:
            continue
        matched += len(filtered)
        display_count = min(limit, len(filtered)) if limit > 0 else len(filtered)
        lines.append("")
        lines.append(f"[{app_name}] (showing {display_count} of {len(filtered)} metric(s))")
        for metric in filtered[:display_count]:
            lines.append(f"  - {metric}")
        if display_count < len(filtered):
            lines.append(f"    … {len(filtered) - display_count} additional metrics (increase limit)")

    if matched == 0:
        lines.append("")
        lines.append("No metrics matched the given filters.")
    else:
        lines.append("")
        lines.append('Tip: Use query_ambari_metrics(metric_names="<metric>", app_id="<app>") to fetch data.')

    return "\n".join(lines)


@mcp.resource("ambari-metrics://catalog/{selector}{?refresh}")
async def ambari_metrics_catalog_resource(
    selector: str = "all",
    refresh: Optional[str] = None,
) -> str:
    """Return AMS metric metadata as compact JSON.

    Supported selectors:
    - `all` (default): full appId → metrics map.
    - `apps`: list available appIds only.
    - `<appId>`: metrics for the given app (synonyms allowed).
    - `app/<appId>`: same as above, explicit prefix for clarity.
    """

    refresh_requested = False
    if isinstance(refresh, str):
        refresh_requested = refresh.strip().lower() in {"1", "true", "yes", "refresh", "force"}

    use_cache = not refresh_requested
    catalog, lookup = await ensure_metric_catalog(use_cache=use_cache)

    selector_normalized = (selector or "all").strip()
    selector_lower = selector_normalized.lower()

    async def metrics_for(app_identifier: str) -> Dict[str, List[str]]:
        metrics = await get_metrics_for_app(app_identifier)
        resolved_name = canonicalize_app_id(app_identifier, lookup)
        if resolved_name:
            resolved_key = lookup.get(resolved_name.lower(), resolved_name)
        else:
            lower = app_identifier.lower()
            resolved_key = lookup.get(lower, next((app for app in catalog if app.lower() == lower), app_identifier))
        return {resolved_key: metrics}

    payload: Any
    if selector_lower in {"all", "*"}:
        non_empty = {app: metrics for app, metrics in sorted(catalog.items()) if metrics}
        payload = non_empty or {app: metrics for app, metrics in sorted(catalog.items())}
    elif selector_lower == "apps":
        payload = sorted(catalog.keys())
    elif selector_lower.startswith("app/") and len(selector_lower) > 4:
        target = selector_normalized.split("/", 1)[1]
        payload = await metrics_for(target)
    else:
        payload = await metrics_for(selector_normalized)

    return json.dumps(payload, separators=(",", ":"))


@mcp.tool(title="List Ambari Metric Apps")
@log_tool
async def list_ambari_metric_apps(
    refresh: bool = False,
    include_counts: bool = True,
    limit: int = 200,
) -> str:
    """Return discovered AMS appIds, optionally with metric counts."""

    catalog, _ = await ensure_metric_catalog(use_cache=not refresh)
    if not catalog:
        return "No Ambari Metrics appIds discovered."

    app_items = sorted(catalog.items(), key=lambda item: item[0])
    limit = max(1, limit)

    lines = [
        "Ambari Metrics AppIds",
        f"Total discovered: {len(app_items)}",
        f"Refresh requested: {'yes' if refresh else 'no'}",
        "",
    ]

    display_items = app_items if limit <= 0 else app_items[:limit]
    for app_name, metrics in display_items:
        if include_counts:
            lines.append(f"- {app_name} ({len(metrics)} metric(s))")
        else:
            lines.append(f"- {app_name}")

    if limit > 0 and len(app_items) > limit:
        lines.append("")
        lines.append(f"… {len(app_items) - limit} additional appIds not shown (increase limit).")

    lines.append("")
    lines.append("Tip: Use ambari-metrics://catalog/<appId> or list_common_metrics_catalog(app_id=…) to inspect metric names.")

    return "\n".join(lines)


@mcp.tool(title="HDFS DFSAdmin Report")
@log_tool
async def hdfs_dfadmin_report(
    cluster_name: Optional[str] = None,
    lookback_minutes: int = 10,
) -> str:
    """Produce a DFSAdmin-style capacity and DataNode report using Ambari metrics."""

    target_cluster = cluster_name or AMBARI_CLUSTER_NAME
    lookback_ms = max(1, lookback_minutes) * 60 * 1000

    # Helper functions -----------------------------------------------------
    def format_bytes(value: Optional[float]) -> str:
        if value is None:
            return "N/A"
        units = ["B", "KB", "MB", "GB", "TB", "PB"]
        size = float(value)
        idx = 0
        while size >= 1024 and idx < len(units) - 1:
            size /= 1024.0
            idx += 1
        return f"{size:.2f} {units[idx]}"

    def safe_percent(numerator: Optional[float], denominator: Optional[float]) -> str:
        if numerator is None or denominator in (None, 0):
            return "N/A"
        try:
            pct = (float(numerator) / float(denominator)) * 100.0
            return f"{pct:.2f}%"
        except ZeroDivisionError:
            return "N/A"

    def to_float(value: Any) -> Optional[float]:
        if value is None:
            return None
        try:
            return float(value)
        except (TypeError, ValueError):
            return None

    # Cluster-level metrics via AMS ---------------------------------------
    capacity_metrics = {
        "configured_capacity": "dfs.FSNamesystem.CapacityTotal",
        "dfs_used": "dfs.FSNamesystem.CapacityUsed",
        "dfs_remaining": "dfs.FSNamesystem.CapacityRemaining",
        "non_dfs_used": "dfs.FSNamesystem.CapacityUsedNonDFS",
        "under_replicated": "dfs.FSNamesystem.UnderReplicatedBlocks",
        "corrupt_replicas": "dfs.FSNamesystem.CorruptBlocks",
        "missing_blocks": "dfs.FSNamesystem.MissingBlocks",
        "missing_blocks_repl_one": "dfs.FSNamesystem.MissingReplOneBlocks",
        "lowest_priority_redundancy": "dfs.FSNamesystem.LowRedundancyBlocks",
        "pending_deletion": "dfs.namenode.PendingDeleteBlocksCount",
        "ec_low_redundancy": "dfs.FSNamesystem.LowRedundancyECBlockGroups",
        "ec_corrupt": "dfs.FSNamesystem.CorruptECBlockGroups",
        "ec_missing": "dfs.FSNamesystem.MissingECBlockGroups",
        "ec_pending_deletion": "dfs.FSNamesystem.PendingDeletionECBlocks",
    }

    cluster_values: Dict[str, Optional[float]] = {}
    for key, metric in capacity_metrics.items():
        value = await fetch_latest_metric_value(metric, app_id="namenode", duration_ms=lookback_ms)
        cluster_values[key] = value

    configured = to_float(cluster_values.get("configured_capacity"))
    dfs_used = to_float(cluster_values.get("dfs_used")) or 0.0
    dfs_remaining = to_float(cluster_values.get("dfs_remaining")) or 0.0
    present_capacity = dfs_used + dfs_remaining

    lines: List[str] = []
    lines.append(f"HDFS DFSAdmin Report (cluster: {target_cluster})")
    lines.append("=" * 72)
    lines.append(f"Configured Capacity: {format_bytes(configured)}")
    lines.append(f"Present Capacity: {format_bytes(present_capacity)}")
    lines.append(f"DFS Remaining: {format_bytes(dfs_remaining)}")
    lines.append(f"DFS Used: {format_bytes(dfs_used)}")
    lines.append(f"DFS Used%: {safe_percent(dfs_used, present_capacity)}")

    lines.append("Replicated Blocks:")
    lines.append(f"    Under replicated blocks: {int(cluster_values.get('under_replicated') or 0)}")
    lines.append(f"    Blocks with corrupt replicas: {int(cluster_values.get('corrupt_replicas') or 0)}")
    lines.append(f"    Missing blocks: {int(cluster_values.get('missing_blocks') or 0)}")
    lines.append(f"    Missing blocks (replication factor 1): {int(cluster_values.get('missing_blocks_repl_one') or 0)}")
    lines.append(f"    Low redundancy blocks with highest priority to recover: {int(cluster_values.get('lowest_priority_redundancy') or 0)}")
    lines.append(f"    Pending deletion blocks: {int(cluster_values.get('pending_deletion') or 0)}")

    lines.append("Erasure Coded Block Groups:")
    lines.append(f"    Low redundancy block groups: {int(cluster_values.get('ec_low_redundancy') or 0)}")
    lines.append(f"    Block groups with corrupt internal blocks: {int(cluster_values.get('ec_corrupt') or 0)}")
    lines.append(f"    Missing block groups: {int(cluster_values.get('ec_missing') or 0)}")
    lines.append(f"    Pending deletion blocks: {int(cluster_values.get('ec_pending_deletion') or 0)}")

    # DataNode inventory ---------------------------------------------------
    lines.append("")
    lines.append("-" * 72)

    hosts_resp = await make_ambari_request(
        f"/clusters/{target_cluster}/hosts?fields=Hosts/host_name,Hosts/public_host_name,Hosts/ip,host_components/HostRoles/component_name",
        method="GET",
    )

    datanode_hosts: List[Dict[str, Any]] = []
    if hosts_resp and not hosts_resp.get("error"):
        for item in hosts_resp.get("items", []):
            host_components = item.get("host_components", [])
            component_names = {comp.get("HostRoles", {}).get("component_name") for comp in host_components}
            if "DATANODE" in component_names:
                datanode_hosts.append(item)

    if datanode_hosts:
        lines.append(f"Live datanodes ({len(datanode_hosts)}):")
        for host_item in datanode_hosts:
            host_info = host_item.get("Hosts", {})
            host_name = host_info.get("host_name") or host_info.get("public_host_name") or host_info.get("ip") or "<unknown>"
            public_name = host_info.get("public_host_name") or host_name
            ip_addr = host_info.get("ip")
            ams_host_filter = public_name or host_name or ip_addr

            detail_resp = await make_ambari_request(
                f"/clusters/{target_cluster}/hosts/{host_name}?fields=Hosts/ip,Hosts/public_host_name,Hosts/last_heartbeat_time,metrics/cpu,metrics/memory,metrics/dfs,metrics/disk,metrics/network",
                method="GET",
            )

            if not detail_resp or detail_resp.get("error"):
                detail_resp = host_item

            host_metrics = detail_resp.get("metrics", {}) if detail_resp else {}
            dfs_metrics = host_metrics.get("dfs", {}) if isinstance(host_metrics, dict) else {}

            capacity_total = to_float(dfs_metrics.get("FSCapacityTotalBytes") or dfs_metrics.get("FSCapacityTotal"))
            dfs_used_host = to_float(dfs_metrics.get("FSUsedBytes") or dfs_metrics.get("FSUsed"))
            dfs_remaining_host = to_float(dfs_metrics.get("FSRemainingBytes") or dfs_metrics.get("FSRemaining"))
            non_dfs_used = to_float(dfs_metrics.get("NonDFSUsedBytes") or dfs_metrics.get("NonDFSUsed"))

            if capacity_total is None:
                capacity_total = await fetch_latest_metric_value(
                    "FSDatasetState.org.apache.hadoop.hdfs.server.datanode.fsdataset.impl.FsDatasetImpl.Capacity",
                    app_id="datanode",
                    hostnames=ams_host_filter,
                    duration_ms=lookback_ms,
                )
            if dfs_used_host is None:
                dfs_used_host = await fetch_latest_metric_value(
                    "FSDatasetState.org.apache.hadoop.hdfs.server.datanode.fsdataset.impl.FsDatasetImpl.DfsUsed",
                    app_id="datanode",
                    hostnames=ams_host_filter,
                    duration_ms=lookback_ms,
                )
            if dfs_remaining_host is None:
                dfs_remaining_host = await fetch_latest_metric_value(
                    "FSDatasetState.org.apache.hadoop.hdfs.server.datanode.fsdataset.impl.FsDatasetImpl.Remaining",
                    app_id="datanode",
                    hostnames=ams_host_filter,
                    duration_ms=lookback_ms,
                )

            if non_dfs_used is None and all(v is not None for v in (capacity_total, dfs_used_host, dfs_remaining_host)):
                non_dfs_used = max(capacity_total - dfs_used_host - dfs_remaining_host, 0)
            if non_dfs_used is None:
                disk_metrics = host_metrics.get("disk", {}) if isinstance(host_metrics, dict) else {}
                disk_total = to_float(disk_metrics.get("disk_total"))
                disk_free = to_float(disk_metrics.get("disk_free"))
                if disk_total is not None and disk_free is not None and dfs_used_host is not None:
                    non_dfs_used = max(disk_total - disk_free - dfs_used_host, 0)

            dfs_used_pct = safe_percent(dfs_used_host, capacity_total)
            dfs_remaining_pct = safe_percent(dfs_remaining_host, capacity_total)

            lines.append("")
            if host_name and host_name != ip_addr:
                lines.append(f"Name: {host_name}")
            lines.append(f"Hostname: {public_name}")
            if ip_addr:
                lines.append(f"IP Address: {ip_addr}")
            if ip_addr:
                lines.append(f"IP Address: {ip_addr}")
            lines.append("Decommission Status : Normal")
            lines.append(f"Configured Capacity: {format_bytes(capacity_total)}")
            lines.append(f"DFS Used: {format_bytes(dfs_used_host)}")
            lines.append(f"Non DFS Used: {format_bytes(non_dfs_used)}")
            lines.append(f"DFS Remaining: {format_bytes(dfs_remaining_host)}")
            lines.append(f"DFS Used%: {dfs_used_pct}")
            lines.append(f"DFS Remaining%: {dfs_remaining_pct}")
            lines.append("Configured Cache Capacity: 0 (0 B)")
            lines.append("Cache Used: 0 (0 B)")
            lines.append("Cache Remaining: 0 (0 B)")
            lines.append("Cache Used%: 0.00%")
            lines.append("Cache Remaining%: 0.00%")

            xceivers = await fetch_latest_metric_value(
                "dfs.datanode.DataNodeActiveXceiversCount",
                app_id="datanode",
                hostnames=ams_host_filter,
                duration_ms=lookback_ms,
            )
            if xceivers is not None:
                lines.append(f"Active Xceivers: {int(xceivers)}")

            block_metric_map = [
                ("Blocks read", "dfs.datanode.BlocksRead"),
                ("Blocks written", "dfs.datanode.BlocksWritten"),
                ("Blocks replicated", "dfs.datanode.BlocksReplicated"),
                ("Blocks removed", "dfs.datanode.BlocksRemoved"),
                ("Blocks cached", "dfs.datanode.BlocksCached"),
                ("Blocks uncached", "dfs.datanode.BlocksUncached"),
                ("Blocks in pending IBR", "dfs.datanode.BlocksInPendingIBR"),
                ("Blocks receiving (pending IBR)", "dfs.datanode.BlocksReceivingInPendingIBR"),
                ("Blocks received (pending IBR)", "dfs.datanode.BlocksReceivedInPendingIBR"),
                ("Blocks deleted (pending IBR)", "dfs.datanode.BlocksDeletedInPendingIBR"),
                ("Blocks verified", "dfs.datanode.BlocksVerified"),
                ("Block verification failures", "dfs.datanode.BlockVerificationFailures"),
                ("Block checksum avg time", "dfs.datanode.BlockChecksumOpAvgTime"),
                ("Block checksum ops", "dfs.datanode.BlockChecksumOpNumOps"),
                ("Block reports avg time", "dfs.datanode.BlockReportsAvgTime"),
                ("Block reports ops", "dfs.datanode.BlockReportsNumOps"),
                ("Copy block avg time", "dfs.datanode.CopyBlockOpAvgTime"),
                ("Copy block ops", "dfs.datanode.CopyBlockOpNumOps"),
                ("Block recovery worker count", "dfs.datanode.DataNodeBlockRecoveryWorkerCount"),
                ("Incremental block reports avg time", "dfs.datanode.IncrementalBlockReportsAvgTime"),
                ("Incremental block reports ops", "dfs.datanode.IncrementalBlockReportsNumOps"),
                ("RamDisk blocks deleted before lazy persisted", "dfs.datanode.RamDiskBlocksDeletedBeforeLazyPersisted"),
                ("RamDisk blocks evicted", "dfs.datanode.RamDiskBlocksEvicted"),
                ("RamDisk blocks evicted without read", "dfs.datanode.RamDiskBlocksEvictedWithoutRead"),
                ("RamDisk blocks eviction window avg time", "dfs.datanode.RamDiskBlocksEvictionWindowMsAvgTime"),
                ("RamDisk blocks eviction window ops", "dfs.datanode.RamDiskBlocksEvictionWindowMsNumOps"),
                ("RamDisk blocks lazy persisted", "dfs.datanode.RamDiskBlocksLazyPersisted"),
                ("RamDisk blocks lazy persist window avg time", "dfs.datanode.RamDiskBlocksLazyPersistWindowMsAvgTime"),
                ("RamDisk blocks lazy persist window ops", "dfs.datanode.RamDiskBlocksLazyPersistWindowMsNumOps"),
                ("RamDisk blocks read hits", "dfs.datanode.RamDiskBlocksReadHits"),
                ("RamDisk blocks write", "dfs.datanode.RamDiskBlocksWrite"),
                ("RamDisk blocks write fallback", "dfs.datanode.RamDiskBlocksWriteFallback"),
                ("Read block avg time", "dfs.datanode.ReadBlockOpAvgTime"),
                ("Read block ops", "dfs.datanode.ReadBlockOpNumOps"),
                ("Replace block avg time", "dfs.datanode.ReplaceBlockOpAvgTime"),
                ("Replace block ops", "dfs.datanode.ReplaceBlockOpNumOps"),
                ("Send data packet blocked avg time", "dfs.datanode.SendDataPacketBlockedOnNetworkNanosAvgTime"),
                ("Send data packet blocked ops", "dfs.datanode.SendDataPacketBlockedOnNetworkNanosNumOps"),
                ("Write block avg time", "dfs.datanode.WriteBlockOpAvgTime"),
                ("Write block ops", "dfs.datanode.WriteBlockOpNumOps"),
                ("Blocks get local path info", "dfs.datanode.BlocksGetLocalPathInfo"),
            ]

            block_values = []
            for label, metric_name in block_metric_map:
                metric_value = await fetch_latest_metric_value(
                    metric_name,
                    app_id="datanode",
                    hostnames=ams_host_filter,
                    duration_ms=lookback_ms,
                )
                if metric_value is not None:
                    try:
                        block_values.append((label, int(metric_value)))
                    except (TypeError, ValueError):
                        block_values.append((label, float(metric_value)))

            for label, value in block_values:
                value_str = f"{value:.2f}" if isinstance(value, float) and not float(value).is_integer() else f"{int(value)}"
                lines.append(f"{label}: {value_str}")
    else:
        lines.append("No DataNodes found via Ambari API.")

    return "\n".join(lines)


@mcp.tool(title="Query Ambari Metrics")
@log_tool
async def query_ambari_metrics(
    metric_names: str,
    app_id: Optional[str] = None,
    hostnames: Optional[str] = None,
    duration: Optional[str] = "1h",
    start_time: Optional[str] = None,
    end_time: Optional[str] = None,
    precision: Optional[str] = None,
    temporal_aggregator: Optional[str] = None,
    temporal_granularity: Optional[str] = None,
    group_by_host: bool = False,
    include_points: bool = False,
    max_points: int = 120,
) -> str:
    """Fetch time-series metrics (exact metric names only) from Ambari Metrics."""

    start_ms, end_ms, window_desc = resolve_metrics_time_range(duration, start_time, end_time)
    if start_ms is None or end_ms is None:
        return "Error: Unable to resolve a valid time window for the request."

    raw_metric_arg = str(metric_names or "").strip()
    requested_metric_list = [name.strip() for name in raw_metric_arg.split(',') if name.strip()]
    user_supplied_metric_names = bool(requested_metric_list)

    provided_app_id = app_id.strip() if isinstance(app_id, str) and app_id.strip() else None
    catalog, lookup = await ensure_metric_catalog()
    available_apps = sorted(catalog.keys())

    if not provided_app_id:
        lines = [
            "Ambari Metrics Query",
            f"Endpoint: {AMBARI_METRICS_BASE_URL}/metrics",
            f"Window: {window_desc}",
            f"Metric names: {metric_names or '<pending>'}",
            "Requested appId: not provided",
            "Resolved appId: <none>",
            "",
            "appId parameter is required. Select one explicitly before retrying.",
            "Available appIds:",
        ]
        for candidate in available_apps:
            lines.append(f"  - {candidate}")
        return "\n".join(lines)

    canonical_app_id = canonicalize_app_id(provided_app_id, lookup)
    resolved_app_id = None
    if canonical_app_id:
        resolved_app_id = lookup.get(canonical_app_id.lower(), canonical_app_id)

    if not resolved_app_id or resolved_app_id not in catalog:
        lines = [
            "Ambari Metrics Query",
            f"Endpoint: {AMBARI_METRICS_BASE_URL}/metrics",
            f"Window: {window_desc}",
            f"Metric names: {metric_names or '<pending>'}",
            f"Requested appId: {provided_app_id}",
            "Resolved appId: <unsupported>",
            "",
            "Unsupported appId. Choose one of the supported appIds explicitly and retry.",
            "Available appIds:",
        ]
        for candidate in available_apps:
            lines.append(f"  - {candidate}")
        return "\n".join(lines)

    base_params: Dict[str, object] = {
        "startTime": start_ms,
        "endTime": end_ms,
        "appId": resolved_app_id,
    }
    available_metrics = await get_metrics_for_app(resolved_app_id)
    catalog[resolved_app_id] = available_metrics

    hostnames_display: Optional[str] = None
    if hostnames:
        sanitized_hosts = ",".join(host.strip() for host in hostnames.split(',') if host.strip())
        if sanitized_hosts:
            base_params["hostname"] = sanitized_hosts
            hostnames_display = sanitized_hosts

    component_name = HOST_FILTER_REQUIRED_COMPONENTS.get(resolved_app_id.lower())
    component_hosts: Optional[List[str]] = None

    async def ensure_component_hosts() -> List[str]:
        nonlocal component_hosts
        if component_name and component_hosts is None:
            component_hosts = await get_component_hostnames(component_name)
        return component_hosts or []

    def build_base_output_lines(
        metric_display: str,
        resolved_label_override: Optional[str] = None,
    ) -> List[str]:
        base_lines = [
            "Ambari Metrics Query",
            f"Endpoint: {AMBARI_METRICS_BASE_URL}/metrics",
            f"Window: {window_desc}",
            f"Metric names: {metric_display}",
        ]
        base_lines.append(f"Requested appId: {provided_app_id}")
        resolved_label = (
            resolved_label_override
            if resolved_label_override is not None
            else resolved_app_id
        )
        base_lines.append(f"Resolved appId: {resolved_label}")
        base_lines.append(f"Hosts: {hostnames_display or 'cluster / default scope'}")
        if precision:
            base_lines.append(f"Precision: {precision}")
        if temporal_aggregator:
            base_lines.append(f"Temporal aggregator: {temporal_aggregator}")
        if temporal_granularity:
            base_lines.append(f"Temporal granularity: {temporal_granularity}")
        return base_lines

    if not user_supplied_metric_names:
        lines = build_base_output_lines("<pending>", resolved_app_id)
        lines.append("")
        lines.append("Explicit metric_names parameter is required for this app (exact matches only).")
        lines.append("Available metrics:")
        for metric in available_metrics:
            lines.append(f"  - {metric}")
        if component_name:
            component_hosts = await ensure_component_hosts()
            lines.append("")
            if component_hosts:
                preview_count = min(len(component_hosts), 10)
                preview_hosts = ", ".join(component_hosts[:preview_count])
                if len(component_hosts) > preview_count:
                    preview_hosts += f", ... (+{len(component_hosts) - preview_count} more)"
                lines.append(f"{component_name} hosts ({len(component_hosts)}): {preview_hosts}")
            else:
                lines.append(f"{component_name} hosts: none discovered via Ambari API.")
        host_tip = ' hostnames="<host1,host2>"' if component_name else ""
        lines.append("")
        lines.append(f'Tip: rerun with metric_names="metric1,metric2"{host_tip}')
        return "\n".join(lines)

    deduped_metrics: List[str] = []
    seen_metrics: Set[str] = set()
    for metric in requested_metric_list:
        if metric not in seen_metrics:
            seen_metrics.add(metric)
            deduped_metrics.append(metric)

    requested_metric_list = deduped_metrics
    metric_names_joined = ",".join(deduped_metrics)
    base_params["metricNames"] = metric_names_joined
    resolved_metric_display = metric_names_joined or "<pending>"

    if precision:
        base_params["precision"] = precision
    if temporal_aggregator:
        base_params["temporalAggregator"] = temporal_aggregator
    if temporal_granularity:
        base_params["temporalGranularity"] = temporal_granularity
    if group_by_host:
        base_params["grouped"] = "true"

    def extract_metric_entries(response_obj) -> (List[Dict], Optional[str]):
        """Extract metric entry list and optional error message from AMS response."""
        if response_obj is None:
            return [], "No response"

        if isinstance(response_obj, dict):
            if response_obj.get("error"):
                return [], str(response_obj["error"])
            if response_obj.get("errorMessage"):
                return [], str(response_obj["errorMessage"])
            if response_obj.get("message") and not response_obj.get("metrics"):
                return [], str(response_obj["message"])

            metrics_section = None
            for key in (
                "metrics",
                "Metrics",
                "timelineMetrics",
                "TimelineMetrics",
                "items",
                "MetricsCollection",
            ):
                if key in response_obj:
                    metrics_section = response_obj[key]
                    break
        elif isinstance(response_obj, list):
            metrics_section = response_obj
        else:
            metrics_section = None

        if metrics_section is None:
            keys_preview = []
            if isinstance(response_obj, dict):
                keys_preview = list(response_obj.keys())[:8]
            descriptor = f"keys={keys_preview}" if keys_preview else f"type={type(response_obj).__name__}"
            return [], f"Unexpected metrics response format ({descriptor})"

        entries: List[Dict] = []
        if isinstance(metrics_section, dict):
            for metric_name, meta in metrics_section.items():
                if not isinstance(meta, dict):
                    continue
                entry = dict(meta)
                entry.setdefault("metricname", metric_name)
                entries.append(entry)
        elif isinstance(metrics_section, list):
            entries = [entry for entry in metrics_section if isinstance(entry, dict)]

        return entries, None

    metrics_list: List[Dict] = []
    attempt_records: List[Dict[str, Optional[str]]] = []
    last_error: Optional[str] = None

    response = await make_ambari_metrics_request("/metrics", params=base_params)
    metric_entries, error_text = extract_metric_entries(response)
    attempt_records.append(
        {
            "appId": resolved_app_id,
            "count": str(len(metric_entries)),
            "error": error_text,
        }
    )
    if metric_entries:
        metrics_list = metric_entries
    else:
        last_error = error_text

    lines: List[str] = build_base_output_lines(resolved_metric_display, resolved_app_id)
    lines.append("")

    def format_value(val: Optional[float]) -> str:
        if val is None:
            return "-"
        if val == 0:
            return "0"
        if abs(val) >= 1000 or abs(val) < 0.01:
            return f"{val:.4g}"
        return f"{val:.2f}"

    def append_metric_summary(
        entry: Dict[str, Any],
        idx_label: Optional[int],
        indent: str = "",
        show_host: bool = True,
        lines_out: Optional[List[str]] = None,
    ) -> None:
        target_lines = lines_out if lines_out is not None else lines

        metric_name = entry.get("metricname") or entry.get("metricName") or entry.get("name", "<unknown>")
        app_label = entry.get("appid") or entry.get("appId") or provided_app_id or "-"
        host_label = entry.get("hostname") or entry.get("host") or "all"

        header_prefix = f"{indent}[{idx_label}] " if idx_label is not None else indent
        header = f"{header_prefix}{metric_name}"
        if show_host:
            header += f" (appId={app_label}, host={host_label})"
        else:
            header += f" (appId={app_label})"
        target_lines.append(header)

        series = metrics_map_to_series(entry.get("metrics", {}))
        summary = summarize_metric_series(series)

        detail_indent = indent + "  "

        if not summary:
            target_lines.append(f"{detail_indent}No datapoints returned for this metric.")
            target_lines.append("")
            return

        target_lines.append(
            f"{detail_indent}Points={summary['count']} | min={format_value(summary['min'])} | max={format_value(summary['max'])} | avg={format_value(summary['avg'])}"
        )
        target_lines.append(
            f"{detail_indent}first={format_value(summary['first'])} @ {format_timestamp(summary['start_timestamp'])}"
        )
        target_lines.append(
            f"{detail_indent}last={format_value(summary['last'])} @ {format_timestamp(summary['end_timestamp'])}"
        )
        target_lines.append(
            f"{detail_indent}delta={format_value(summary['delta'])} over {summary['duration_ms'] / 1000:.1f}s"
        )

        if include_points and series:
            if max_points > 0 and len(series) > max_points:
                step = max(1, len(series) // max_points)
                sampled = [series[i] for i in range(0, len(series), step)][:max_points]
                skipped = len(series) - len(sampled)
            else:
                sampled = series
                skipped = 0

            target_lines.append(f"{detail_indent}Sampled datapoints:")
            for point in sampled:
                target_lines.append(
                    f"{detail_indent}  • {format_timestamp(point['timestamp'])} → {format_value(point['value'])}"
                )
            if skipped > 0:
                target_lines.append(f"{detail_indent}  … {skipped} additional points omitted (increase max_points)")

        target_lines.append("")

    if not metrics_list:
        if last_error:
            lines.append(f"Metrics API reported: {last_error}")
        lines.append("No datapoints were returned for the requested window.")
        metadata_url = f"{AMBARI_METRICS_BASE_URL}/metrics/metadata"
        lines.append(f"Tip: verify metric availability via {metadata_url}")
        if attempt_records and (len(attempt_records) > 1 or attempt_records[0].get("error")):
            lines.append("")
            lines.append("Query attempts (appId → results):")
            for attempt in attempt_records:
                label = f"appId={attempt['appId']}"
                detail = attempt["count"]
                if attempt.get("error"):
                    err = attempt["error"] or ""
                    if len(err) > 120:
                        err = err[:117] + "…"
                    detail += f" (error: {err})"
                lines.append(f"  - {label}: {detail}")
        return "\n".join(lines)

    for idx, metric_entry in enumerate(metrics_list, 1):
        if not isinstance(metric_entry, dict):
            continue
        append_metric_summary(metric_entry, idx)

    if len(attempt_records) > 1 or (attempt_records and attempt_records[0].get("error")):
        lines.append("Query attempts (appId → results):")
        for attempt in attempt_records:
            label = f"appId={attempt['appId']}"
            detail = attempt["count"]
            if attempt.get("error"):
                err = attempt["error"] or ""
                if len(err) > 120:
                    err = err[:117] + "…"
                detail += f" (error: {err})"
            lines.append(f"  - {label}: {detail}")

    return "\n".join(lines)

@mcp.tool()
async def get_prompt_template(section: Optional[str] = None, mode: Optional[str] = None) -> str:
    """Return the canonical English prompt template (optionally a specific section).

    Simplified per project decision: only a single English template file `PROMPT_TEMPLATE.md` is maintained.

    Args:
        section: (optional) section number or keyword (case-insensitive) e.g. "1", "purpose", "tool map".
        mode: (optional) if "headings" returns just the list of section headings with numeric indices.
    """
    # Template is packaged as mcp_ambari_api/prompt_template.md for PyPI distribution
    try:
        content = pkg_resources.files('mcp_ambari_api').joinpath('prompt_template.md').read_text(encoding='utf-8')  # type: ignore[arg-type]
    except FileNotFoundError:
        return "Error: prompt_template.md not found inside package mcp_ambari_api." 
    except Exception as e:
        return f"Error: Unable to read packaged prompt_template.md - {e}" 

    if mode == 'headings':
        import re
        raw_headings = [line[3:].strip() for line in content.splitlines() if line.startswith('## ')]
        # Each raw heading already starts with its own numeric prefix (e.g. "1. Purpose"),
        # so we avoid double-numbering like "1. 1. Purpose" by stripping existing prefix and re-indexing.
        cleaned = []
        for h in raw_headings:
            m = re.match(r'^(\d+)\.\s+(.*)$', h)
            if m:
                cleaned.append(m.group(2).strip())
            else:
                cleaned.append(h)
        lines = ["Section Headings:"]
        for idx, title in enumerate(cleaned, 1):
            lines.append(f"{idx}. {title}")
        return "\n".join(lines)

    if not section:
        return content

    lowered = section.lower().strip()
    sections = {}
    current_key = None
    accumulator = []
    for line in content.splitlines():
        if line.startswith('## '):
            if current_key:
                sections[current_key] = '\n'.join(accumulator).strip()
            title = line[3:].strip()
            key = title.lower()
            sections[key] = ''
            if key and key[0].isdigit():
                num = key.split('.', 1)[0]
                sections[num] = ''
            current_key = key
            accumulator = [line]
        else:
            accumulator.append(line)
    if current_key:
        sections[current_key] = '\n'.join(accumulator).strip()

    if lowered in sections and sections[lowered]:
        return sections[lowered]
    for k, v in sections.items():
        if lowered in k and v:
            return v
    sample_keys = ', '.join(list(sections.keys())[:8])
    return f"Section '{section}' not found. Available sample keys: {sample_keys}"

# =============================================================================
# MCP Prompts (for prompts/list exposure)
# =============================================================================

@mcp.prompt("prompt_template_full")
async def prompt_template_full() -> str:
    """Return the full canonical prompt template."""
    return await get_prompt_template()

@mcp.prompt("prompt_template_headings")
async def prompt_template_headings() -> str:
    """Return compact list of section headings."""
    return await get_prompt_template(mode="headings")

@mcp.prompt("prompt_template_section")
async def prompt_template_section(section: Optional[str] = None) -> str:
    """Return a specific prompt template section by number or keyword.

    If 'section' is omitted: returns a concise help block plus a compact headings list instead of erroring.
    """
    if not section:
        headings_block = await get_prompt_template(mode="headings")
        # Reuse exact multi-line format from prompt_template_headings for consistency.
        return "\n".join([
            "[HELP] Missing 'section' argument.",
            "Specify a section number or keyword.",
            "Examples: 1 | purpose | tool map | decision flow",
            headings_block.strip()
        ])
    return await get_prompt_template(section=section)

# =============================================================================
# Server Execution
# =============================================================================

def main(argv: Optional[List[str]] = None):
    """Entrypoint for MCP Ambari API server.

    Supports optional CLI arguments (e.g. --log-level DEBUG) while remaining
    backward-compatible with stdio launcher expectations.
    """
    global mcp
    
    parser = argparse.ArgumentParser(prog="mcp-aambari-api", description="MCP Ambari API Server")
    parser.add_argument(
        "--log-level",
        dest="log_level",
        help="Logging level override (DEBUG, INFO, WARNING, ERROR, CRITICAL). Overrides MCP_LOG_LEVEL env if provided.",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
    )
    parser.add_argument(
        "--type",
        dest="transport_type",
        help="Transport type (stdio or streamable-http). Default: stdio",
        choices=["stdio", "streamable-http"],
    )
    parser.add_argument(
        "--host",
        dest="host",
        help="Host address for streamable-http transport. Default: 127.0.0.1",
    )
    parser.add_argument(
        "--port",
        dest="port",
        type=int,
        help="Port number for streamable-http transport. Default: 8000",
    )
    parser.add_argument(
        "--auth-enable",
        dest="auth_enable",
        action="store_true",
        help="Enable Bearer token authentication for streamable-http mode. Default: False",
    )
    parser.add_argument(
        "--secret-key",
        dest="secret_key",
        help="Secret key for Bearer token authentication. Required when auth is enabled.",
    )
    # Allow future extension without breaking unknown args usage
    args = parser.parse_args(argv)

    # Determine log level: CLI arg > environment variable > default
    log_level = args.log_level or os.getenv("MCP_LOG_LEVEL", "INFO")
    
    # Set logging level
    logging.getLogger().setLevel(log_level)
    logger.setLevel(log_level)
    logging.getLogger("aiohttp.client").setLevel("WARNING")  # reduce noise at DEBUG
    
    if args.log_level:
        logger.info("Log level set via CLI to %s", args.log_level)
    elif os.getenv("MCP_LOG_LEVEL"):
        logger.info("Log level set via environment variable to %s", log_level)
    else:
        logger.info("Using default log level: %s", log_level)

    # 우선순위: 실행옵션 > 환경변수 > 기본값
    # Transport type 결정
    transport_type = args.transport_type or os.getenv("FASTMCP_TYPE", "stdio")
    
    # Host 결정
    host = args.host or os.getenv("FASTMCP_HOST", "127.0.0.1")
    
    # Port 결정 (간결하게)
    port = args.port or int(os.getenv("FASTMCP_PORT", 8000))
    
    # Authentication 설정 결정
    auth_enable = args.auth_enable or os.getenv("REMOTE_AUTH_ENABLE", "false").lower() in ("true", "1", "yes", "on")
    secret_key = args.secret_key or os.getenv("REMOTE_SECRET_KEY", "")
    
    # Validation for streamable-http mode with authentication
    if transport_type == "streamable-http":
        if auth_enable:
            if not secret_key:
                logger.error("ERROR: Authentication is enabled but no secret key provided.")
                logger.error("Please set REMOTE_SECRET_KEY environment variable or use --secret-key argument.")
                return
            logger.info("Authentication enabled for streamable-http transport")
        else:
            logger.warning("WARNING: streamable-http mode without authentication enabled!")
            logger.warning("This server will accept requests without Bearer token verification.")
            logger.warning("Set REMOTE_AUTH_ENABLE=true and REMOTE_SECRET_KEY to enable authentication.")

    # Note: MCP instance with authentication is already initialized at module level
    # based on environment variables. CLI arguments will override if different.
    if auth_enable != _auth_enable or secret_key != _secret_key:
        logger.warning("CLI authentication settings differ from environment variables.")
        logger.warning("Environment settings take precedence during module initialization.")

    # Transport 모드에 따른 실행
    if transport_type == "streamable-http":
        logger.info(f"Starting streamable-http server on {host}:{port}")
        mcp.run(transport="streamable-http", host=host, port=port)
    else:
        logger.info("Starting stdio transport for local usage")
        mcp.run(transport='stdio')
