This repo contains code for a MCP interacting with GLPI API to allow consuming it from any LLM.
Additionally a lightweight client is available

| Available tools   |
|-------------------|
|create_reservation |
|delete_reservation |
|info_computer      |
|info_reservation   |
|get_user           |
|list_computers     |
|list_reservations  |
|list_users         |
|update_computer    |
|update_reservation |

# Requirements

- Available glpi instance
- valid user and API token
- prettytable python library

# Installation

```
pip3 install glpic
```

# Using MCP

## STDIO

Include the following configuration snippet In VSCode or Claude Desktop:

```json
"mcpServers": {
    "glpi": {
        "command": "python3",
        "args": ["/path/to/glpic/src/glpic/mcp_server.py", "--stdio"],
        "env": {
            "GLPI_URL": "https://server/apirest.php",
            "GLPI_USER": "myuser",
            "GLPI_TOKEN": "mytoken"
            }
        }
    }
```

## Streamable HTTP

For Streamable HTTP, first start the server in a terminal:

```
glpimcp
```

You can then point to the server from your client with a modified snippet

```json
"mcpServers": {
         "glpi": {
             "command": "/usr/local/bin/npx",
             "args": ["mcp-remote", "http://your_server:8000/mcp", "--allow-http",
             "--header", "GLPI_URL: https://server/apirest.php",
             "--header", "GLPI_USER: myuser",
             "--header", "GLPI_TOKEN: mytoken"]
        }
    }
```

For Claude Code, you can add the mcp directly from command line:

```
claude mcp add --transport http glpi http://your_server:8000/mcp -H "GLPI_URL: https://server/apirest.php" -H "GLPI_USER: myuser" -H "GLPI_TOKEN: mytoken"
```

# Using client

Store your creds in any env file such as [glpic.env.sample](glpic.env.sample) and set data accordingly. You can then use `glpic` and access similar functions
