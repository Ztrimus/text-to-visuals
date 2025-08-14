
# Server Folder Structure Overview

This backend is designed for scalable, modular AI workflows using LangChain and LangGraph. Below is an explanation of each directory and its role in the project.

## Directory Layout

```
server/
├── config/                  # Configuration files for environments, models, variables
│   ├── variables.py
│   ├── environments/
│   │   ├── development.yaml
│   │   └── production.yaml
│   └── models/
│       ├── openai_config.yaml
│       └── custom_llm_config.yaml
├── agents/                  # Agent definitions (LLMs, pipeline steps, etc.)
│   ├── text_intent_agent.py
│   ├── ir_generation_agent.py
│   └── visual_structure_agent.py
├── apis/                    # API endpoint definitions (e.g., FastAPI routers)
│   └── mermaid_api.py
├── graphs/                  # Workflow orchestration (LangGraph, pipelines)
│   └── workflow.py
├── tools/                   # Custom tools, integrations, utility modules
│   └── mermaid.py
├── prompts/                 # Prompt templates for agents and workflows
│   ├── intent_prompt.py
│   ├── ir_generation_prompt.py
│   └── visual_structure_prompt.py
├── services/                # Data processing, validation, model integration
│   ├── model_bedrock.py
│   └── validator.py
├── schemas/                 # Pydantic schemas, data models, entities
│   ├── diagram.py
│   └── intent_output.py
├── utils/                   # Helper functions, logging, shared utilities
│   ├── helper.py
│   └── logger.py
├── tests/                   # Unit and integration tests (recommended to mirror code structure)
├── .env                     # Environment variables (API keys, secrets)
├── langgraph.json           # LangGraph config for deployment
├── requirements.txt         # Python dependencies
├── README.md                # This overview and setup instructions
└── main.py                  # Application entry point (initializes LangGraph, API, etc.)
```

## Directory Explanations

- **config/**: Centralizes all configuration files for environments, models, and variables. Makes it easy to switch between dev/prod and manage model/API settings.
- **agents/**: Contains agent definitions (LLMs, pipeline steps, etc.), each responsible for a specific task in the workflow.
- **apis/**: API endpoint definitions, such as FastAPI routers for serving the backend.
- **graphs/**: Orchestrates workflows and pipelines using LangGraph or similar frameworks.
- **tools/**: Custom tools, integrations, and utility modules used by agents or workflows.
- **prompts/**: All prompt templates, organized by agent or workflow type.
- **services/**: Data processing, validation, and model integration logic.
- **schemas/**: Pydantic schemas and data models for type safety and validation.
- **utils/**: Helper functions, logging setup, and shared utilities.
- **tests/**: Unit and integration tests. Recommended to mirror the code structure for maintainability.
- **.env**: Stores sensitive environment variables (API keys, secrets) outside the codebase for security.
- **langgraph.json**: Configuration for LangGraph workflows and deployment.
- **requirements.txt**: Lists all Python dependencies for easy installation.
- **README.md**: Project overview, folder explanations, and setup instructions.
- **main.py**: Entry point for the backend application, initializing LangGraph, API, and other core services.

## How to Use This Structure

- Add new agents, tools, or workflows by creating new files in the relevant folders.
- Keep prompts and schemas modular for easy extension.
- Use config files to manage environment and model settings.
- Place shared helpers in `utils/` and keep tests organized in `tests/`.
- Store sensitive info in `.env` and keep it out of version control.

This structure is designed for maintainability, scalability, and collaboration in modern AI backend projects.