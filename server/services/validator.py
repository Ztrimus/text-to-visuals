import os
from server.utils.logger import get_logger
from server.schemas.diagram import Diagram, GraphData, TimelineData, MindMapData

logger = get_logger(os.path.basename(__file__))


def validate(diagram_dict: dict) -> Diagram:
    try:
        logger.info("Validating diagram ...")
        # Accept both dict and Diagram
        if isinstance(diagram_dict, Diagram):
            d = diagram_dict
        else:
            d = Diagram(**diagram_dict)
        t = d.type
        # Pre-validation for edges and mind_map root
        if t in ["flowchart", "mind_map"]:
            edges = d.data.get("edges", [])
            filtered_edges = []
            for idx, edge in enumerate(edges):
                # Accept both dict and Edge instance
                src = (
                    getattr(edge, "source", None)
                    if hasattr(edge, "source")
                    else edge.get("source")
                )
                tgt = (
                    getattr(edge, "target", None)
                    if hasattr(edge, "target")
                    else edge.get("target")
                )
                if not src or not tgt:
                    logger.warning(
                        "Dropping edge at index %d: missing 'source' or 'target'. Edge: %s",
                        idx,
                        edge,
                    )
                else:
                    filtered_edges.append(edge)
            d.data["edges"] = filtered_edges
        if t == "mind_map":
            root = d.data.get("root", {})
            # Accept both dict and Node instance
            root_id = (
                getattr(root, "id", None) if hasattr(root, "id") else root.get("id")
            )
            if not root_id:
                logger.warning(
                    "MindMap root node missing 'id'. Setting to 'root'. Root: %s", root
                )
                if isinstance(root, dict):
                    root["id"] = "root"
                else:
                    root.id = "root"
                d.data["root"] = root
                # Fix children field if missing but nodes exists
                if "children" not in d.data and "nodes" in d.data:
                    logger.warning(
                        "MindMapData missing 'children' field, using 'nodes' instead. nodes: %s",
                        d.data["nodes"],
                    )
                    d.data["children"] = d.data["nodes"]
                    del d.data["nodes"]
                # Ensure every child node has a label
                children = d.data.get("children", [])
                for idx, child in enumerate(children):
                    label = (
                        getattr(child, "label", None)
                        if hasattr(child, "label")
                        else child.get("label")
                    )
                    if not label:
                        default_label = (
                            getattr(child, "id", None)
                            if hasattr(child, "id")
                            else child.get("id", "Untitled")
                        )
                        logger.warning(
                            "MindMap child node at index %d missing 'label'. Setting to id: %s",
                            idx,
                            default_label,
                        )
                        if isinstance(child, dict):
                            child["label"] = default_label
                        else:
                            child.label = default_label
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
        logger.error("Error creating diagram: %s", e)
        raise
    except Exception as e:
        logger.error("Unexpected error during diagram validation: %s", e)
        raise
