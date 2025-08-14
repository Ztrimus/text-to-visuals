import os
from server.utils.logger import get_logger
from pydantic import ValidationError
from server.schemas.diagram import Diagram, GraphData, TimelineData, MindMapData

logger = get_logger(os.path.basename(__file__))


def validate(diagram_dict: dict) -> Diagram:
    try:
        logger.info(f"Validating diagram dict: {diagram_dict}")
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
        logger.info("Diagram validated successfully.")
        return d
    except (TypeError, AssertionError, ValueError) as e:
        logger.error(f"Error creating diagram: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error during diagram validation: {e}")
        raise
