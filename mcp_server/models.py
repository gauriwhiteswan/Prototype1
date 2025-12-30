from pydantic import BaseModel
from typing import Dict, Any

class AgentContext(BaseModel):
    agent_id: str
    intent: str

class ToolRequest(BaseModel):
    tool_name: str
    arguments: Dict[str, Any]
    agent_context: AgentContext
