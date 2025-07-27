from typing import List
from fastapi import APIRouter, Path, Query
import controllers.analysis_graph_controller as controller
from models.analysis_graph import AnalysisGraph

analysis_graph_router = APIRouter()

@analysis_graph_router.post('/')
async def create_analysis_graph(analysis_graph: AnalysisGraph) -> AnalysisGraph:
    created_graph = await controller.create_analysis_graph(analysis_graph)
    return created_graph

@analysis_graph_router.get('/')
async def get_analysis_graphs(
    skip: int = Query(0, ge=0, description="Number of items to skip"),
    limit: int = Query(100, ge=1, le=1000, description="Number of items to return")
) -> List[AnalysisGraph]:
    analysis_graphs = await controller.get_all_analysis_graphs(
        skip=skip,
        limit=limit
    )

    return analysis_graphs

@analysis_graph_router.put('/{graph_id}')
async def update_analysis_graph(
    update_data: AnalysisGraph,
    graph_id: int = Path(..., description="ID of the analysis graph")
) -> AnalysisGraph:
    updated_graph = await controller.update_analysis_graph(
        graph_id=graph_id,
        updated_data=update_data
    )

    return updated_graph

@analysis_graph_router.delete('/{graph_id}')
async def delete_analysis_graph(
    graph_id: int = Path(..., description="ID of the analysis graph to delete")
) -> bool:
    deleted_graph = await controller.delete_analysis_graph_by_id(graph_id)
    return deleted_graph