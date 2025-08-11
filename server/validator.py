from pydantic import ValidationError
from server.schemas.diagram import Diagram, GraphData, TimelineData, MindMapData


def validate(diagram_dict: dict) -> Diagram:
    try:
        # Accept both dict and Diagram
        if isinstance(diagram_dict, Diagram):
            d = diagram_dict
        else:
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
    except (TypeError, AssertionError, ValueError) as e:
        print(f"Error creating diagram: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error during diagram validation: {e}")
        raise
