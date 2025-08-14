"""
ir_generator.py

This module generates a diagram IR (intermediate representation) from user text and diagram type using Bedrock LLMs.
- Keeps IR generation logic modular and isolated.
- Can be extended for prompt engineering, few-shot examples, etc.
"""

from server.visual_structure import VisualStructureExtractor
from server.schemas.diagram import Diagram
from server.variables import MODEL_ID

from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from server.prompts.ir_generation_prompt import IR_GENERATION_PROMPT


class IRGenerator:

    def __init__(self, model_id=MODEL_ID):
        print(f"[IRGenerator] Initializing with model_id: {model_id}")
        self.visual_extractor = VisualStructureExtractor(model_id=model_id)
        self.parser = PydanticOutputParser(pydantic_object=Diagram)
        self.prompt = PromptTemplate(
            template=IR_GENERATION_PROMPT,
            input_variables=["visual_structure"],
            partial_variables={
                "format_instructions": self.parser.get_format_instructions()
            },
        )
        from server.model_bedrock import BedrockModel

        self.model = BedrockModel(model_id=model_id)
        self.chain = LLMChain(
            llm=self.model.llm, prompt=self.prompt, output_parser=self.parser
        )

    def generate_ir(self, text: str, intent_fields: dict) -> dict:
        print(f"[IRGenerator] Generating IR for text: {text}")
        # Step 1: Extract visual structure (dict)
        visual_structure = self.visual_extractor.extract(text, intent_fields)
        print(f"[IRGenerator] Extracted visual structure: {visual_structure}")
        # Step 2: Convert to Pydantic Diagram model
        result = self.chain.run(visual_structure=visual_structure)
        print(f"[IRGenerator] IR result: {result}")
        return result
