from mcp.server.fastmcp import FastMCP

from amsdal_ml.agents.retriever_tool import retriever_search

server = FastMCP('retriever-stdio')
server.tool(
    name='retriever.search',
    description='Semantic search in knowledge base (OpenAI embeddings)',
    structured_output=True,
)(retriever_search)
server.run(transport='stdio')
