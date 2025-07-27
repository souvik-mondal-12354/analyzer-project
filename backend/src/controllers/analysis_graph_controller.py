from models.analysis_graph import AnalysisGraph
from db import engine

async def create_analysis_graph(analysis_graph: AnalysisGraph):
    created_graph = await engine.save(analysis_graph)
    return created_graph