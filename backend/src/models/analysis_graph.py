from typing import List, Dict, Any, Optional, TypedDict
from odmantic import Model, Field

class NodeDict(TypedDict):
    """Node structure for the graph"""
    id: str
    label: str
    type: Optional[str]
    properties: Optional[Dict[str, Any]]

class EdgeDict(TypedDict):
    """Edge structure for the graph"""
    id: str
    source: str
    target: str
    label: Optional[str]
    type: Optional[str]
    properties: Optional[Dict[str, Any]]

class GraphDict(TypedDict):
    """Graph structure containing nodes and edges"""
    nodes: List[NodeDict]
    edges: List[EdgeDict]

class AnalysisGraph(Model):
    name: str
    desc: Optional[str]
    graph: GraphDict = Field(default_factory=lambda: {"nodes": [], "edges": []})