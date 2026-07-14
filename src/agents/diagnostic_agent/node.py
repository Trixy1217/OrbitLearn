from States.Diagnosticstate import DiagnosticState
from pydantic import BaseModel
from llms.gemini import gemini_model
from prompt import SYSTEMPROMPT

clase= "python"

llm = gemini_model()

class DiagnosticLLMResponse(BaseModel):
    next_question: str | None
    finished: bool

structured_llm = llm.with_structured_output(DiagnosticLLMResponse)


def node_diagnostic(state: DiagnosticState):

    prompt = f"""
    {SYSTEMPROMPT}

    Curso: {clase}

    Pregunta actual:
    {state.current_question}/{state.total_questions}

    Pregunta anterior:
    {state.current_question_text}
    

    Última respuesta:
    {state.answers[-1] if state.answers else "Ninguna"}
    """

    response = structured_llm.invoke(prompt)


    state.finished = response.finished


    if not response.finished:
        state.current_question += 1
        state.current_question_text = response.next_question

    return state
      














