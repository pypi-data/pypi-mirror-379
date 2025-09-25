#!/usr/bin/env python3
"""
AWS Blogs MCP Server - Fixed Version

A Model Context Protocol server that provides access to AWS blog content.
"""

import asyncio
import logging
from typing import Any, Dict, List, Optional
import json

import httpx
from bs4 import BeautifulSoup
from mcp.server import Server
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server
from mcp.server.lowlevel import NotificationOptions
from mcp.types import Tool, TextContent
import mcp.types as types

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("aws-blogs-mcp-server")

class AWSBlogsServer:
    """AWS Blogs search server."""
    
    def __init__(self):
        self.client = httpx.AsyncClient(
            timeout=30.0,
            headers={
                "User-Agent": "Mozilla/5.0 (compatible; AWS-Blogs-MCP-Server/1.0)"
            }
        )
    
    async def close(self):
        """Clean up resources."""
        await self.client.aclose()
    
    async def search_blogs(self, query: str, category: Optional[str] = None, limit: int = 10) -> List[Dict[str, Any]]:
        """Search AWS blogs."""
        try:
            logger.info(f"Searching for: '{query}' in category: {category}")
            
            # Simple search using the main blogs page
            search_url = f"https://aws.amazon.com/blogs/?s={query}" if query else "https://aws.amazon.com/blogs/"
            
            response = await self.client.get(search_url)
            if response.status_code != 200:
                logger.error(f"Failed to fetch {search_url}: {response.status_code}")
                return []
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find blog post links
            blog_posts = []
            
            # Look for blog post containers
            post_containers = soup.find_all(['article', 'div'], class_=lambda x: x and any(
                term in x.lower() for term in ['post', 'blog', 'article', 'entry']
            ))
            
            for container in post_containers[:limit]:
                # Find title and link
                title_elem = container.find(['h1', 'h2', 'h3', 'h4'], class_=lambda x: x and 'title' in x.lower())
                if not title_elem:
                    title_elem = container.find(['h1', 'h2', 'h3', 'h4'])
                
                link_elem = title_elem.find('a') if title_elem else container.find('a')
                
                if title_elem and link_elem:
                    title = title_elem.get_text(strip=True)
                    url = link_elem.get('href', '')
                    
                    # Make URL absolute
                    if url.startswith('/'):
                        url = f"https://aws.amazon.com{url}"
                    
                    # Find excerpt
                    excerpt_elem = container.find(['p', 'div'], class_=lambda x: x and 'excerpt' in x.lower())
                    if not excerpt_elem:
                        excerpt_elem = container.find('p')
                    
                    excerpt = excerpt_elem.get_text(strip=True)[:200] + "..." if excerpt_elem else ""
                    
                    blog_posts.append({
                        'title': title,
                        'url': url,
                        'excerpt': excerpt,
                        'date': 'N/A'
                    })
            
            # If no structured posts found, try a different approach
            if not blog_posts:
                # Look for any links that might be blog posts
                links = soup.find_all('a', href=True)
                for link in links[:limit]:
                    href = link.get('href', '')
                    if '/blogs/' in href and href not in [post['url'] for post in blog_posts]:
                        title = link.get_text(strip=True)
                        if title and len(title) > 10:  # Filter out short/empty titles
                            if href.startswith('/'):
                                href = f"https://aws.amazon.com{href}"
                            
                            blog_posts.append({
                                'title': title,
                                'url': href,
                                'excerpt': 'No excerpt available',
                                'date': 'N/A'
                            })
            
            logger.info(f"Found {len(blog_posts)} blog posts")
            return blog_posts[:limit]
            
        except Exception as e:
            logger.error(f"Error searching blogs: {e}")
            return []

# Create the MCP server
app = Server("aws-blogs-mcp-server")
blogs_server = AWSBlogsServer()

@app.list_tools()
async def handle_list_tools() -> List[Tool]:
    """List available tools."""
    return [
        Tool(
            name="search_aws_blogs",
            description="Search AWS blogs for posts matching a query",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query for blog posts"
                    },
                    "category": {
                        "type": "string",
                        "description": "Optional blog category to search in"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Maximum number of results to return",
                        "default": 10
                    }
                },
                "required": ["query"]
            }
        )
    ]

@app.call_tool()
async def handle_call_tool(name: str, arguments: dict) -> List[types.TextContent]:
    """Handle tool calls."""
    try:
        if name == "search_aws_blogs":
            query = arguments.get("query", "")
            category = arguments.get("category")
            limit = arguments.get("limit", 10)
            
            logger.info(f"Tool call: search_aws_blogs with query='{query}', category={category}, limit={limit}")
            
            results = await blogs_server.search_blogs(query, category, limit)
            
            if not results:
                return [types.TextContent(
                    type="text",
                    text=f"No blog posts found for query: '{query}'"
                )]
            
            # Format results
            formatted_results = []
            for i, post in enumerate(results, 1):
                formatted_results.append(
                    f"{i}. **{post['title']}**\n"
                    f"   URL: {post['url']}\n"
                    f"   Excerpt: {post.get('excerpt', 'No excerpt available')}\n"
                )
            
            response_text = f"Found {len(results)} AWS blog posts for '{query}':\n\n" + "\n".join(formatted_results)
            
            return [types.TextContent(
                type="text",
                text=response_text
            )]
        
        else:
            return [types.TextContent(
                type="text",
                text=f"Unknown tool: {name}"
            )]
            
    except Exception as e:
        logger.error(f"Error in tool call {name}: {e}")
        return [types.TextContent(
            type="text",
            text=f"Error executing {name}: {str(e)}"
        )]

async def main():
    """Main entry point."""
    try:
        async with stdio_server() as (read_stream, write_stream):
            await app.run(
                read_stream,
                write_stream,
                InitializationOptions(
                    server_name="aws-blogs-mcp-server",
                    server_version="1.0.1",
                    capabilities=app.get_capabilities(
                        notification_options=NotificationOptions(
                            tools_changed=False,
                            resources_changed=False,
                            prompts_changed=False,
                        ),
                        experimental_capabilities={},
                    ),
                ),
            )
    finally:
        await blogs_server.close()

if __name__ == "__main__":
    asyncio.run(main())
