"""
model_bedrock.py

This module provides a simple interface to AWS Bedrock foundational models using LangChain.
It is designed to be imported and used by other backend components for text-to-IR or text-to-visual tasks.

- Keeps all Bedrock/model logic isolated from API and workflow code.
- Follows modular, extensible design for future model support.
"""

from langchain_aws import BedrockLLM
from langchain_core.language_models.llms import LLM
from typing import Any, Dict
import os


class BedrockModel:
    """Wrapper for AWS Bedrock LLMs via LangChain."""

    def __init__(self, model_id: str, region: str = None, **kwargs):
        self.model_id = model_id
        self.region = region or os.environ.get("AWS_REGION", "us-east-1")
        self.llm: LLM = BedrockLLM(model_id=model_id, region=self.region, **kwargs)

    def generate(self, prompt: str, **kwargs) -> str:
        """Generate a response from the Bedrock model."""
        return self.llm.invoke(prompt, **kwargs)


# Example usage (for testing only, not run on import)
if __name__ == "__main__":
    model = BedrockModel(model_id="anthropic.claude-v2")
    prompt = "Summarize the following text: LangChain is a framework for developing applications powered by language models."
    print(model.generate(prompt))
