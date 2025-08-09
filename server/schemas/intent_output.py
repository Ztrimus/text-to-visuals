"""
Pydantic schema for intent extraction output.
"""
from typing import List, Optional
from pydantic import BaseModel, Field

class IntentOutput(BaseModel):
    intent: str
    diagram_type: str
    entities: Optional[List[str]] = Field(default_factory=list)
    relationships: Optional[List[str]] = Field(default_factory=list)
    actions: Optional[List[str]] = Field(default_factory=list)
    constraints: Optional[List[str]] = Field(default_factory=list)
    context: Optional[str] = None
    confidence: Optional[float] = None
    explanation: Optional[str] = None
    user_goals: Optional[List[str]] = Field(default_factory=list)
