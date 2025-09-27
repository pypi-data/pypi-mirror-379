# ===== Main Registration Function =====


from fastmcp.resources import Resource
from fastmcp.utilities.logging import get_logger

from src.utils.config import REPO_SLUG, WORKSPACE

from .iterators import register_pipeline_resources, register_pr_resources
from .resources import (get_branching_model, get_default_reviewers,
                        get_open_prs, get_recent_pipelines,
                        get_repository_branches, get_repository_info,
                        get_workspace_members)

logger = get_logger(__name__)

async def init(mcp) -> None:
    """Register all resources."""   
    
    logger.info("Registering Bitbucket resources...")

    resources_list = [
        [get_repository_info, f"repo://{REPO_SLUG}/info"],
        [get_recent_pipelines, f"pipelines://{REPO_SLUG}/recent"],
        [get_open_prs, f"pull-requests://{REPO_SLUG}/open"],
        [get_workspace_members, f"workspace://{WORKSPACE}/members"],
        [get_default_reviewers, f"workspace://{WORKSPACE}/default-reviewers"],
        [get_repository_branches, f"repo://{REPO_SLUG}/branches"],
        [get_branching_model, f"repo://{REPO_SLUG}/branching-model"],
    ]

    resources_objects: list[dict] = []
    for func, uri in resources_list:
                resources_objects.append({
                    "fn": func,
                    "uri": uri,
                    "name": f"Resource for {uri}",
                    "title": f"Resource Information for {uri}",
                    "description": f"Details about the resource '{uri}'",
                    "mime_type": "application/json"
                })

    resources = [Resource.from_function(r["fn"], r["uri"], r["name"], r["title"], r["description"], r["mime_type"]) for r in resources_objects]

    for resource in resources:
        mcp.add_resource(resource)

    # Register dynamic pipeline resources
    await register_pipeline_resources(mcp)

    # Register dynamic PR resources
    await register_pr_resources(mcp)
