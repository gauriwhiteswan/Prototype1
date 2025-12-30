# Prompt Injection Threat Model

## Threats
- Tool name manipulation
- Argument smuggling
- Instruction override attempts

## Controls
- Tool name is never agent-controlled
- Strict tool contracts
- PEP blocks unknown parameters
- PDP enforces explicit allow/deny

## Trust Boundary
Agents are untrusted.
MCP server is the security authority.
