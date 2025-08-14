import os
from server.utils.logger import get_logger
from server.agents.visual_structure_agent import VisualStructureExtractor
from server.schemas.diagram import Diagram
from server.config.variables import MODEL_ID

from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from server.prompts.ir_generation_prompt import IR_GENERATION_PROMPT

logger = get_logger(os.path.basename(__file__))


class IRGenerator:

    def __init__(self, model_id=MODEL_ID):
        logger.info(f"Initializing with model_id: {model_id}")
        self.visual_extractor = VisualStructureExtractor(model_id=model_id)
        self.parser = PydanticOutputParser(pydantic_object=Diagram)
        self.prompt = PromptTemplate(
            template=IR_GENERATION_PROMPT,
            input_variables=["visual_structure"],
            partial_variables={
                "format_instructions": self.parser.get_format_instructions()
            },
        )
        from server.services.model_bedrock import BedrockModel

        self.model = BedrockModel(model_id=model_id)
        self.chain = LLMChain(
            llm=self.model.llm, prompt=self.prompt, output_parser=self.parser
        )

    def generate_ir(self, text: str, intent_fields: dict) -> dict:
        logger.info(f"Generating IR for text")
        # Step 1: Extract visual structure (dict)
        visual_structure = self.visual_extractor.extract(text, intent_fields)
        logger.info(f"Extracted visual structure:\n{visual_structure}")
        # Step 2: Convert to Pydantic Diagram model
        result = self.chain.run(visual_structure=visual_structure)
        logger.info(f"IR result:\n{result}")
        return result
