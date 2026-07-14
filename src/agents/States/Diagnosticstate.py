from pydantic import BaseModel, Field
from typing import List, Optional


class DiagnosticState(BaseModel):

    user_id: str

    # Control del flujo
    current_question: int = 1
    total_questions: int = 10
    current_question_text: str

    # Respuestas del usuario
    answers: List[str] = Field(default_factory=list)
    # ¿Terminó el diagnóstico?
    finished: bool = False

