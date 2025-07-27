from fastapi import APIRouter
import controllers.analysis_graph_controller as controller
from models.analysis_graph import AnalysisGraph

analysis_graph_router = APIRouter()

@analysis_graph_router.post('/')
async def create_analysis_graph(analysis_graph: AnalysisGraph) -> AnalysisGraph:
    created_graph = await controller.create_analysis_graph(analysis_graph)
    return created_graph