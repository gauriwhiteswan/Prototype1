from .pep.enforcement import enforce_policy
from .tools.github import execute_github_tool
from .models import ToolRequest

def handle_tool_request(request: ToolRequest):
    decision = enforce_policy(request)

    if not decision["allowed"]:
        return {
            "status": "denied",
            "reason": decision["reason"]
        }

    return execute_github_tool(
        request.tool_name,
        request.arguments
    )
