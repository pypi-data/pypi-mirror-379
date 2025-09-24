# z/OS MCP Client

MCP client for connecting Amazon Q CLI to z/OS mainframe operations.

## Installation

Install using uvx:
```bash
uvx install zos-mcp-client
```

Or install from source:
```bash
pip install .
```

## Amazon Q CLI Configuration

Add to your MCP configuration file (`~/.config/mcp/mcp-config.json`):

```json
{
  "mcpServers": {
    "zos-mainframe": {
      "command": "uvx",
      "args": ["zos-mcp-client"],
      "env": {
        "ZOS_HOST": "your-mainframe-host.company.com",
        "ZOS_PORT": "8080"
      }
    }
  }
}
```

Replace `your-mainframe-host.company.com` with your actual mainframe hostname or IP address.

## Usage

Start the z/OS MCP server on your mainframe, then use Amazon Q CLI:

```bash
q chat --mcp-config ~/.config/mcp/mcp-config.json
```

Available tools:
- Read PS datasets
- List PDS members  
- Read PDS member content
- Submit batch jobs

## Requirements

- Python 3.9+
- Access to z/OS MCP server
- Amazon Q CLI with MCP support
