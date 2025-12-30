from models import ToolRequest, AgentContext
from main import handle_tool_request

request = ToolRequest(
    tool_name="list_repositories",
    arguments={"org": "openai"},
    agent_context=AgentContext(
        agent_id="claude-desktop",
        intent="list repositories"
    )
)

response = handle_tool_request(request)
print(response)
