import sys
import os

# Add the mcp_server folder to sys.path
sys.path.append(os.path.dirname(__file__))

from fastapi import FastAPI, HTTPException
from tools.models import ToolRequest
from tools.main import handle_tool_request

app = FastAPI(
    title="Secure MCP Server",
    description="Policy-governed MCP server with PEP/PDP",
    version="1.0.0"
)

@app.post("/mcp/tool")
def invoke_tool(request: ToolRequest):
    response = handle_tool_request(request)

    if response.get("status") == "denied":
        raise HTTPException(status_code=403, detail=response["reason"])

    return response
