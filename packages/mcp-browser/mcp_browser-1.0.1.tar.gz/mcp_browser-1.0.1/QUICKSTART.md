# MCP Browser Quick Start Guide

## Installation in 3 Steps (5 Minutes Total)

### Step 1: Clone and Setup

```bash
# Clone the repository
git clone https://github.com/browserpymcp/mcp-browser.git
cd mcp-browser

# Use the project management script for installation
./mcp-browser install  # Install dependencies in project-local venv
./mcp-browser init     # Initialize MCP configuration
```

This will:
- ✅ Check system requirements (Python 3.8+, Chrome)
- ✅ Create project-local virtual environment in `.venv/`
- ✅ Install all dependencies (MCP, WebSocket, Playwright)
- ✅ Set up directory structure (tmp/, data/, logs/)
- ✅ Create MCP configuration file
- ✅ Configure default settings

### Step 2: Load Chrome Extension (30 seconds)

1. Open Chrome and go to `chrome://extensions/`
2. Enable "Developer mode" (top right toggle)
3. Click "Load unpacked"
4. Select the `extension/` folder from this project
5. Extension icon appears with green connection indicator
6. Extension automatically connects to WebSocket (ports 8875-8895)

### Step 3: Configure Claude Code Integration

```bash
# Auto-configure Claude Code integration
./setup-claude-code.sh
```

This script will:
- ✅ Test MCP server functionality
- ✅ Validate all 11 MCP tools
- ✅ Generate Claude Code configuration
- ✅ Create demo files for testing
- ✅ Show connection instructions

Then start the MCP server:
```bash
./mcp-browser start  # Start MCP server in background
# or
./mcp-browser dev    # Start in development mode with hot reload
```

Claude Code will automatically discover and use all 11 browser automation tools.

## Testing the Setup

### 1. Start the Server

```bash
mcp-browser start
```

You should see:
```
[✓] WebSocket server listening on port 8875
[✓] MCP Browser server started successfully
[✓] Process ID: 12345
[✓] Ready for browser connections
```

### 2. Check Extension Connection

- Look at the extension icon in Chrome toolbar
- Green badge with port number = connected
- Red badge with "!" = disconnected

### 3. Test Console Capture and DOM Interaction

#### Test Console Capture
Open any website and run in the browser console:
```javascript
console.log("Test message from MCP Browser");
console.error("Test error");
console.warn("Test warning");
```

#### Test DOM Interaction with Demo Page
```bash
# Open the demo page
open tmp/demo_dom_interaction.html
```

Then ask Claude Code to:
- "Fill the username field with 'testuser'"
- "Click the test button and wait for results"
- "Select 'Canada' from the country dropdown"
- "Fill out the entire form and submit it"

### 4. Use All 11 Tools in Claude Code

Ask Claude to:
- **Navigation**: "Navigate my browser to https://example.com"
- **Console Logs**: "Show me the console logs from my browser"
- **Screenshots**: "Take a screenshot of my browser"
- **DOM Interaction**: "Click the login button on this page"
- **Form Filling**: "Fill out this contact form with test data"
- **Element Selection**: "Select 'Premium' from the subscription dropdown"
- **JavaScript Execution**: "Execute this JavaScript code in the browser"
- **Element Waiting**: "Wait for the loading spinner to disappear"
- **Form Submission**: "Submit this form and capture the response"

## Common Commands

```bash
# Install and setup
./mcp-browser install    # Install dependencies
./mcp-browser init       # Initialize configuration

# Server management
./mcp-browser start      # Start MCP server in background
./mcp-browser stop       # Stop MCP server
./mcp-browser status     # Check server and extension status
./mcp-browser dev        # Start in development mode

# Maintenance
./mcp-browser logs       # View logs (default: last 50 lines)
./mcp-browser logs 100   # View last 100 lines
./mcp-browser clean      # Clean temporary files and cache
./mcp-browser update     # Update dependencies

# Information
./mcp-browser version    # Show version information
./mcp-browser help       # Show all available commands

# Chrome extension
./mcp-browser extension  # Open Chrome extension setup page

# Testing
./mcp-browser test       # Run test suite
```

## Troubleshooting

### Extension Not Connecting?

1. Check server status: `./mcp-browser status`
2. Verify port range 8875-8895 is available: `netstat -an | grep LISTEN | grep 887`
3. Click extension icon - should show green connection with port number
4. Check Chrome DevTools console for WebSocket errors
5. Try refreshing the page after extension loads

### No Console Logs Captured?

1. Verify extension shows green connection status
2. Refresh the web page after extension loads
3. Check for "[MCP Browser] Console capture initialized" in console
4. Test with: `console.log("Test from MCP Browser")`
5. View logs: `./mcp-browser logs`

### DOM Interaction Not Working?

1. Ensure elements are visible and loaded
2. Try different selectors (CSS, XPath, text)
3. Use `browser_wait_for_element` for dynamic content
4. Check browser console for JavaScript errors
5. Verify WebSocket connection is active

### Claude Can't Access Tools?

1. Run setup script: `./setup-claude-code.sh`
2. Verify MCP server is running: `./mcp-browser start`
3. Check configuration in Claude Code
4. Test individual tools with validation script
5. Review MCP server logs: `./mcp-browser logs`

### Installation Issues?

1. Check Python version: `python3 --version` (need 3.8+)
2. Verify virtual environment: `ls -la .venv/`
3. Re-run installation: `rm -rf .venv && ./mcp-browser install`
4. Check system requirements: `./mcp-browser status`
5. Review installation logs for specific errors

## Architecture Overview

```
Browser Tab → Console Messages + DOM Events → Chrome Extension
                                                     ↓
                                            WebSocket (8875-8895)
                                                     ↓
                                              MCP Browser Server
                                                     ↓
                                            11 MCP Tools Available
                                                     ↓
                                               MCP Protocol
                                                     ↓
                                               Claude Code
```

**Key Components:**
- **Chrome Extension**: Captures console logs, handles DOM interaction commands
- **WebSocket Server**: Bidirectional communication with auto-port discovery
- **MCP Server**: Exposes 11 tools for browser automation
- **Storage Layer**: JSONL files with automatic rotation (50MB, 7-day retention)
- **Professional CLI**: Complete process management and monitoring

## Data Storage and Organization

### Runtime Directory Structure
```
~/.mcp-browser/
├── config/
│   └── settings.json        # Auto-generated configuration
├── logs/
│   ├── mcp-browser.log      # Main server log
│   └── [8875-8895]/         # Port-specific browser logs
├── run/
│   └── mcp-browser.pid      # Process ID tracking
└── data/                    # JSONL storage with rotation
    └── [port]/
        ├── console.jsonl        # Current session logs
        └── console_20240921_*.jsonl  # Rotated archives
```

### Storage Features
- **Automatic Rotation**: Files rotate at 50MB
- **Retention Policy**: 7-day automatic cleanup
- **JSONL Format**: Easy parsing and processing
- **Port Isolation**: Separate logs per WebSocket connection
- **Process Tracking**: PID files for proper process management

## Next Steps and Resources

### Immediate Testing
```bash
# Run comprehensive installation test
./test_installation.sh

# Run feature demonstration
./demo.sh

# Test DOM interaction with demo page
open tmp/demo_dom_interaction.html
```

### Available Documentation
- **README.md**: Complete feature overview and setup guide
- **INSTALLATION.md**: Detailed installation and configuration
- **CLAUDE.md**: AI agent instructions and architecture details
- **DEVELOPER.md**: Technical implementation guide

### Getting Help
- **GitHub Issues**: https://github.com/browserpymcp/mcp-browser/issues
- **Self-Diagnosis**: `mcp-browser status` and `./test_installation.sh`
- **Demo Scripts**: `./demo.sh` for comprehensive feature testing
- **Validation**: `./setup-claude-code.sh` for MCP tool verification

### Success Indicators
✅ Extension shows green connection status
✅ `mcp-browser status` shows running server
✅ Claude Code can see all 11 MCP tools
✅ Demo page interactions work smoothly
✅ Console logs are captured in real-time