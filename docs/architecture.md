

# Architecture Overview

## Layers
- **Input Layer**: Handles user text input (Frontend/CLI/GUI)
- **Processing Layer**: Prepares, validates, and routes text (LangChain, prompt modules)
- **Model Layer**: AWS Bedrock foundational models (via LangChain)
- **Workflow Layer**: Orchestrates intent, structure extraction, IR generation (see `server/workflow.py`)
- **Schema/Prompt Layer**: All schemas and prompts are modularized for maintainability
- **Observability Layer**: LangSmith (planned)
- **Output Layer**: Displays or saves generated visuals (Frontend)

## Data Flow
User Input → Processing (LangChain, modular prompts/schemas) → Bedrock LLM → Workflow Orchestration → Output

## Extensibility
- Add new models by implementing the model interface (`server/model_bedrock.py`)
- Add new diagram types by extending schemas and prompts
- Plug in new input/output methods easily
- Swap or extend workflow/orchestration logic
