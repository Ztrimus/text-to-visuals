

# Developer Workflow

1. Clone the repo and install dependencies
2. Start the FastAPI backend: `uvicorn server.api:app --reload`
3. Start the frontend: `npm run dev` (in `frontend/`)
   - Modern React app with StackEdit-inspired UI
   - Theme support (light/dark/auto) for user preferences
   - Mobile-responsive design with professional styling
4. Develop and test Bedrock model logic in `server/model_bedrock.py`
5. Add/modify workflow orchestration in `server/workflow.py`
6. Add or update prompt templates in `server/prompts/` and schemas in `server/schemas/`
7. Integrate LangSmith for observability (planned)
8. Extend frontend for new features while maintaining clean UI/UX standards

## Quick Commands
- `uvicorn server.api:app --reload` – Start backend API
- `pytest` – Run backend tests
- `npm run dev` (in `frontend/`) – Start frontend

## Tips
- Keep model, workflow, and API code modular and separated
- Use LangChain for prompt management and Bedrock access
- Modularize all prompts and schemas for maintainability
- Maintain UI/UX consistency with StackEdit-inspired design standards
- Support theme preferences and responsive design for all new frontend features
- Use LangSmith for observability (planned)
- Document new features and backend changes in this folder
