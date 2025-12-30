import os

class Settings:
    MCP_SERVER_NAME = "secure-mcp-server"
    ENV = os.getenv("ENV", "dev")

    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    if not GITHUB_TOKEN:
        raise RuntimeError("GITHUB_TOKEN must be set in environment")

settings = Settings()
