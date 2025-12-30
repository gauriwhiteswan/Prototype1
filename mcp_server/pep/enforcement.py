from ..pdp.policy_engine import evaluate_policy
from ..contracts import tool_contracts

def enforce_policy(request):
    # 1. Validate tool exists
    if request.tool_name not in tool_contracts:
        return {
            "allowed": False,
            "reason": "Tool not registered"
        }

    contract = tool_contracts[request.tool_name]

    # 2. Enforce agent allow-list
    if request.agent_context.agent_id not in contract["allowed_agents"]:
        return {
            "allowed": False,
            "reason": "Agent not allowed for this tool"
        }

    # 3. Enforce schema
    for param in request.arguments:
        if param not in contract["parameters"]:
            return {
                "allowed": False,
                "reason": f"Invalid parameter: {param}"
            }

    # 4. Ask PDP
    return evaluate_policy(request)
