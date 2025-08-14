"""
visual_structure.py

This module extracts a structured, but not yet Pydantic-validated, visual representation from user text and intent fields.
- Step 1 of IR generation: extract entities, relationships, actions, etc. as a dict.
- Step 2 (in ir_generator.py): convert this to a Pydantic Diagram model.
"""

from typing import Dict

from langchain.prompts import PromptTemplate
from langchain_core.output_parsers.json import JsonOutputParser
from langchain.chains.llm import LLMChain
from server.model_bedrock import BedrockModel
from server.prompts.visual_structure_prompt import VISUAL_STRUCTURE_PROMPT
from server.variables import MODEL_ID


class VisualStructureExtractor:

    def __init__(self, model_id=MODEL_ID):
        print(f"[VisualStructureExtractor] Initializing with model_id: {model_id}")
        self.model = BedrockModel(model_id=model_id)
        self.parser = JsonOutputParser()
        self.prompt = PromptTemplate(
            template=VISUAL_STRUCTURE_PROMPT,
            input_variables=["user_text", "intent_fields"],
        )
        self.chain = LLMChain(
            llm=self.model.llm, prompt=self.prompt, output_parser=self.parser
        )

    def extract(self, user_text: str, intent_fields: dict) -> Dict:
        print(
            f"[VisualStructureExtractor] Extracting visual structure for text: {user_text}"
        )
        result = self.chain.run(user_text=user_text, intent_fields=intent_fields)
        print(f"[VisualStructureExtractor] Extraction result: {result}")
        return result
