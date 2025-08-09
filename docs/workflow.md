
# Developer Workflow

1. Clone the repo and install dependencies
2. Run the main script or start the FastAPI server for backend
3. Develop and test Bedrock model logic in `server/model_bedrock.py`
4. Add/modify workflow orchestration using LangGraph and LangChain
5. Integrate LangSmith for observability and monitoring
6. Extend frontend for new features

## Quick Commands
- `python main.py` – Run the main program (if present)
- `uvicorn server.api:app --reload` – Start backend API
- `pytest` – Run tests
- `npm run dev` (in `frontend/`) – Start frontend

## Tips
- Keep model, workflow, and API code modular and separated
- Use LangChain for prompt management and Bedrock access
- Use LangGraph for workflow orchestration
- Use LangSmith for observability
- Document new features and backend changes in this folder
