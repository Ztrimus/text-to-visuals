"""
Prompt for IR (diagram) generation from structured visual representation, with format instructions placeholder.
"""

IR_GENERATION_PROMPT = """
You are a diagram IR generator. Given a structured visual representation, output a valid JSON IR matching this Pydantic schema: {schema}.
Few-shot example:
Input: {'type': 'flowchart', 'meta': {}, 'data': {'nodes': [{'id': 'A', 'label': 'Start'}, {'id': 'B', 'label': 'End'}], 'edges': [{'source': 'A', 'target': 'B'}]}}
Output: {'type': 'flowchart', 'meta': {}, 'data': {'nodes': [{'id': 'A', 'label': 'Start'}, {'id': 'B', 'label': 'End'}], 'edges': [{'source': 'A', 'target': 'B'}]}}

Input: {visual_structure}
{format_instructions}
Output:
"""
