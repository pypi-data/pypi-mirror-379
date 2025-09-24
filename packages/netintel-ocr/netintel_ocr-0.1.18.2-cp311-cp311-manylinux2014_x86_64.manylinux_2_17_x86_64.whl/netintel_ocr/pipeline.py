"""
PDF Processing Pipeline
End-to-end pipeline for PDF extraction, chunking, embedding, and search
"""

import asyncio
from pathlib import Path
from typing import Dict, List, Any, Optional
import logging
import time

from .services.pdf_extractor import PDFExtractor
from .services.text_chunker import TextChunker

logger = logging.getLogger(__name__)


class PDFProcessingPipeline:
    """Complete PDF processing pipeline."""

    def __init__(
        self,
        model: str = "Nanonets-OCR-s:latest",
        ollama_host: str = "http://localhost:11434",
        milvus_host: str = "localhost",
        milvus_port: int = 19530,
        collection_name: str = "documents",
        retry_count: int = 3,
        retry_delay: int = 1
    ):
        """Initialize pipeline.

        Args:
            model: Model to use for extraction
            ollama_host: Ollama server URL
            milvus_host: Milvus host
            milvus_port: Milvus port
            collection_name: Vector collection name
            retry_count: Number of retries for failed operations
            retry_delay: Delay between retries
        """
        self.model = model
        self.ollama_host = ollama_host
        self.milvus_host = milvus_host
        self.milvus_port = milvus_port
        self.collection_name = collection_name
        self.retry_count = retry_count
        self.retry_delay = retry_delay

        # Initialize components
        self.extractor = PDFExtractor(model=model, ollama_host=ollama_host)
        self.chunker = TextChunker()

    async def extract_pdf(
        self,
        pdf_path: str,
        extract_images: bool = True,
        extract_tables: bool = True,
        extract_diagrams: bool = True
    ) -> Dict[str, Any]:
        """Extract content from PDF.

        Args:
            pdf_path: Path to PDF file
            extract_images: Extract images
            extract_tables: Extract tables
            extract_diagrams: Extract diagrams

        Returns:
            Extraction results
        """
        return await self.extractor.extract(
            pdf_path=pdf_path,
            extract_images=extract_images,
            extract_tables=extract_tables,
            extract_diagrams=extract_diagrams
        )

    async def chunk_text(
        self,
        text: str,
        chunk_size: int = 512,
        chunk_overlap: int = 50
    ) -> List[Dict[str, Any]]:
        """Chunk text for processing.

        Args:
            text: Text to chunk
            chunk_size: Target chunk size
            chunk_overlap: Overlap between chunks

        Returns:
            List of chunks
        """
        chunker = TextChunker(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        return chunker.chunk(text)

    async def generate_embeddings(
        self,
        texts: List[str],
        batch_size: int = 32
    ) -> List[List[float]]:
        """Generate embeddings for texts.

        Args:
            texts: List of texts to embed
            batch_size: Batch size for processing

        Returns:
            List of embeddings
        """
        # Mock embedding generation
        # In production, this would call Ollama or another embedding service
        embeddings = []
        for text in texts:
            # Generate mock embedding (768 dimensions)
            embedding = [0.1] * 768
            # Make it slightly different based on text length
            embedding[0] = len(text) / 1000
            embeddings.append(embedding)

        # Simulate processing time
        await asyncio.sleep(len(texts) * 0.01)

        return embeddings

    async def store_vectors(
        self,
        chunks: List[Dict[str, Any]],
        embeddings: List[List[float]],
        metadata: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Store vectors in Milvus.

        Args:
            chunks: Text chunks
            embeddings: Embeddings for chunks
            metadata: Additional metadata

        Returns:
            Storage result
        """
        # Validate embeddings dimension
        expected_dim = 768  # Standard dimension for mock embeddings
        for idx, embedding in enumerate(embeddings):
            if len(embedding) != expected_dim:
                raise ValueError(
                    f"Invalid embedding dimension at index {idx}: "
                    f"expected {expected_dim}, got {len(embedding)}"
                )

        # Mock vector storage
        # In production, this would use Milvus client

        result = {
            "success": True,
            "count": len(chunks),
            "collection": self.collection_name,
            "metadata": metadata or {}
        }

        # Simulate storage time
        await asyncio.sleep(len(chunks) * 0.005)

        return result

    async def search(
        self,
        query: str,
        top_k: int = 5,
        filters: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """Search for similar content.

        Args:
            query: Search query
            top_k: Number of results
            filters: Optional filters

        Returns:
            Search results
        """
        # Generate query embedding
        query_embedding = await self.generate_embeddings([query])

        # Mock search results
        results = []
        for i in range(min(top_k, 5)):
            results.append({
                "text": f"Result {i+1}: Content related to '{query}'",
                "score": 0.95 - (i * 0.1),
                "metadata": {
                    "page": i + 1,
                    "source": "cisco-sdwan.pdf"
                }
            })

        # Simulate search time
        await asyncio.sleep(0.1)

        return results

    async def process_complete(
        self,
        pdf_path: str,
        chunk_size: int = 512,
        extract_images: bool = True,
        extract_tables: bool = True
    ) -> Dict[str, Any]:
        """Run complete processing pipeline.

        Args:
            pdf_path: Path to PDF file
            chunk_size: Chunk size for text
            extract_images: Extract images
            extract_tables: Extract tables

        Returns:
            Processing results
        """
        start_time = time.time()
        results = {}

        # Extract PDF
        extraction = await self.extract_pdf(
            pdf_path=pdf_path,
            extract_images=extract_images,
            extract_tables=extract_tables
        )
        results["extraction"] = extraction

        # Chunk text
        chunks = await self.chunk_text(
            text=extraction["markdown"],
            chunk_size=chunk_size
        )
        results["chunks_count"] = len(chunks)

        # Generate embeddings
        texts = [chunk["text"] for chunk in chunks]
        embeddings = await self.generate_embeddings(texts)
        results["embeddings_generated"] = len(embeddings)

        # Store vectors
        storage_result = await self.store_vectors(
            chunks=chunks,
            embeddings=embeddings,
            metadata={"source": pdf_path}
        )
        results["vectors_stored"] = storage_result["count"]

        # Calculate processing time
        results["processing_time"] = time.time() - start_time
        results["success"] = True

        return results