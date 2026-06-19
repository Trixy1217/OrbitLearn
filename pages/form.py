import streamlit as st
import json
import os
from google import genai
from dotenv import load_dotenv

# =========================
# LANGFUSE (DESHABILITADO)
# =========================
# from langfuse import Langfuse

load_dotenv()

# langfuse = Langfuse(
#     public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
#     secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
#     host="https://cloud.langfuse.com"
# )

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def load_progress():
    if os.path.exists("progress.json"):
        with open("progress.json", "r") as f:
            return json.load(f)

    return {
        "xp": 0,
        "streak": 0
    }


def save_progress(progress):
    with open("progress.json", "w") as f:
        json.dump(progress, f)


# =========================
# UI
# =========================

st.set_page_config(
    page_title="AI Tutor",
    page_icon="🎓",
    layout="centered"
)

progress = load_progress()

col1, col2 = st.columns(2)

with col1:
    st.metric("XP", progress["xp"])

with col2:
    st.metric("🔥 Streak", progress["streak"])

nivel = progress["xp"] // 100 + 1
xp_para_siguiente = (nivel * 100) - progress["xp"]

st.progress(
    1 - xp_para_siguiente / 100,
    text=f"Nivel {nivel} - Faltan {xp_para_siguiente} XP"
)

st.divider()

# =========================
# FORMULARIO
# =========================

with st.form("tutor_form"):
    topic = st.text_input("Tema")
    question = st.text_area("Pregunta")

    submitted = st.form_submit_button(
        "Preguntar al Tutor",
        type="primary"
    )

# =========================
# PROCESAMIENTO
# =========================

if submitted:

    if not topic.strip() or not question.strip():
        st.warning("Debes ingresar un tema y una pregunta.")
        st.stop()

    with st.spinner("Pensando..."):

        try:

            with open(
                "prompts/tutor.txt",
                "r",
                encoding="utf-8"
            ) as f:
                prompt_template = f.read()

            prompt = (
                prompt_template
                .replace("{topic}", topic)
                .replace("{question}", question)
                .replace("{learning_style}", "visual")
                .replace("{xp}", str(progress["xp"]))
                .replace("{streak}", str(progress["streak"]))
            )

            # =========================
            # LANGFUSE (DESHABILITADO)
            # =========================
            #
            # trace = langfuse.trace(
            #     name="tutor_question",
            #     user_id="demo_user"
            # )
            #
            # trace.span(
            #     name="prompt_build",
            #     input={
            #         "topic": topic,
            #         "question": question
            #     }
            # )
            #
            # generation = trace.generation(
            #     name="gemini_call",
            #     model="gemini-1.5-flash",
            #     input=prompt
            # )

            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )

            # generation.end(
            #     output=response.text
            # )
            #
            # trace.update(
            #     output={
            #         "answer": response.text
            #     }
            # )

            st.subheader("Respuesta del Tutor")
            st.write(response.text)

            progress["xp"] += 10
            progress["streak"] += 1

            save_progress(progress)

            st.success(
                f"+10 XP! Total: {progress['xp']} XP"
            )

        except Exception as e:
            st.error(f"Error: {e}")
            st.code(str(e))

st.caption("Cuota gratis: ~15 preguntas por minuto")





















