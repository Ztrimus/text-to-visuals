from pydantic import ValidationError
from .models import Diagram, GraphData, TimelineData, MindMapData


def validate(diagram_dict: dict) -> Diagram:
    d = Diagram(**diagram_dict)
    t = d.type
    if t == "flowchart":
        GraphData(**d.data)
    elif t == "timeline":
        TimelineData(**d.data)
    elif t == "mind_map":
        MindMapData(**d.data)
    elif t == "table":
        # very simple: expect headers/rows
        assert "headers" in d.data and "rows" in d.data
    else:
        raise ValueError(f"Unsupported type: {t}")
    return d
