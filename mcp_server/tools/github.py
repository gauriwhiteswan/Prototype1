from ..config import settings
import requests

GITHUB_API = "https://api.github.com"

HEADERS = {
    "Authorization": f"token {settings.GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

def execute_github_tool(tool_name, args):
    if tool_name == "list_repositories":
        org = args["org"]
        resp = requests.get(
            f"{GITHUB_API}/orgs/{org}/repos",
            headers=HEADERS
        )
        return resp.json()

    raise RuntimeError("Tool execution not implemented")
