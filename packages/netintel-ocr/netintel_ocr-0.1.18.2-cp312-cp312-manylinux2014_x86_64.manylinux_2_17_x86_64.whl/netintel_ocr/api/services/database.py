"""
Database Service - Milvus connection management
"""

import os
from pymilvus import connections, utility
from typing import Optional
import asyncio

_milvus_connected: bool = False

async def init_database():
    """Initialize Milvus connection"""
    global _milvus_connected

    host = os.getenv("MILVUS_HOST", "localhost")
    port = os.getenv("MILVUS_PORT", "19530")

    # Connect to Milvus
    await asyncio.to_thread(
        connections.connect,
        alias="default",
        host=host,
        port=port
    )

    _milvus_connected = True
    print(f"Connected to Milvus at {host}:{port}")

async def close_database():
    """Close database connection"""
    global _milvus_connected
    if _milvus_connected:
        connections.disconnect("default")
        _milvus_connected = False
        print("Database connection closed")

async def check_database_connection() -> bool:
    """Check if database is connected"""
    try:
        return _milvus_connected and utility.list_collections() is not None
    except:
        return False

def get_db():
    """Get database connection status"""
    if not _milvus_connected:
        raise RuntimeError("Database not initialized")
    return connections