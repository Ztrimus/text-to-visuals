"""
Prompt for extracting intent and diagram type from user text, with format instructions placeholder.
"""

INTENT_EXTRACTION_PROMPT = """You are an expert assistant for diagram/visual intent extraction. Given the following user request, extract the following fields as JSON:
intent, diagram_type (one of {diagram_types}), entities, relationships, actions, constraints, context, confidence, explanation, user_goals.

{format_instructions}

Few-shot examples:
User: Show the process of water boiling.
Output: {"intent": "describe process", "diagram_type": "flowchart", "entities": ["water"], "actions": ["boil"], "relationships": [], "constraints": [], "context": "science", "confidence": 0.95, "explanation": "User wants a process diagram.", "user_goals": ["clarity"]}
User: Timeline of major world wars.
Output: {"intent": "show timeline", "diagram_type": "timeline", "entities": ["World War I", "World War II"], "actions": [], "relationships": [], "constraints": [], "context": "history", "confidence": 0.9, "explanation": "User wants a timeline.", "user_goals": ["completeness"]}
User: {user_text}
Output:
"""
