# AWS Blogs MCP Server - Universal Distribution

A Model Context Protocol (MCP) server that provides access to AWS blog content. Search and retrieve blog posts from aws.amazon.com directly in your AI assistant.

## 🌍 Cross-Platform Support

This distribution works on:
- ✅ **macOS** (Intel & Apple Silicon)
- ✅ **Linux** (Ubuntu, CentOS, etc.)
- ✅ **Windows** (10, 11)

## 🚀 Quick Installation

### Prerequisites
- **Python 3.8+** (required on all platforms)
- **Kiro IDE** or any MCP-compatible client

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

### Step 2: Configure MCP

Add the appropriate configuration to your `.kiro/settings/mcp.json`:

**For macOS/Linux:**
```json
{
  "mcpServers": {
    "aws-blogs": {
      "command": "/FULL/PATH/TO/aws-blogs-mcp-server/aws-blogs-mcp-server",
      "args": [],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "disabled": false,
      "autoApprove": [
        "search_aws_blogs",
        "find_similar_blogs",
        "find_blog_by_title",
        "get_blog_post",
        "get_blog_categories"
      ],
      "disabledTools": []
    }
  }
}
```

**For Windows:**
```json
{
  "mcpServers": {
    "aws-blogs": {
      "command": "python",
      "args": ["C:\\FULL\\PATH\\TO\\aws-blogs-mcp-server\\aws-blogs-mcp-server.py"],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "disabled": false,
      "autoApprove": [
        "search_aws_blogs",
        "find_similar_blogs", 
        "find_blog_by_title",
        "get_blog_post",
        "get_blog_categories"
      ],
      "disabledTools": []
    }
  }
}
```

**Universal Python approach (recommended):**
```json
{
  "mcpServers": {
    "aws-blogs": {
      "command": "python",
      "args": ["/FULL/PATH/TO/aws-blogs-mcp-server/aws-blogs-mcp-server.py"],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "disabled": false,
      "autoApprove": [
        "search_aws_blogs",
        "find_similar_blogs",
        "find_blog_by_title", 
        "get_blog_post",
        "get_blog_categories"
      ],
      "disabledTools": []
    }
  }
}
```

### Step 3: Update Paths

**IMPORTANT:** Replace `/FULL/PATH/TO/aws-blogs-mcp-server` with the actual path where you extracted this package.

**Examples:**
- macOS: `/Users/username/Downloads/aws-blogs-mcp-server`
- Linux: `/home/username/aws-blogs-mcp-server`
- Windows: `C:\Users\username\Downloads\aws-blogs-mcp-server`

### Step 4: Restart Kiro

Close and reopen Kiro to load the new MCP server.

### Step 5: Test

Try asking: "Search for AWS Lambda blogs"

## 🛠️ Available Features

- **search_aws_blogs**: Search for blog posts by keywords
- **find_similar_blogs**: Find related blog posts based on your idea
- **find_blog_by_title**: Locate specific blog posts by title
- **get_blog_post**: Retrieve full content of a blog post
- **get_blog_categories**: Browse available AWS blog categories

## 🔧 Troubleshooting

### Common Issues

**"Command not found" or "Module not found":**
1. Verify Python 3.8+ is installed: `python --version` or `python3 --version`
2. Install dependencies: `pip install -r requirements.txt`
3. Use the Python-based configuration (most reliable)

**"Permission denied" (macOS/Linux):**
```bash
chmod +x aws-blogs-mcp-server
chmod +x install.sh
```

**Path issues:**
- Use absolute paths in MCP configuration
- Avoid spaces in directory names
- On Windows, use double backslashes: `C:\\path\\to\\server`

### Testing the Server

You can test the server directly:

**macOS/Linux:**
```bash
./aws-blogs-mcp-server
```

**Windows:**
```cmd
python aws-blogs-mcp-server.py
```

The server should start and wait for connections (this is normal behavior).

## 📁 File Structure

```
aws-blogs-mcp-server/
├── src/                          # Source code
├── mcp-config-examples/          # Configuration examples
├── aws-blogs-mcp-server          # Unix launcher
├── aws-blogs-mcp-server.bat      # Windows launcher  
├── aws-blogs-mcp-server.py       # Python launcher (universal)
├── install.sh                    # Unix install script
├── install.bat                   # Windows install script
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## 🆘 Support

If you encounter issues:

1. Check that Python 3.8+ is installed
2. Verify all dependencies are installed
3. Use absolute paths in MCP configuration
4. Try the Python-based launcher (most compatible)
5. Check Kiro's MCP server panel for error messages

## 📄 License

MIT License - see LICENSE file for details.
