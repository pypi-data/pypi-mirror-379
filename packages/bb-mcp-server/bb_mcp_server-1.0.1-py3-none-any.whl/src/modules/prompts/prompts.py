
from src.utils.api_client import make_request
from src.utils.config import REPO_SLUG, WORKSPACE


async def commit_push_and_create_pr() -> str:
    reviewers = await make_request(
        "GET",
        f"repositories/{WORKSPACE}/{REPO_SLUG}/default-reviewers",
        accept_type="application/json")
    user = await make_request("GET", "user", accept_type="application/json")
    reviewers["values"] = [
        r for r in reviewers["values"] if r["uuid"] != user["uuid"]
    ]
    if not reviewers["values"]:
        return (
            "Commit all changes, push to remote, and create a pull request in the "
            "Bitbucket UI (no direct tooling exposed)."
        )
    reviewers["values"] = [
        f"{r['display_name']} ({r['uuid']})" for r in reviewers["values"]
    ]
    return (
        "Commit all changes, push to remote, and create a pull request in Bitbucket. "
        f"Suggested reviewers: {reviewers['values']}."
    )


async def create_markdown_from_latest_failed_pipeline() -> str:
    pipeline = await make_request(
        "GET",
        f"repositories/{WORKSPACE}/{REPO_SLUG}/pipelines/?sort=-created_on&pagelen=1&status=FAILED",
        accept_type="application/json")
    return (
        "Call pipe.fail.summary to summarise the latest failed pipeline, then "
        f"create a markdown report from the returned items: {pipeline}"
    )
