from server.utils.logger import get_logger

"""
model_bedrock.py

This module provides a simple interface to AWS Bedrock foundational models using LangChain.
It is designed to be imported and used by other backend components for text-to-IR or text-to-visual tasks.

- Keeps all Bedrock/model logic isolated from API and workflow code.
- Follows modular, extensible design for future model support.
"""

from langchain_aws import BedrockLLM, ChatBedrock
from langchain_core.language_models.llms import LLM
import os
from server.config.variables import MODEL_ID

logger = get_logger(os.path.basename(__file__))


class BedrockModel:
    """Wrapper for AWS Bedrock LLMs via LangChain. Uses ChatBedrock for chat models, BedrockLLM for legacy models."""

    def __init__(self, model_id: str, region: str = "us-east-1", **kwargs):
        self.model_id = model_id
        self.region = region or os.environ.get("AWS_REGION", "us-east-1")
        # Use ChatBedrock for Claude 3/Opus, BedrockLLM for legacy
        if any(x in model_id for x in ["claude-3", "opus", "sonnet", "haiku"]):
            self.llm = ChatBedrock(model=model_id, region=self.region, **kwargs)
        else:
            self.llm = BedrockLLM(model=model_id, region=self.region, **kwargs)

    def generate(self, prompt: str, **kwargs) -> str:
        """Generate a response from the Bedrock model."""
        result = self.llm.invoke(prompt, **kwargs)
        return result.content


# Example usage (for testing only, not run on import)
if __name__ == "__main__":
    model = BedrockModel(model_id=MODEL_ID)
    prompt = "Summarize the following text: LangChain is a framework for developing applications powered by language models."
    logger.info(model.generate(prompt))
