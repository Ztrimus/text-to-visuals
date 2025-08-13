
# Text-to-Visuals: Developer Guide

## Main Idea
**API-First Text-to-Visual Generation Platform**: Convert textual descriptions into visual outputs (images, gifs, videos) through a robust backend API that can be integrated anywhere - from web frontends to Slack bots, Teams, chatbots, or any platform.

## Core Philosophy & Approach
- **Backend-First Architecture**: All processing logic resides in the backend for maximum reusability and integration flexibility
- **API-Centric Design**: Simple text input → visual output API that requires no heavy frontend setup
- **Platform Agnostic**: Can be consumed by any system (web apps, bots, mobile apps, CLI tools, etc.)
- **Generic & Accessible**: Focus on making visual generation easily available across different platforms and use cases
- **Iterative Enhancement**: Continuously improve functionality and features while maintaining the clean API interface

## Key Features
- **Text-to-Visual API**: Input text, output visual content (currently Mermaid diagrams, future: images, gifs, videos)
- **Backend-Focused Processing**: All LLM orchestration, intent understanding, and visual generation logic in backend
- **Universal Integration**: Simple API interface allows easy integration with any platform or system
- **Modular Architecture**: Prompts and schemas separated for maintainability and easy extension
- **Multiple Visual Types**: Flowchart, timeline, mind map, table generation (with plans for more)
- **Modern Demo Frontend**: StackEdit-inspired UI with theme support for showcasing API capabilities
- **AWS Bedrock LLMs**: Powerful language models via LangChain for intelligent visual generation
- **Robust Workflow**: Intent extraction → IR generation → Visual rendering pipeline

## Project Structure
- `server/` — **Core Backend Logic** (All processing, LLM orchestration, API endpoints)
	- `api.py` — FastAPI endpoints for text-to-visual generation
	- `workflow.py` — Orchestrates the complete text → visual pipeline
	- `intent.py`, `ir_generator.py`, `visual_structure.py` — Modular LLM-powered processing steps
	- `model_bedrock.py` — AWS Bedrock LLM integration
	- `prompts/` — All prompt templates (intent, IR generation, visual structure)
	- `schemas/` — Pydantic schemas for type safety and validation
	- `mermaid.py`, `validator.py` — Output rendering and validation
- `frontend/` — **Demo Interface** (Showcases API capabilities with modern UI)
	- Modern React app with StackEdit-inspired design for demonstrating backend API
	- Theme support and responsive design for better user experience
	- **Note**: Frontend is for demo purposes; real value is in the backend API
- `docs/` — Documentation and architectural guidance

## API-First Backend Workflow (Core Value)
**Current Implementation (Mermaid Diagrams):**
1. **Intent Understanding**: Maps user text to intent and diagram type using Bedrock LLMs (`server/intent.py`)
2. **Visual Structure Extraction**: Extracts diagram structure as structured data (`server/visual_structure.py`) 
3. **IR Generation**: Converts structure to validated Pydantic model (`server/ir_generator.py`)
4. **Mermaid Rendering**: Transforms IR to Mermaid diagram syntax (`server/mermaid.py`)
5. **API Response**: Returns generated visual via simple HTTP endpoint (`server/api.py`)

**Future Vision (Images/GIFs/Videos):**
- Extend the same workflow to generate actual image files, animated GIFs, and videos
- Add visual export capabilities (PNG/SVG/MP4 generation)
- Maintain the same simple API interface: text input → visual file output
- Enable easy integration with platforms like Slack, Teams, ChatOps, and web applications

## Integration Examples & Use Cases
**The API is designed to be consumed by various platforms:**
- **Web Applications**: Simple fetch() calls to generate visuals in real-time
- **Slack Bots**: Convert team discussions into visual summaries and process flows  
- **Teams Integration**: Generate diagrams from meeting notes and project descriptions
- **ChatOps**: Add visual generation capabilities to existing chat workflows
- **CLI Tools**: Command-line utilities for bulk diagram generation
- **Mobile Apps**: Integrate visual generation into mobile experiences
- **Documentation Systems**: Auto-generate diagrams from technical documentation

**Current API Endpoint:**
```
POST /generate_mermaid
Body: {"text": "your description here"}
Response: {"mermaid": "generated mermaid syntax"}
```

**Future API Vision:**
```
POST /generate_visual
Body: {"text": "description", "format": "png|gif|mp4", "style": "..."}
Response: {"visual_url": "path_to_generated_file"}
```

## Backend-First Development Principles
- **API-Centric Design**: All functionality accessible via clean, simple HTTP endpoints
- **Platform Independence**: Backend logic isolated from frontend concerns for maximum reusability
- **Modular Architecture**: Prompts, schemas, and processing steps separated for easy maintenance and extension
- **Format Instructions**: Always inject format instructions into prompts for reliable LLM output parsing
- **SOLID Principles**: Separation of concerns, extensibility, and maintainability throughout the codebase
- **Integration-Ready**: Designed for easy consumption by any client application or platform

## Improvements & Next Steps

## Recent Improvements & Best Practices (2025)

- **Frontend UI/UX Overhaul (Aug 2025):**
	- Complete redesign with StackEdit-inspired modern interface
	- Theme support: light, dark, and auto modes with CSS custom properties
	- Mobile-responsive design with efficient two-column layout
	- Professional typography using system fonts and improved spacing
	- Interactive circular generate button with loading states and animations
	- Settings dropdown with Heroicons for modern UI elements
	- Clean, minimal design focused on user experience and accessibility

- **Pydantic v2+ Compatibility:**
	- All usages of `.dict()` replaced with `.model_dump()` for Pydantic models to avoid deprecation warnings and ensure forward compatibility.
	- Validation functions now accept both dicts and Pydantic model instances, with robust error handling (try/except for TypeError, AssertionError, ValueError, and generic Exception).

- **Mermaid/MMD Node Naming:**
	- Avoid using reserved keywords (like `end`) as node names in Mermaid diagrams. Always ensure node references match their definitions to prevent parse errors.

- **Bedrock Model Selection Logic:**
	- Backend supports both `ChatBedrock` and `BedrockLLM` based on model type, with correct parameter usage for Claude 3/Opus and legacy models. This ensures compatibility with the latest AWS Bedrock offerings.

- **Prompt Escaping and Format Instructions:**
	- Use double curly braces and string replacement for prompt formatting, especially for JSON examples in prompts, to avoid formatting errors and ensure reliable output parsing.

- **Error Handling and Debugging Tips:**
	- When running scripts that import from the `server` package, use `python -m server.validator` from the project root or set `PYTHONPATH` appropriately to avoid import errors.

- **General Best Practices:**
	- Modularize all prompts and schemas for maintainability.
	- Maintain clean separation between backend logic and frontend presentation.
	- Use modern web standards for responsive design and accessibility.
	- Implement proper theme management for user preference support.
	- Document new features and backend changes promptly in this folder.
- Add visual export functionality (PNG/SVG/GIF/MP4 generation)
- Implement direct image/video generation from text (bypass Mermaid for richer visuals)
- Add more diagram types and visual formats
- Enhance integration examples for Slack, Teams, and other platforms
- Integrate LangSmith for observability and debugging
- Expand test coverage and API documentation
- Develop client SDKs for popular programming languages

## Valuable diagram types to consider:
- **Flowchart**: Maps processes step-by-step.
- **Timeline**: Shows sequences or historical progression.
- **Mind Map**: Visualizes connections and hierarchies of ideas.
- **Table**: Organizes data in rows and columns for comparison.
- **Bar Chart / Column Chart**: Good for comparing quantities across categories.
- **Line Chart**: Effective for showing trends or changes over time.
- **Pie Chart / Circle Diagram**: Shows parts of a whole, proportions or percentages.
- **Venn Diagram**: Highlights overlaps and relationships between different sets.
- **Tree Diagram**: Shows hierarchies or branching decisions.
- **Swimlane Diagram**: Clarifies roles and responsibilities in processes by lanes.
- **Fishbone Diagram (Cause-and-Effect)**: Illustrates root causes of a problem.
- **Funnel Chart**: Displays stages in a process narrowing down to an outcome.
- **Sankey Diagram**: Shows flow and quantity between nodes, useful for movement or transfers.
- **Matrix or Quadrant Chart**: Categorizes and ranks items along two axes, useful for decision making and strategic analysis.
- **Bubble Chart**: Visualizes relationships among three numeric variables.
- **Heatmap**: Represents data intensity or frequency with color variations.
- **Network Diagram**: Displays relationships and interactions between entities.

---
Refer to this guide for a quick overview and development reference.
