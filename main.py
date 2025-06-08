from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import httpx
import os
import asyncio
from bs4 import BeautifulSoup


load_dotenv()

mcp = FastMCP("sk-docs-server")
USER_AGENT = "sk-docs-app/1.0"
SERPER_URL = "https://google.serper.dev/search"

docs_urls = {
    "langchain": "python.langchain.com/docs",
    "llama-index": "docs.llamaindex.ai/en/stable",
    "openai": "platform.openai.com/docs",
}

"""
3 methods to get docs:
1. search_web
2. fetch_url
3. get_docs
    this is the mcp tool that llm can use to get docs
"""


async def search_web(query: str) -> dict | None:
    """
    Search the web for the most relevant information about the query in the form of urls
    returns search results in a dictionary
    """
    headers = {
        "X-API-KEY": os.getenv("SERPER_API_KEY"),
        "Content-Type": "application/json",
    }
    payload = {
        "q": query,
        "num": 2
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(SERPER_URL, headers=headers, params=payload, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            return f"Error: {e}"
        except httpx.RequestError as e:
            return f"Error: {e}"
        except httpx.TimeoutException:
            return {"organic": []}


async def fetch_url(url: str):
    """
    Fetch the content of the url
    """
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers={"User-Agent": USER_AGENT}, timeout=30.0)
            soup = BeautifulSoup(response.text, "html.parser")
            text = soup.get_text()
            return text
        except httpx.TimeoutException:
            return "Timeout Error"


@mcp.tool()
async def get_latest_docs(query: str, library: str):
    """
    Search the web for given query and library.
    Supports anthropic  and Google's Vertex AI documentations

    Args:
        query: The query to search for ( for example "how to add a new model to mcp")
        library: The library to search for ( for example "anthropic")

    Returns:
        extracted text from the documentation related to the query and library
    """
    if library not in docs_urls:
        raise ValueError(f"Library {library} not supported")

    # Appending "site" to a search query, typically using the format "site:domain.com", tells the search engine to limit the search results to a specific website
    query = f"site:{docs_urls[library]} {query}"
    search_results = await search_web(query)
    if len(search_results["organic"]) == 0:
        return "No Results Found"

    text = ""
    for result in search_results["organic"]:
        text += await fetch_url(result["link"])
    return text

if __name__ == "__main__":
    mcp.run(transport="stdio")
