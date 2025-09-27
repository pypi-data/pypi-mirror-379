"""
Resource definitions for Bitbucket MCP Server
Contains all resource functions for accessing common Bitbucket data
"""

from fastmcp.utilities.logging import get_logger

from src.modules.tools import tools
from src.utils.api_client import make_request
from src.utils.config import REPO_SLUG, WORKSPACE

logger = get_logger(__name__)

# ===== Static Resource Functions =====
# These are defined as standalone functions and registered via mcp.add_resource()

async def get_default_reviewers() -> dict:
    try:
        default_reviewers = await make_request(
            "GET", f"repositories/{WORKSPACE}/{REPO_SLUG}/default-reviewers")

        reviewers = {}
        for reviewer in default_reviewers.get("values", []):
            account_id = reviewer.get("account_id", "")
            uuid = reviewer.get("uuid", "")
            reviewers[uuid] = {
                "username": reviewer.get("nickname", ""),
                "display_name": reviewer.get("display_name", ""),
                "account_id": account_id,
                "uuid": uuid,
                "source": "default_reviewer"
            }
        return reviewers

    except Exception as e:
        return {"error": str(e)}



async def get_repository_info() -> dict:
    return await tools.repo_get(REPO_SLUG, verbosity=tools.Verbosity.full)



async def get_recent_pipelines() -> dict:
    try:
        pipelines = await make_request(
            "GET",
            f"repositories/{WORKSPACE}/{REPO_SLUG}/pipelines",
            params={
                "pagelen": 10,
                "sort": "-created_on"
            })
        return pipelines
    except Exception as e:
        return {"error": str(e)}

async def get_open_prs() -> dict:
    return await tools.pr_list(REPO_SLUG, state=tools.PRState.OPEN, verbosity=tools.Verbosity.full, limit=20)



async def get_workspace_members() -> dict:
    """Available PR reviewers in workspace"""
    try:
        members = await make_request(
            "GET", f"workspaces/{WORKSPACE}/members")
        return members
    except Exception as e:
        return {"error": str(e)}


async def get_repository_branches() -> dict:
    """All branches with latest commit info (max 50)"""
    try:
        branches = await make_request(
            "GET",
            f"repositories/{WORKSPACE}/{REPO_SLUG}/refs/branches",
            params={"pagelen": 50}
        )
        # Simplify branch data for easier consumption
        simplified = []
        for branch in branches.get("values", []):
            branch_data = {
                "name": branch.get("name", ""),
                "target_hash": branch.get("target", {}).get("hash", "")[:8],
                "last_commit_date": branch.get("target", {}).get("date"),
                "author": branch.get("target", {}).get("author", {}).get("user", {}).get("display_name")
            }
            # Only include branches with names
            if branch_data["name"]:
                simplified.append(branch_data)

        return {
            "branches": simplified,
            "count": len(simplified),
            "repository": f"{WORKSPACE}/{REPO_SLUG}"
        }
    except Exception as e:
        return {"error": str(e)}


async def get_branching_model() -> dict:
    """Branch strategy including default PR destination"""
    try:
        model = await make_request(
            "GET",
            f"repositories/{WORKSPACE}/{REPO_SLUG}/branching-model"
        )

        # Simplify the response for easier consumption
        simplified = {
            "development_branch": None,
            "production_branch": None,
            "branch_prefixes": {},
            "default_pr_destination": None
        }

        if "development" in model and model["development"]:
            simplified["development_branch"] = model["development"].get("name")
            simplified["default_pr_destination"] = model["development"].get("name")

        if "production" in model and model["production"]:
            simplified["production_branch"] = model["production"].get("name")
            if not simplified["default_pr_destination"]:
                simplified["default_pr_destination"] = model["production"].get("name")

        if "branch_types" in model:
            for branch_type in model["branch_types"]:
                kind = branch_type.get("kind", "")
                prefix = branch_type.get("prefix", "")
                if kind and prefix:
                    simplified["branch_prefixes"][kind] = prefix

        return simplified

    except Exception as e:
        return {
            "error": str(e),
            "development_branch": "develop",
            "production_branch": "master",
            "default_pr_destination": "develop"
        }
