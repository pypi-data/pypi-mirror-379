"""
MCP Server Implementation using FastMCP with HTTP-SSE
"""

from fastmcp import FastMCP
try:
    from fastmcp.server import Server
except ImportError:
    # Fallback if Server doesn't exist in fastmcp
    Server = None
from typing import List, Dict, Any, Optional
import os
import asyncio
from datetime import datetime
from pymilvus import connections, Collection, utility

# Initialize FastMCP server
mcp = FastMCP("netintel-ocr-mcp")
mcp.description = "NetIntel-OCR Model Context Protocol Server - Read-only access to document data"

# MCPServer class for backward compatibility
class MCPServer:
    """MCP Server wrapper for compatibility."""

    def __init__(self, name: str = "netintel-ocr-mcp"):
        """Initialize MCP Server.

        Args:
            name: Server name
        """
        self.name = name
        self.mcp = mcp
        self.tools = {}

    async def start(self, host: str = "0.0.0.0", port: int = 8000):
        """Start the MCP server.

        Args:
            host: Host to bind to
            port: Port to bind to
        """
        # Mock server start for testing
        return {"status": "started", "host": host, "port": port}

    async def stop(self):
        """Stop the MCP server."""
        return {"status": "stopped"}

    def register_tool(self, name: str, handler):
        """Register a tool with the server.

        Args:
            name: Tool name
            handler: Tool handler function
        """
        self.tools[name] = handler

    async def handle_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Handle an incoming request.

        Args:
            request: Request data

        Returns:
            Response data
        """
        tool_name = request.get("tool")
        parameters = request.get("parameters", {})

        if tool_name in self.tools:
            handler = self.tools[tool_name]
            result = await handler(**parameters) if asyncio.iscoroutinefunction(handler) else handler(**parameters)
            return {"status": "success", "result": result}
        else:
            return {"status": "error", "message": f"Tool {tool_name} not found"}

# Milvus connection
_milvus_connected = False

def get_milvus():
    """Get Milvus connection"""
    global _milvus_connected
    if not _milvus_connected:
        host = os.getenv("MILVUS_HOST", "localhost")
        port = os.getenv("MILVUS_PORT", "19530")
        connections.connect(
            alias="default",
            host=host,
            port=port
        )
        _milvus_connected = True
    return connections

# Tool: Search Documents
@mcp.tool()
async def search_documents(
    query: str,
    limit: int = 10,
    document_type: Optional[str] = None
) -> List[Dict[str, Any]]:
    """
    Search documents by content or metadata
    
    Args:
        query: Search query string
        limit: Maximum number of results (default: 10)
        document_type: Filter by document type (optional)
    
    Returns:
        List of matching documents with metadata
    """
    get_milvus()

    if not utility.has_collection("documents"):
        return []

    collection = Collection("documents")
    collection.load()

    # Perform vector search
    # Note: This is simplified - actual implementation would need embeddings
    results = collection.query(
        expr="",
        limit=limit,
        output_fields=["id", "filename", "content", "metadata"]
    )

    return results

# Tool: Get Document Content
@mcp.tool()
async def get_document_content(
    document_id: str,
    page: Optional[int] = None
) -> Dict[str, Any]:
    """
    Get extracted text content from a document
    
    Args:
        document_id: Document identifier
        page: Specific page number (optional)
    
    Returns:
        Document content with text and metadata
    """
    get_milvus()

    if not utility.has_collection("content"):
        return {"error": "Content not found"}

    collection = Collection("content")
    collection.load()

    if page is not None:
        expr = f"document_id == '{document_id}' && page_number == {page}"
    else:
        expr = f"document_id == '{document_id}'"

    results = collection.query(
        expr=expr,
        output_fields=["document_id", "page_number", "text", "metadata"]
    )
    
    return {
        "document_id": document_id,
        "pages": results,
        "total_pages": len(results)
    }

# Tool: Get Network Diagrams
@mcp.tool()
async def get_network_diagrams(
    document_id: Optional[str] = None,
    device_type: Optional[str] = None,
    limit: int = 10
) -> List[Dict[str, Any]]:
    """
    Get extracted network diagrams
    
    Args:
        document_id: Filter by document ID (optional)
        device_type: Filter by device type (optional)
        limit: Maximum number of results
    
    Returns:
        List of network diagrams with devices and connections
    """
    get_milvus()

    if not utility.has_collection("diagrams"):
        return []

    collection = Collection("diagrams")
    collection.load()

    expr = ""
    if document_id:
        expr = f"document_id == '{document_id}'"

    # TODO: Add device_type filtering

    results = collection.query(
        expr=expr if expr else "",
        limit=limit,
        output_fields=["document_id", "diagram_type", "devices", "connections"]
    )
    
    return results

# Tool: Get Tables
@mcp.tool()
async def get_tables(
    document_id: Optional[str] = None,
    column_name: Optional[str] = None,
    limit: int = 10
) -> List[Dict[str, Any]]:
    """
    Get extracted tables from documents
    
    Args:
        document_id: Filter by document ID (optional)
        column_name: Filter by column name (optional)
        limit: Maximum number of results
    
    Returns:
        List of extracted tables with headers and data
    """
    get_milvus()

    if not utility.has_collection("tables"):
        return []

    collection = Collection("tables")
    collection.load()

    expr = ""
    if document_id:
        expr = f"document_id == '{document_id}'"

    # TODO: Add column_name filtering

    results = collection.query(
        expr=expr if expr else "",
        limit=limit,
        output_fields=["document_id", "table_id", "headers", "data"]
    )
    
    return results

# Tool: Vector Search
@mcp.tool()
async def vector_search(
    query: str,
    collection: str = "content",
    limit: int = 10,
    threshold: float = 0.7
) -> List[Dict[str, Any]]:
    """
    Perform vector similarity search
    
    Args:
        query: Search query text
        collection: Collection to search in
        limit: Maximum number of results
        threshold: Similarity threshold (0-1)
    
    Returns:
        List of similar documents/content with scores
    """
    get_milvus()
    
    if not utility.has_collection(collection):
        return []

    coll = Collection(collection)
    coll.load()
    
    # TODO: Implement actual vector search
    # This requires embedding generation and similarity calculation
    
    return []

# Tool: Get Document Metadata
@mcp.tool()
async def get_document_metadata(
    document_id: str
) -> Dict[str, Any]:
    """
    Get metadata for a specific document
    
    Args:
        document_id: Document identifier
    
    Returns:
        Document metadata including status, dates, and properties
    """
    get_milvus()
    
    if not utility.has_collection("documents"):
        return {"error": "Document not found"}

    collection = Collection("documents")
    collection.load()
    results = collection.query(
        expr=f"document_id == '{document_id}'",
        limit=1,
        output_fields=["document_id", "filename", "status", "metadata"]
    )
    
    if not results:
        return {"error": "Document not found"}
    
    return results[0]

# Tool: List Documents
@mcp.tool()
async def list_documents(
    skip: int = 0,
    limit: int = 20,
    status: Optional[str] = None
) -> Dict[str, Any]:
    """
    List all documents with pagination
    
    Args:
        skip: Number of documents to skip
        limit: Maximum number of documents to return
        status: Filter by document status
    
    Returns:
        Paginated list of documents
    """
    get_milvus()
    
    if not utility.has_collection("documents"):
        return {"documents": [], "total": 0}

    collection = Collection("documents")
    collection.load()

    expr = ""
    if status:
        expr = f"status == '{status}'"

    # Note: Milvus doesn't have native offset, so we need to work around it
    actual_limit = skip + limit
    all_results = collection.query(
        expr=expr if expr else "",
        limit=actual_limit,
        output_fields=["document_id", "filename", "status", "metadata"]
    )
    results = all_results[skip:skip+limit] if skip < len(all_results) else []
    
    return {
        "documents": results,
        "total": len(results),
        "skip": skip,
        "limit": limit
    }

# Tool: Get Statistics
@mcp.tool()
async def get_statistics() -> Dict[str, Any]:
    """
    Get database statistics and metrics
    
    Returns:
        Statistics about documents, processing, and storage
    """
    get_milvus()
    
    stats = {
        "timestamp": datetime.utcnow().isoformat(),
        "collections": {}
    }
    
    for collection_name in utility.list_collections():
        collection = Collection(collection_name)
        collection.load()
        stats["collections"][collection_name] = {
            "count": collection.num_entities
        }
    
    return stats

# Resource: Document Collection
@mcp.resource("documents://list")
async def list_documents_resource() -> str:
    """List all available documents"""
    result = await list_documents(limit=100)
    return f"Total documents: {result['total']}\\n" + \
           "\\n".join([f"- {d['document_id']}: {d.get('filename', 'Unknown')}" 
                     for d in result['documents']])

# Resource: Network Diagrams
@mcp.resource("diagrams://list")
async def list_diagrams_resource() -> str:
    """List all network diagrams"""
    diagrams = await get_network_diagrams(limit=100)
    return f"Total diagrams: {len(diagrams)}\\n" + \
           "\\n".join([f"- Diagram {d['diagram_id']} (Page {d.get('page_number', 'N/A')})" 
                     for d in diagrams])

# Resource: Tables
@mcp.resource("tables://list")
async def list_tables_resource() -> str:
    """List all extracted tables"""
    tables = await get_tables(limit=100)
    return f"Total tables: {len(tables)}\\n" + \
           "\\n".join([f"- Table {t['table_id']} (Page {t.get('page_number', 'N/A')})" 
                     for t in tables])

# Prompt: Network Analysis
@mcp.prompt()
async def network_analysis_prompt(document_id: str) -> str:
    """
    Generate a prompt for network infrastructure analysis
    
    Args:
        document_id: Document to analyze
    
    Returns:
        Analysis prompt with context
    """
    content = await get_document_content(document_id)
    diagrams = await get_network_diagrams(document_id)
    tables = await get_tables(document_id)
    
    prompt = f"""Analyze the network infrastructure documentation:

Document ID: {document_id}
Pages: {content.get('total_pages', 0)}
Diagrams: {len(diagrams)}
Tables: {len(tables)}

Please provide:
1. Network topology overview
2. Key components and their relationships
3. Security considerations
4. Potential improvements
"""
    
    return prompt

# Prompt: Table Summary
@mcp.prompt()
async def table_summary_prompt(document_id: str) -> str:
    """
    Generate a prompt for table data summarization
    
    Args:
        document_id: Document containing tables
    
    Returns:
        Summary prompt with table context
    """
    tables = await get_tables(document_id)
    
    prompt = f"""Summarize the following {len(tables)} tables:

"""
    
    for table in tables[:5]:  # Limit to first 5 tables
        prompt += f"Table {table['table_id']}:\\n"
        prompt += f"Headers: {', '.join(table.get('headers', []))}\\n"
        prompt += f"Rows: {len(table.get('rows', []))}\\n\\n"
    
    prompt += """
Please provide:
1. Key data patterns
2. Important relationships
3. Notable findings
"""
    
    return prompt

def create_app():
    """Create FastMCP application"""
    return mcp.get_app()

if __name__ == "__main__":
    import uvicorn
    
    # Configuration from environment
    host = os.getenv("MCP_HOST", "0.0.0.0")
    port = int(os.getenv("MCP_PORT", "8001"))
    
    # Run server
    uvicorn.run(
        create_app(),
        host=host,
        port=port,
        log_level="info"
    )