from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from server.graphs.workflow import Workflow
import uvicorn

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


workflow = Workflow()


@app.post("/generate_mermaid")
def generate_mermaid(req: TextRequest):
    if not req.text.strip():
        raise HTTPException(status_code=400, detail="Text input required.")
    try:
        mermaid_str = workflow.run(req.text)
        return {"mermaid": mermaid_str}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run("app.api:app", host="0.0.0.0", port=8000, reload=True)
