"""
workflow.py

This module orchestrates the backend workflow using LangChain/LangGraph patterns.
Steps:
1. Intent understanding (text → intent/type)
2. IR generation (type → IR)
3. Mermaid rendering (IR → Mermaid string)

Observability hooks (LangSmith) can be added for each step.
"""

from server.intent import IntentClassifier

from server.validator import validate
from server.mermaid import to_mermaid
from server.ir_generator import IRGenerator


class Workflow:
    def __init__(self):
        self.intent = IntentClassifier()
        self.ir_generator = IRGenerator()
        # Add more components as needed

    def run(self, text: str) -> str:
        # 1. Intent understanding
        intent_result = self.intent.classify(text)
        # 2. IR generation (LLM-powered, pass all intent fields)
        ir = self.ir_generator.generate_ir(text, intent_result)
        diagram = validate(ir)
        # 3. Mermaid rendering
        return to_mermaid(diagram)
