# MCP Tutorial

This project uses UV for Python environment management and runs an MCP server that fetches latest documentation for libraries like llamaindex or langchain.



## Prerequisites

- Python 3.12 or higher
- UV package manager

## Setup Instructions

1. Install UV if you haven't already and initialize a new project:
   ```bash
   uv init
   ```

2. Activate a virtual environment using uv:
   ```bash
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies in pyproject.toml using uv:
   ```bash
   uv sync
   ```

## Running the MCP Server
The mcp server is defined in `main.py`
1. Make sure your virtual environment is activated:
   ```bash
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Run the MCP server, to test it locally:
   ```bash
   uv run main.py
   ```

## Accessing the MCP Server from Claude Desktop

1. Open Claude Desktop application

2. Go to Developer Settings (you can access this through the settings menu)

3. Locate the configuration file at:
   ```
   %APPDATA%\Claude\claude_desktop_config.json
   ```
   (On Windows, this is typically at `C:\Users\<username>\AppData\Roaming\Claude\claude_desktop_config.json`)

4. Add or modify the `mcpServers` section in the configuration file. The command should be absolute path of `uv` executable, and the --directory option should be the absolute path of your project directory. 

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

If the MCP tool (defined in your main.py) doesn't appear in Claude Desktop after configuration:

1. Close Claude Desktop application completely

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
   - Check the claude logs (accessible through developer settings) or  Windows Event Viewer for any related errors.
   - Verify that the uv executable path is correct
   - Ensure the project directory path exists and is accessible

## Selecting theCustom MCP Server  in Claud Desktop 
When properly configured, your MCP server (e.g., `sk-docs-server`) will appear in Claude Desktop which is acting as MCP client. Here's what to expect:

1. **Accessing the Tool:**
   - Open Claude Desktop.
   - Click the settings icon next to the chat input to open the tools/search menu.

2. **Selecting the MCP Server:**
   - In the search menu, you should see your MCP server listed (e.g., `sk-docs-server`).
   - Example:
     
     ![Select MCP Server](select_mcp.png)

3. **Viewing the MCP Tool:**
   - After selecting or enabling the MCP server, the available MCP tool(s) (such as `get_latest_docs`) will be accessible.
   - Example:
     
     ![MCP Tool in Menu](tool.png)

4. **In-Chat Appearance:**
   - When the tool is enabled, it will be available for use in your chat session.
   - Example:
     
     ![MCP Server in Claude Desktop](image.png)

You should see your custom tool (like `get_latest_docs`) listed and ready to use.

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

## How Claude Desktop Uses Your MCP Server

When you ask a question related to LangChain, LlamaIndex, or OpenAI (for example, "How to create a custom chat model in langchain?"), Claude Desktop will use your enabled MCP server to fetch and display the answer.

Below is an example of Claude Desktop using the MCP tool to answer such a question:

![Claude Desktop using MCP tool](claud-using-mcp-tool.png)
