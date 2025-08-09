
# Architecture Overview

- **Input Layer**: Handles user text input (Frontend/CLI/GUI)
- **Processing Layer**: Prepares, validates, and routes text (LangChain, LangGraph)
- **Model Layer**: AWS Bedrock foundational models (via LangChain)
- **Workflow Layer**: Orchestrates intent understanding, visual type mapping, IR generation (LangGraph)
- **Observability Layer**: LangSmith for monitoring and debugging
- **Output Layer**: Displays or saves generated visuals (Frontend)

## Data Flow
Input → Processing (LangChain/LangGraph) → Model (Bedrock) → Workflow (LangGraph) → Output

## Extensibility
- Add new models by implementing the model interface (see `server/model_bedrock.py`)
- Plug in new input/output methods easily
- Swap or extend workflow/orchestration logic
