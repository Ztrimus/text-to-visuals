"""
workflow.py

This module orchestrates the backend workflow using LangChain/LangGraph patterns.
Steps:
1. Intent understanding (text → intent/type)
2. IR generation (type → IR)
3. Mermaid rendering (IR → Mermaid string)

Observability hooks (LangSmith) can be added for each step.
"""

import os
from server.agents.text_intent_agent import IntentClassifier

from server.services.validator import validate
from server.tools.mermaid import to_mermaid
from server.agents.ir_generation_agent import IRGenerator


from server.utils.logger import get_logger

logger = get_logger(os.path.basename(__file__))


class Workflow:
    def __init__(self):
        logger.info("Initializing Workflow components...")
        self.intent = IntentClassifier()
        self.ir_generator = IRGenerator()

    def run(self, text: str) -> str:
        logger.info("Received input")

        logger.info("%s\nStep 1: Intent understanding...\n%s\n", "=" * 20, "=" * 20)
        intent_result = self.intent.classify(text)

        logger.info("%s\nStep 2: IR generation...\n%s\n", "=" * 20, "=" * 20)
        ir = self.ir_generator.generate_ir(text, intent_result)
        # logger.info("IR: %s", ir)
        diagram = validate(ir)
        logger.info("Validated diagram: %s", diagram)

        logger.info("%s\nStep 3: Mermaid rendering...\n%s\n", "=" * 20, "=" * 20)
        mermaid_code = to_mermaid(diagram)
        logger.info("Mermaid code generated.")
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
