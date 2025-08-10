
# Text-to-Visuals: Developer Guide

## Main Idea
Convert textual descriptions into visual diagrams using LLMs and modular orchestration.

## Key Features
- Text-to-diagram (flowchart, timeline, mind map, table) generation
- Modular backend: prompts and schemas separated for maintainability
- FastAPI backend, Vite + React frontend, Mermaid for rendering
- AWS Bedrock LLMs via LangChain
- Robust intent extraction, IR generation, and workflow orchestration

## Project Structure
- `server/` — Backend code (FastAPI, orchestration, LLM logic)
	- `prompts/` — All prompt templates (e.g., `intent_prompt.py`, `ir_generation_prompt.py`)
	- `schemas/` — All Pydantic schemas (e.g., `intent_output.py`, `diagram.py`)
	- `model_bedrock.py` — Bedrock LLM wrapper
	- `intent.py`, `ir_generator.py`, `visual_structure.py` — Modular LLM-powered logic
	- `workflow.py` — Orchestrates intent, IR, and rendering
- `frontend/` — Vite + React app with Mermaid rendering
- `docs/` — Documentation (this folder)

## Backend Workflow (LLM + Orchestration)
1. **Intent Understanding**: Maps user text to intent and diagram type using Bedrock LLMs (see `server/intent.py`).
2. **Visual Structure Extraction**: Extracts diagram structure as a dict (see `server/visual_structure.py`).
3. **IR Generation**: Converts structure to Pydantic model (see `server/ir_generator.py`).
4. **Workflow Orchestration**: Chains together all steps (see `server/workflow.py`).
5. **Observability**: LangSmith (planned) for monitoring and debugging.

## Best Practices
- All prompts and schemas are modularized in dedicated folders
- Format instructions are always injected into prompts for reliable parsing
- SOLID principles: separation of concerns, extensibility, maintainability
- Output parsing uses LangChain's recommended output parsers

## Improvements & Next Steps
- Add more diagram types and models
- Enhance frontend UX and diagram editing
- Integrate LangSmith for observability
- Expand test coverage

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
