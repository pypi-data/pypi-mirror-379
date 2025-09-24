from __future__ import annotations

from typing import Any
from typing import Optional

from mcp.server.fastmcp.tools.base import Tool
from pydantic import BaseModel
from pydantic import Field

from amsdal_ml.ml_retrievers.openai_retriever import OpenAIRetriever


class RetrieverArgs(BaseModel):
    query: str = Field(..., description='User search query')
    k: int = 5
    include_tags: Optional[list[str]] = None
    exclude_tags: Optional[list[str]] = None


_retriever = OpenAIRetriever()


async def retriever_search(args: RetrieverArgs) -> list[dict[str, Any]]:
    chunks = await _retriever.asimilarity_search(
        query=args.query,
        k=args.k,
        include_tags=args.include_tags,
        exclude_tags=args.exclude_tags,
    )
    out: list[dict[str, Any]] = []
    for c in chunks:
        if hasattr(c, 'model_dump'):
            out.append(c.model_dump())
        elif hasattr(c, 'dict'):
            out.append(c.dict())
        elif isinstance(c, dict):
            out.append(c)
        else:
            out.append({'raw_text': str(c)})
    return out


retriever_tool = Tool.from_function(
    retriever_search,
    name='retriever.search',
    description='Semantic search in knowledge base (OpenAI embeddings)',
    structured_output=True,
)
