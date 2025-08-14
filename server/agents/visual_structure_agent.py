"""
visual_structure.py

This module extracts a structured, but not yet Pydantic-validated, visual representation from user text and intent fields.
- Step 1 of IR generation: extract entities, relationships, actions, etc. as a dict.
- Step 2 (in ir_generator.py): convert this to a Pydantic Diagram model.
"""

import os
from typing import Dict

from langchain.prompts import PromptTemplate
from langchain_core.output_parsers.json import JsonOutputParser
from langchain.chains.llm import LLMChain
from server.services.model_bedrock import BedrockModel
from server.prompts.visual_structure_prompt import VISUAL_STRUCTURE_PROMPT
from server.config.variables import MODEL_ID
from server.utils.helper import measure_execution_time
from server.utils.logger import get_logger, pretty_log

logger = get_logger(os.path.basename(__file__))


class VisualStructureExtractor:

    def __init__(self, model_id=MODEL_ID):
        print(f"[VisualStructureExtractor] Initializing with model_id: {model_id}")
        self.model = BedrockModel(model_id=model_id)
        self.parser = JsonOutputParser()
        self.prompt = PromptTemplate(
            template=VISUAL_STRUCTURE_PROMPT,
            input_variables=["user_text", "intent_fields"],
        )
        # Use RunnableSequence pipeline: prompt | llm | output_parser
        self.chain = self.prompt | self.model.llm | self.parser

    @measure_execution_time
    def extract(self, user_text: str, intent_fields: dict) -> Dict:
        result = self.chain.invoke(
            {"user_text": user_text, "intent_fields": intent_fields}
        )
        pretty_log(logger, "[VisualStructureExtractor] Extraction result", result)
        return result
