from langchain_ollama import OllamaLLM

# IMPORTANTE: llm se define, pero NO se ejecuta nada aquí
llm = OllamaLLM(model="gemma:2b")


def map_step(chunks, query: str):
    """
    Primer paso del Map-Reduce:
    resume cada chunk de texto.
    """
    summary_chunk = []

    for chunk in chunks:
        prompt = f"""
Eres un asistente que analiza partes de un documento.

Extrae SOLO la información relevante para responder esta pregunta:
{query}

Texto:
{chunk}

Respuesta breve:
"""

        rsp = llm.invoke(prompt)
        summary_chunk.append(rsp.content)

    return summary_chunk


def reduce_step(summary_chunk, query: str):
    """
    Segundo paso del Map-Reduce:
    combina todos los resúmenes y genera respuesta final.
    """
    combined = "\n".join(summary_chunk)

    prompt = f"""
    Eres un analista de documentos.

    Con base en estos resúmenes parciales, responde la pregunta final de forma clara y directa.

    Pregunta:
    {query}

    Resúmenes:
    {combined}

    Respuesta final:
    """
    response = llm.invoke(prompt)
 
    return response.content


def map_reduce_rag(chunks, query: str):
    """
    Pipeline completo Map-Reduce RAG.
    """
    mapped = map_step(chunks, query)
    final_answer = reduce_step(mapped, query)
    return final_answer