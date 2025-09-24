# Quick Setup Guide for Cherry Studio

## 🚀 5-Minute Setup

### Step 1: Install UV (Package Manager)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Step 2: Test Installation
```bash
uvx mcp-evaluation-server --help
```

### Step 3: Configure Cherry Studio
1. Open Cherry Studio
2. Go to Settings → MCP Servers
3. Click "Add Server"
4. Fill in:
   - **Name**: `MCP Evaluation Server`
   - **Type**: `stdio`
   - **Command**: `uvx mcp-evaluation-server`
5. Click "Save"

### Step 4: Verify Setup
1. Restart Cherry Studio
2. Check if the server appears in your MCP tools list
3. Try using the `health_check` tool

## ✅ Verification

Run this command to test everything works:
```bash
python scripts/test_quick.py
```

Expected output: `🎉 Cherry Studio兼容性重构成功！`

## 🔧 If You Need Help

1. **UV not working?** Make sure you installed it correctly
2. **Cherry Studio can't connect?** Check the command is exactly `uvx mcp-evaluation-server`
3. **Tools not appearing?** Restart Cherry Studio after adding the server

## 📚 What You Can Do

Once set up, you'll have access to:
- Code quality evaluation
- Performance analysis
- Report generation
- Benchmarking tools
- Health checks

## 🎯 Next Steps

- Try the different tools available
- Check the full documentation in `CHERRY_STUDIO_INTEGRATION.md`
- Run comprehensive tests with `python scripts/test_mcp_protocol.py`

---

**You're all set!** The MCP Evaluation Server is now integrated with Cherry Studio and ready to use.