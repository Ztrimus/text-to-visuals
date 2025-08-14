import os
from server.utils.logger import get_logger
from server.agents.visual_structure_agent import VisualStructureExtractor
from server.schemas.diagram import Diagram
from server.config.variables import MODEL_ID

from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from server.prompts.ir_generation_prompt import IR_GENERATION_PROMPT
from server.services.model_bedrock import BedrockModel

logger = get_logger(os.path.basename(__file__))


class IRGenerator:
    def __init__(self, model_id=MODEL_ID):
        logger.info("Initializing with model_id: %s", model_id)
        self.visual_extractor = VisualStructureExtractor(model_id=model_id)
        self.parser = PydanticOutputParser(pydantic_object=Diagram)
        self.prompt = PromptTemplate(
            template=IR_GENERATION_PROMPT,
            input_variables=["visual_structure"],
            partial_variables={
                "format_instructions": self.parser.get_format_instructions()
            },
        )
        self.model = BedrockModel(model_id=model_id)
        # Use RunnableSequence pipeline: prompt | llm | output_parser
        self.chain = self.prompt | self.model.llm | self.parser

    def generate_ir(self, text: str, intent_fields: dict) -> dict:
        logger.info("Generating IR for text")
        # Step 1: Extract visual structure (dict)
        visual_structure = self.visual_extractor.extract(text, intent_fields)
        # Step 2: Convert to Pydantic Diagram model
        result = self.chain.invoke({"visual_structure": visual_structure})
        logger.info("IR result:\n%s", result)
        return result
