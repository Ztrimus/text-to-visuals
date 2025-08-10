"""
Prompt for extracting a structured visual representation from user text and intent fields.
"""

VISUAL_STRUCTURE_PROMPT = """
You are a diagram structure extractor. Given the user's request and extracted intent fields, output a JSON structure with nodes, edges, events, or topics as appropriate for the diagram type.

Guidelines:
- Choose the most effective structure for the user's intent (e.g., flowchart for processes, timeline for sequences, mind map for hierarchies).
- Use clear, descriptive node and edge labels.
- For timelines, use events with time and label fields.
- For mind maps, use root, children, and edges.
- If information is missing, use empty lists or nulls as appropriate.
- Follow best practices for clarity, minimalism, and accessibility.

User request: {user_text}
Intent fields: {intent_fields}
Output:
"""
