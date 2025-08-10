from server.schemas.diagram import Diagram, GraphData, TimelineData, MindMapData


def to_mermaid(diagram: Diagram) -> str:
    t = diagram.type
    meta = diagram.meta or {}
    if t == "flowchart":
        g = GraphData(**diagram.data)
        direction = meta.get("direction", "TD")
        lines = [f"flowchart {direction}"]
        for n in g.nodes:
            lines.append(f'{n.id}["{n.label}"]')
        for e in g.edges:
            label = f"|{e.label}|" if e.label else ""
            lines.append(f"{e.source} -->{label} {e.target}")
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
