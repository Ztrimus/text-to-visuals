from typing import List, Optional, Literal, Dict, Any
from pydantic import BaseModel, Field

DiagramType = Literal["flowchart", "timeline", "mind_map", "table"]


class Node(BaseModel):
    id: str
    label: str
    type: Optional[str] = None
    props: Dict[str, Any] = Field(default_factory=dict)


class Edge(BaseModel):
    source: str
    target: str
    label: Optional[str] = None
    condition: Optional[str] = None
    props: Dict[str, Any] = Field(default_factory=dict)


class GraphData(BaseModel):
    nodes: List[Node]
    edges: List[Edge]


class TimelineEvent(BaseModel):
    id: str
    label: str
    time: str
    props: Dict[str, Any] = Field(default_factory=dict)


class TimelineData(BaseModel):
    events: List[TimelineEvent]


class MindMapData(BaseModel):
    root: Node
    children: List[Node]
    edges: List[Edge]


class Diagram(BaseModel):
    type: DiagramType
    data: Dict[str, Any]
    meta: Dict[str, Any] = Field(default_factory=dict)
