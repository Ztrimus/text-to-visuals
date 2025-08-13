

# Architecture Overview

## Core Design Philosophy
**Backend-First, API-Centric Text-to-Visual Generation Platform**

The architecture prioritizes backend processing and API accessibility to enable universal integration across platforms (web, mobile, Slack, Teams, CLI, etc.) without requiring heavy frontend setup.

## Architectural Layers
- **API Layer**: FastAPI endpoints providing simple text-to-visual generation interface
- **Input Processing Layer**: Text validation, preprocessing, and routing (LangChain integration)
- **LLM Orchestration Layer**: AWS Bedrock foundational models via LangChain for intelligent processing
- **Workflow Layer**: Multi-step pipeline orchestrating intent → structure → IR → visual generation
- **Schema/Prompt Layer**: Modularized prompts and Pydantic schemas for maintainability and type safety
- **Output Generation Layer**: Converts processed data to visual formats (currently Mermaid, future: images/videos)
- **Integration Layer**: Clean API interface enabling consumption by any client platform
- **Demo Layer**: React frontend showcasing API capabilities (not core to the architecture)

## Data Flow & Processing Pipeline
```
Text Input (via API) → Intent Classification → Visual Structure Extraction → 
IR Generation → Validation → Visual Rendering → API Response
```

**Key Principle**: All processing logic resides in the backend, making the API universally consumable.

## Extensibility & Integration Design
- **New Visual Formats**: Add new output generators by implementing the visual rendering interface
- **Platform Integration**: Simple HTTP API enables integration with any platform (Slack, Teams, mobile apps, web)
- **LLM Models**: Extend model support by implementing the model interface (`server/model_bedrock.py`)
- **Diagram Types**: Add new visual types by extending schemas and prompts in modular fashion
- **Client Applications**: Any language/platform can consume the API without backend modifications
- **Workflow Enhancement**: Extend or modify the processing pipeline while maintaining API compatibility

## Future Architecture Vision
- **Visual Export Layer**: Direct image/GIF/video generation capabilities
- **Multi-Format Support**: Single API supporting multiple output formats (Mermaid, PNG, SVG, MP4)
- **Caching Layer**: Intelligent caching for improved performance and cost optimization
- **Observability Layer**: LangSmith integration for monitoring and debugging
- **Client SDKs**: Official SDKs for popular programming languages and platforms
