from fastapi import FastAPI, HTTPException
from .models import ToolRequest
from .main import handle_tool_request

app = FastAPI(
    title="Secure MCP Server",
    description="Policy-governed MCP server with PEP/PDP",
    version="1.0.0"
)

# ------------------------
# Root landing page
# ------------------------
@app.get("/")
def home():
    return {
        "status": "running",
        "message": "MCP policy-governed server ready.",
        "docs_url": "/docs",
        "tool_endpoint": "/mcp/tool"
    }


# ------------------------
# MCP Tool execution endpoint
# ------------------------
@app.post("/mcp/tool")
def invoke_tool(request: ToolRequest):
    response = handle_tool_request(request)

    if response.get("status") == "denied":
        raise HTTPException(status_code=403, detail=response["reason"])

    return response
