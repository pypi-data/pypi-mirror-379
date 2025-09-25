# AWS Blogs MCP Server

A Model Context Protocol (MCP) server that provides access to AWS blog content. Search and retrieve blog posts from aws.amazon.com directly in your AI assistant.

## 🌍 Compatible IDEs & Clients

This MCP server works with any MCP-compatible client:
- ✅ **Amazon Q Developer** (VS Code, JetBrains, CLI)
- ✅ **Claude Desktop**
- ✅ **Kiro IDE**
- ✅ **Any MCP-compatible client**

## 🚀 Easy Installation (Recommended)

### Using uvx (Universal Package Manager)

The easiest way to use this MCP server is via PyPI:

```bash
# No installation needed - uvx handles everything
```

Add to your MCP configuration:

**Amazon Q Developer (`~/.aws/amazonq/mcp.json`):**
```json
{
  "mcpServers": {
    "aws-blogs": {
      "command": "uvx",
      "args": ["aws-blogs-mcp-server"],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "disabled": false,
      "autoApprove": [
        "search_aws_blogs",
        "find_blog_by_title",
        "get_blog_post",
        "get_blog_categories",
        "find_similar_blogs"
      ]
    }
  }
}
```

**Claude Desktop (`~/Library/Application Support/Claude/claude_desktop_config.json` on macOS):**
```json
{
  "mcpServers": {
    "aws-blogs": {
      "command": "uvx",
      "args": ["aws-blogs-mcp-server"],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      }
    }
  }
}
```

**Kiro IDE (`~/.kiro/settings/mcp.json`):**
```json
{
  "mcpServers": {
    "aws-blogs": {
      "command": "uvx",
      "args": ["aws-blogs-mcp-server"],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "disabled": false,
      "autoApprove": [
        "search_aws_blogs",
        "find_blog_by_title",
        "get_blog_post",
        "get_blog_categories",
        "find_similar_blogs"
      ]
    }
  }
}
```

## 🛠️ Manual Installation (Alternative)

### Prerequisites
- **Python 3.8+** (required on all platforms)
- **uvx** or **pip** for package management

### Cross-Platform Support
- ✅ **macOS** (Intel & Apple Silicon)
- ✅ **Linux** (Ubuntu, CentOS, etc.)
- ✅ **Windows** (10, 11)

### Step 1: Install Dependencies

**On macOS/Linux:**
```bash
./install.sh
```

**On Windows:**
```cmd
install.bat
```

**Manual installation (any platform):**
```bash
pip install -r requirements.txt
```

### Step 2: Configure MCP (Manual Installation)

For manual installation, use the full path to the executable:

```json
{
  "mcpServers": {
    "aws-blogs": {
      "command": "/FULL/PATH/TO/aws-blogs-mcp-server",
      "args": [],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "disabled": false,
      "autoApprove": [
        "search_aws_blogs",
        "find_blog_by_title",
        "get_blog_post",
        "get_blog_categories",
        "find_similar_blogs"
      ]
    }
  }
}
```

## 🛠️ Available Features

- **search_aws_blogs**: Search for blog posts by keywords
- **find_blog_by_title**: Locate specific blog posts by title
- **get_blog_post**: Retrieve full content of a blog post
- **get_blog_categories**: Browse available AWS blog categories
- **find_similar_blogs**: Find related blog posts

## 🧪 Testing

Try these example queries in your AI assistant:
- "Search for AWS Lambda blogs"
- "Find blog posts about Amazon Bedrock"
- "Get the latest AWS security blog posts"
- "Show me blogs about cost optimization"

## 🔧 Troubleshooting

### Common Issues

**uvx not found:**
```bash
pip install uv
```

**"Command not found" or "Module not found":**
1. Verify Python 3.8+ is installed: `python --version`
2. For manual installation: `pip install -r requirements.txt`
3. Use absolute paths in MCP configuration

**Permission denied (macOS/Linux):**
```bash
chmod +x aws-blogs-mcp-server
```

### Testing the Server Directly

**Using uvx:**
```bash
uvx aws-blogs-mcp-server
```

**Manual installation:**
```bash
./aws-blogs-mcp-server  # macOS/Linux
python aws-blogs-mcp-server.py  # Windows/Universal
```

## 📦 Package Information

- **PyPI Package**: https://pypi.org/project/aws-blogs-mcp-server/
- **Version**: 1.0.0
- **License**: MIT

## 🆘 Support

If you encounter issues:

1. **Recommended**: Use the uvx installation method
2. Check that Python 3.8+ is installed
3. Verify your MCP client supports the configuration format
4. Use absolute paths for manual installations
5. Check your IDE's MCP server panel for error messages

## 📄 License

MIT License - see LICENSE file for details.
