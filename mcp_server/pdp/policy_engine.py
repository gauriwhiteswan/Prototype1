import yaml
from pathlib import Path

POLICY_FILE = Path(__file__).parent.parent / "policies/github_access.yaml"

with open(POLICY_FILE) as f:
    POLICY = yaml.safe_load(f)

def evaluate_policy(request):
    for rule in POLICY["rules"]:
        if rule["tool"] == request.tool_name:
            if rule["action"] == "allow":
                return {
                    "allowed": True,
                    "reason": "Policy allows access"
                }
            else:
                return {
                    "allowed": False,
                    "reason": rule.get("reason", "Denied by policy")
                }

    return {
        "allowed": False,
        "reason": "No matching policy rule"
    }
