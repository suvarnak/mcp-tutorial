# MCP Tutorial

This project uses UV for Python environment management and runs an MCP server.

## Prerequisites

- Python 3.12 or higher
- UV package manager

## Setup Instructions

1. Install UV if you haven't already:
   ```bash
   pip install uv
   ```

2. Create and activate a virtual environment using UV:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies using UV:
   ```bash
   uv pip install -e .
   ```

## Running the MCP Server

1. Make sure your virtual environment is activated:
   ```bash
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Run the MCP server:
   ```bash
   uv run main.py
   ```

## Running in Claude Desktop

1. Open Claude Desktop application

2. Go to Developer Settings (you can access this through the settings menu)

3. Locate the configuration file at:
   ```
   %APPDATA%\Claude\claude_desktop_config.json
   ```
   (On Windows, this is typically at `C:\Users\<username>\AppData\Roaming\Claude\claude_desktop_config.json`)

4. Add or modify the `mcpServers` section in the configuration file:
   ```json
   {
     "mcpServers": {
       "sk-docs-server": {
         "command": "c:\\users\\<username>\\.local\\bin\\uv.exe",
         "args": [
           "--directory",
           "c:\\path\\to\\your\\current\\project\\directory\\mcp-tutorial\\",
           "run",
           "main.py"
         ]
       }
     }
   }
   ```

5. Replace `<username>` with your Windows username and update the path to your project directory

6. Save the configuration file

7. Restart Claude Desktop for the changes to take effect

## Troubleshooting

If the MCP tool doesn't appear in Claude Desktop after configuration:

1. Close Claude Desktop completely

2. Check if Claude Desktop is still running in the background:
   - Open Task Manager (Ctrl + Shift + Esc)
   - Look for any "Claude Desktop" processes
   - If found, select them and click "End Task"

3. Verify the configuration file:
   - Make sure the JSON is properly formatted
   - Check that all paths are correct and use double backslashes
   - Ensure the `mcpServers` section is at the root level of the JSON

4. Restart Claude Desktop

5. If the tool still doesn't appear:
   - Check the Windows Event Viewer for any related errors
   - Verify that the UV executable path is correct
   - Ensure the project directory path exists and is accessible

## Project Structure

- `main.py` - Main server implementation
- `pyproject.toml` - Project configuration and dependencies
- `uv.lock` - Lock file for dependency versions

## Dependencies

- bs4 >= 0.0.2
- httpx >= 0.28.1
- mcp[cli] >= 1.9.3

## Notes

- The project requires Python 3.12 or higher
- All dependencies are managed through UV
- The virtual environment is stored in the `.venv` directory
