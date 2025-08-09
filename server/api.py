from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from server.validator import validate
from server.mermaid import to_mermaid
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify ["http://localhost:5174"] for more security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TextRequest(BaseModel):
    text: str


@app.post("/generate_mermaid")
def generate_mermaid(req: TextRequest):
    # For now, use a stub: map text to a fixed IR (flowchart)
    # Later, replace with real NLU/LLM logic
    if not req.text.strip():
        raise HTTPException(status_code=400, detail="Text input required.")
    # Example: always return a simple flowchart IR
    ir = {
        "type": "flowchart",
        "meta": {"direction": "TD", "title": "Simple flow"},
        "data": {
            "nodes": [
                {"id": "A", "label": "Start"},
                {"id": "B", "label": "Step B"},
                {"id": "C", "label": "Step C"},
            ],
            "edges": [{"source": "A", "target": "B"}, {"source": "B", "target": "C"}],
        },
    }
    diagram = validate(ir)
    mermaid_str = to_mermaid(diagram)
    return {"mermaid": mermaid_str}
