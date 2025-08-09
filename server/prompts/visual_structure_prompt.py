VISUAL_STRUCTURE_PROMPT = """
    You are a diagram structure extractor. Given the user's request and extracted intent fields, output a JSON structure with nodes, edges, events, or topics as appropriate for the diagram type.
    User request: {user_text}
    Intent fields: {intent_fields}
    Output:
"""
