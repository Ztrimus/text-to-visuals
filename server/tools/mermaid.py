import re
from server.schemas.diagram import Diagram, GraphData, TimelineData, MindMapData

# List of reserved words in Mermaid
MERMAID_RESERVED_WORDS = {
    "graph",
    "flowchart",
    "sequenceDiagram",
    "classDiagram",
    "stateDiagram",
    "journey",
    "gitgraph",
    "pie",
    "timeline",
    "mindmap",
    "click",
    "style",
    "classDef",
    "linkStyle",
    "subgraph",
    "end",
    "direction",
    "TB",
    "TD",
    "BT",
    "RL",
    "LR",
    "true",
    "false",
    "null",
}


@staticmethod
def sanitize_id(node_id: str) -> str:
    """Sanitize node ID to be Mermaid-compatible."""
    if not node_id:
        return "node_empty"

    # Replace spaces and special characters with underscores
    sanitized = re.sub(r"[^a-zA-Z0-9_]", "_", node_id)

    # Ensure it doesn't start with a number
    if sanitized and sanitized[0].isdigit():
        sanitized = f"node_{sanitized}"

    # Handle reserved keywords
    if sanitized.lower() in MERMAID_RESERVED_WORDS:
        sanitized = f"{sanitized}_node"

    # Ensure it's not empty after sanitization
    return sanitized if sanitized else "node_default"


@staticmethod
def sanitize_label(label: str) -> str:
    """Sanitize label text for Mermaid compatibility."""
    if not label:
        return "Untitled"

    # Escape quotes and handle special characters
    sanitized = label.replace('"', '\\"').replace("\n", "<br>").replace("\r", "")

    # Limit length to prevent rendering issues
    if len(sanitized) > 100:
        sanitized = sanitized[:97] + "..."

    return sanitized


def fix_mermaid_string(mermaid_str: str) -> str:
    """Fix common Mermaid string issues like escaped newlines."""
    # Fix the main issue: escaped newlines
    fixed = mermaid_str.replace("\\n", "\n")
    return fixed


def to_mermaid(diagram: Diagram) -> str:
    t = diagram.type
    meta = diagram.meta or {}
    if t == "flowchart":
        g = GraphData(**diagram.data)
        direction = meta.get("direction", "TD")
        lines = [f"flowchart {direction}"]
        # Sanitize node IDs
        node_id_map = {}
        for n in g.nodes:
            safe_id = sanitize_id(n.id)
            node_id_map[n.id] = safe_id
            lines.append(f'{safe_id}["{n.label}"]')
        for e in g.edges:
            src = node_id_map.get(e.source, sanitize_id(e.source))
            tgt = node_id_map.get(e.target, sanitize_id(e.target))
            if e.label:
                safe_label = sanitize_label(e.label)
                lines.append(f'{src} --"{safe_label}"--> {tgt}')
            else:
                lines.append(f"{src} --> {tgt}")
        return "\n".join(lines)

    if t == "timeline":
        tl = TimelineData(**diagram.data)
        lines = ["timeline"]
        title = meta.get("title")
        if title:
            lines.append(f"title {title}")
        for ev in tl.events:
            lines.append(f"{ev.time} : {ev.label}")
        return "\n".join(lines)

    if t == "mind_map":
        mm = MindMapData(**diagram.data)
        lines = ["mindmap"]
        lines.append(f"root(({mm.root.label}))")
        # map child IDs to labels for readability
        for child in mm.children:
            lines.append(f"{child.id}({child.label})")
        for e in mm.edges:
            # only support root->child for now
            if e.source == "root":
                lines.append(f"root --> {e.target}")
        return "\n".join(lines)

    if t == "table":
        headers = diagram.data["headers"]
        rows = diagram.data["rows"]
        lines = ["%% Mermaid has limited table support; using Markdown fallback"]
        lines.append("| " + " | ".join(headers) + " |")
        lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
        for r in rows:
            lines.append("| " + " | ".join(r) + " |")
        return "\n".join(lines)

    raise ValueError(f"Unsupported diagram type: {t}")
