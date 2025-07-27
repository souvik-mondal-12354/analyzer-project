from typing import List, Optional
from models.analysis_graph import AnalysisGraph
from db import engine

# CREATE
async def create_analysis_graph(analysis_graph: AnalysisGraph) -> AnalysisGraph:
    """Create a new analysis graph."""
    created_graph = await engine.save(analysis_graph)
    return created_graph

# READ
async def get_analysis_graph_by_id(graph_id: int) -> Optional[AnalysisGraph]:
    """Get an analysis graph by its ID."""
    analysis_graph = await engine.find(AnalysisGraph, graph_id)
    return analysis_graph

async def get_all_analysis_graphs(
    skip: int = 0, 
    limit: int = 100,
    filters: Optional[dict] = None
) -> List[AnalysisGraph]:
    """Get all analysis graphs with optional pagination and filtering."""
    query_params = {"skip": skip, "limit": limit}
    if filters:
        query_params.update(filters)
    
    analysis_graphs = await engine.find_all(AnalysisGraph, **query_params)
    return analysis_graphs

# UPDATE
async def update_analysis_graph(graph_id: int, update_graph: AnalysisGraph) -> Optional[AnalysisGraph]:
    """Update an existing analysis graph."""
    # First, get the existing graph
    existing_graph = await engine.find(AnalysisGraph, graph_id)
    if not existing_graph:
        return None
    
    # Update the fields
    for field, value in updated_graph.items():
        if hasattr(existing_graph, field):
            setattr(existing_graph, field, value)
    
    # Save the updated graph
    updated_graph = await engine.save(existing_graph)
    return updated_graph

# DELETE

async def delete_analysis_graph_by_id(graph_id: int) -> bool:
    """Delete an analysis graph directly by ID (if engine supports it)."""
    result = await engine.delete_by_id(AnalysisGraph, graph_id)
    return result
