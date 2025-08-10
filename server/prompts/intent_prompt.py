"""
Prompt for extracting intent and diagram type from user text, with format instructions placeholder.
"""

INTENT_EXTRACTION_PROMPT = """You are an expert assistant for diagram/visual intent extraction.

Your task is to analyze the user's request and extract the following fields as a structured JSON object:
- intent: The user's main goal or action.
- diagram_type: One of {diagram_types}. Always output diagram_type as a string. If not sure, use "" (empty string) or "unknown".
- entities: Key objects, concepts, or actors.
- relationships: Connections or interactions between entities.
- actions: Main actions or processes described.
- constraints: Any limitations, conditions, or requirements.
- context: The domain or background (e.g., science, history).
- confidence: A float between 0 and 1 indicating your confidence in the extraction.
- explanation: A brief rationale for your choices.
- user_goals: What the user wants to achieve with the diagram.

{format_instructions}

Guidelines:
- Always choose the most appropriate diagram_type from the allowed list.
- If information is missing, use an empty list or null as appropriate.
- Be concise and use natural language for explanations.
- Use the provided format instructions to ensure valid JSON output.

Few-shot examples:
User: Show the process of water boiling.
Output: {{"intent": "describe process", "diagram_type": "flowchart", "entities": ["water"], "actions": ["boil"], "relationships": [], "constraints": [], "context": "science", "confidence": 0.95, "explanation": "User wants a process diagram.", "user_goals": ["clarity"]}}
User: Timeline of major world wars.
Output: {{"intent": "show timeline", "diagram_type": "timeline", "entities": ["World War I", "World War II"], "actions": [], "relationships": [], "constraints": [], "context": "history", "confidence": 0.9, "explanation": "User wants a timeline.", "user_goals": ["completeness"]}}
User: {user_text}
Output:
"""
