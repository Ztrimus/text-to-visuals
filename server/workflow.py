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
        print("[Workflow] Initializing Workflow components...")
        self.intent = IntentClassifier()
        self.ir_generator = IRGenerator()

    def run(self, text: str) -> str:
        print(f"[Workflow] Received input: {text}")
        # 1. Intent understanding
        print("[Workflow] Step 1: Intent understanding...")
        intent_result = self.intent.classify(text)
        print(f"[Workflow] Intent result: {intent_result}")
        # 2. IR generation (LLM-powered, pass all intent fields)
        print("[Workflow] Step 2: IR generation...")
        ir = self.ir_generator.generate_ir(text, intent_result)
        print(f"[Workflow] IR: {ir}")
        diagram = validate(ir)
        print(f"[Workflow] Validated diagram: {diagram}")
        # 3. Mermaid rendering
        print("[Workflow] Step 3: Mermaid rendering...")
        mermaid_code = to_mermaid(diagram)
        print(f"[Workflow] Mermaid code generated.")
        return mermaid_code

    def run_example(self, text: str) -> str:
        return """
        flowchart TD
        start["Start: Need to Write Code"]
        assess_task["Assess Task Complexity"]
        traditional_coding["Traditional Coding<br>(Cursor/Copilot)"]
        vibe_coding_decision["Is it a Leaf Node?"]
        prepare_context["Prepare Context<br>(15-20 min)"]
        act_as_pm["Act as PM for Claude:<br>• Define requirements<br>• Tour codebase<br>• Set constraints"]
        let_claude_cook["Let Claude Generate Code"]
        design_verification["Design Verification:<br>• Stress tests<br>• Input/output checks<br>• End-to-end tests"]
        review_tests["Review Tests Only<br>(Not Implementation)"]
        tests_pass["Do Tests Pass?"]
        iterate_claude["Iterate with Claude"]
        merge_code["Merge to Production"]
        end_node["End: Code Deployed"]
        core_architecture["Core Architecture:<br>Write/Review Manually"]
        start --> assess_task
        assess_task -->|< 1 hour task| traditional_coding
        assess_task -->|> 1 hour task| vibe_coding_decision
        vibe_coding_decision -->|Yes| prepare_context
        vibe_coding_decision -->|"No (Core/Trunk)"| core_architecture
        prepare_context --> act_as_pm
        act_as_pm --> let_claude_cook
        let_claude_cook --> design_verification
        design_verification --> review_tests
        review_tests --> tests_pass
        tests_pass -->|Yes| merge_code
        tests_pass -->|No| iterate_claude
        iterate_claude --> let_claude_cook
        traditional_coding --> merge_code
        core_architecture --> merge_code
        merge_code --> end_node"""
