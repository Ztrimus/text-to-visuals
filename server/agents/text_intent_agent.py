"""
intent.py

This module provides intent understanding for user input text.
It uses Bedrock LLMs (via model_bedrock.py) to classify the intent and map to a visual type.
"""

import os
from server.services.model_bedrock import BedrockModel

from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser

from server.prompts.intent_prompt import INTENT_EXTRACTION_PROMPT
from server.schemas.intent_output import IntentOutput
from server.config.variables import MODEL_ID, DIAGRAM_TYPES
from server.utils.logger import get_logger

logger = get_logger(os.path.basename(__file__))


class IntentClassifier:

    def __init__(self, model_id=MODEL_ID):
        logger.info("[IntentClassifier] Initializing with model_id: %s", model_id)
        self.model = BedrockModel(model_id=model_id)
        self.parser = PydanticOutputParser(pydantic_object=IntentOutput)
        # Prepare prompt with format instructions injected
        self.prompt = PromptTemplate(
            template=INTENT_EXTRACTION_PROMPT,
            input_variables=["user_text"],
            partial_variables={
                "format_instructions": self.parser.get_format_instructions(),
                "diagram_types": ", ".join(DIAGRAM_TYPES),
            },
        )
        # Use RunnableSequence pipeline: prompt | llm | output_parser
        self.chain = self.prompt | self.model.llm | self.parser

    def classify(self, text: str) -> dict:
        """Classify user text to intent and diagram type, with context fields."""
        logger.info("[IntentClassifier] Classifying text...")
        result = self.chain.invoke({"user_text": text})
        logger.info("[IntentClassifier] Classification result: %s", result)
        return result
