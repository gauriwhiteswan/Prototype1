import json
from pathlib import Path

with open(Path(__file__).parent / "github_tools.json") as f:
    tool_contracts = json.load(f)
