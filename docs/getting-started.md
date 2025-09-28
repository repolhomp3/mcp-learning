# Getting Started with MCP Learning Project

## Quick Setup

### 1. Install Dependencies
```bash
cd /Users/karl/MCP
pip install -r requirements.txt
```

### 2. Test Local MCP Servers

**File System Server:**
```bash
cd local-mcp
python filesystem-server.py
# Test with: {"method": "tools/list"}
```

**Database Server:**
```bash
cd database-mcp  
python sqlite-server.py
# Test with: {"method": "tools/list"}
```

### 3. AWS Setup (Optional)
```bash
# Install AWS CLI
brew install awscli

# Configure credentials
aws configure
# Enter your Access Key, Secret Key, Region (us-east-1), Output (json)

# Test AWS MCP
cd aws-mcp
python aws-server.py
```

## Testing MCP Servers

### Manual Testing
Each server accepts JSON-RPC requests via stdin:

```bash
echo '{"method": "tools/list"}' | python server.py
echo '{"method": "tools/call", "params": {"name": "read_file", "arguments": {"path": "test.txt"}}}' | python server.py
```

### Integration with AI Clients
- Claude Desktop: Add server configs to `claude_desktop_config.json`
- Custom clients: Use the MCP protocol specification

## Learning Path

1. **Start Local**: File system and database operations
2. **Add AWS**: S3, basic services (free tier)
3. **Explore Bedrock**: Start with cheapest models
4. **Build Custom**: Create domain-specific MCP servers

## Common Issues

**"No credentials" error**: Run `aws configure`
**"Permission denied"**: Check file paths and permissions  
**"Module not found"**: Run `pip install -r requirements.txt`
**High AWS costs**: Check billing dashboard, set alerts