"""
intent.py

This module provides intent understanding for user input text.
It uses Bedrock LLMs (via model_bedrock.py) to classify the intent and map to a visual type.
"""

from server.model_bedrock import BedrockModel

from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from langchain.chains.llm import LLMChain
from server.prompts.intent_prompt import INTENT_EXTRACTION_PROMPT
from server.schemas.intent_output import IntentOutput
from server.variables import MODEL_ID, DIAGRAM_TYPES


class IntentClassifier:

    def __init__(self, model_id=MODEL_ID):
        print(f"[IntentClassifier] Initializing with model_id: {model_id}")
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
        self.chain = LLMChain(
            llm=self.model.llm, prompt=self.prompt, output_parser=self.parser
        )

    def classify(self, text: str) -> dict:
        """Classify user text to intent and diagram type, with context fields."""
        print(f"[IntentClassifier] Classifying text: {text}")
        result = self.chain.run(user_text=text)
        print(f"[IntentClassifier] Classification result: {result}")
        return result
