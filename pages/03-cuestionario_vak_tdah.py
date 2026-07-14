import streamlit as st
from src.database.player_repository import set_learning_style
from src.database.player_repository import get_player



current_id = st.session_state.get("player_id")
VAK_QUESTIONS = [
    {
        "id": 1,
        "text": "Cuando aprendes algo nuevo, ¿cómo prefieres que te lo expliquen?",
        "options": [
            {
                "text": "Con diagramas, gráficos y ejemplos visuales",
                "learning_style": "visual",
            },
            {
                "text": "Hablándome paso a paso con explicaciones verbales",
                "learning_style": "auditory",
            },
            {
                "text": "Dejándome experimentar y practicar directamente",
                "learning_style": "kinesthetic",
            },
        ],
    },
    {
        "id": 2,
        "text": "¿Cuál es tu mejor forma de recordar información?",
        "options": [
            {
                "text": "Recordando lo que vi (imágenes, colores, formas)",
                "learning_style": "visual",
            },
            {
                "text": "Recordando lo que escuché (palabras, tonos, ritmo)",
                "learning_style": "auditory",
            },
            {
                "text": "Recordando lo que hice o sentí (movimientos, emociones)",
                "learning_style": "kinesthetic",
            },
        ],
    },
    {
        "id": 3,
        "text": "Cuando tienes que seguir instrucciones, ¿qué prefieres?",
        "options": [
            {
                "text": "Leer las instrucciones escritas o ver un video",
                "learning_style": "visual",
            },
            {
                "text": "Que alguien me las explique verbalmente",
                "learning_style": "auditory",
            },
            {
                "text": "Intentar hacerlo yo mismo mientras me guían",
                "learning_style": "kinesthetic",
            },
        ],
    },
    {
        "id": 4,
        "text": "¿Cómo te concentras mejor en clase o en una presentación?",
        "options": [
            {
                "text": "Tomando notas y haciendo esquemas visuales",
                "learning_style": "visual",
            },
            {
                "text": "Escuchando atentamente sin distracciones",
                "learning_style": "auditory",
            },
            {
                "text": "Moviéndome, gesticulando o haciendo algo con las manos",
                "learning_style": "kinesthetic",
            },
        ],
    },
    {
        "id": 5,
        "text": "Cuando aprendes a usar un software o herramienta, ¿qué haces?",
        "options": [
            {
                "text": "Busco tutoriales en video o guías con capturas de pantalla",
                "learning_style": "visual",
            },
            {
                "text": "Escucho explicaciones o veo videos con narración",
                "learning_style": "auditory",
            },
            {
                "text": "Empiezo a explorar y aprender haciendo clic",
                "learning_style": "kinesthetic",
            },
        ],
    },
    {
        "id": 6,
        "text": "¿Cómo describes tu ambiente de estudio ideal?",
        "options": [
            {
                "text": "Bien iluminado, con todo organizado visualmente",
                "learning_style": "visual",
            },
            {
                "text": "Tranquilo, sin ruidos que me distraigan",
                "learning_style": "auditory",
            },
            {
                "text": "Cómodo, donde pueda moverme libremente",
                "learning_style": "kinesthetic",
            },
        ],
    },
    {
        "id": 7,
        "text": "Cuando resuelves un problema complejo, ¿qué haces primero?",
        "options": [
            {
                "text": "Dibujo o visualizo el problema en mi mente",
                "learning_style": "visual",
            },
            {
                "text": "Me lo explico a mí mismo en voz alta",
                "learning_style": "auditory",
            },
            {
                "text": "Intento diferentes soluciones hasta encontrar la correcta",
                "learning_style": "kinesthetic",
            },
        ],
    },
    {
        "id": 8,
        "text": "¿Cuál es tu forma favorita de entretenimiento?",
        "options": [
            {
                "text": "Ver películas, leer cómics o navegar por redes sociales",
                "learning_style": "visual",
            },
            {
                "text": "Escuchar podcasts, música o audiolibros",
                "learning_style": "auditory",
            },
            {
                "text": "Jugar videojuegos, hacer deporte o actividades manuales",
                "learning_style": "kinesthetic",
            },
        ],
    },
]






if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "scores" not in st.session_state:
    st.session_state.scores = {
        "visual": 0,
        "auditory": 0,
        "kinesthetic": 0
    }


if st.session_state.current_question < len(VAK_QUESTIONS):
    question = VAK_QUESTIONS[st.session_state.current_question]

    st.subheader(
        f"Pregunta {st.session_state.current_question + 1} de {len(VAK_QUESTIONS)}"
    )

    choice = st.radio(
        question["text"],
        question["options"],
        format_func=lambda x: x["text"]
    )

    if st.button("Siguiente"):
        learning_style = choice["learning_style"]
        st.session_state.scores[learning_style] += 1
        st.session_state.current_question += 1
        st.rerun()



scores = st.session_state.scores

max_score = max(scores.values())

dominant = [
    learning_style
    for learning_style, score in scores.items()
    if score == max_score
]

learning_style_final = dominant[0] if len(dominant) == 1 else "mixed"


set_learning_style(current_id,learning_style_final)

st.title(learning_style_final)
st.title(current_id)

oelo = get_player(current_id)
learning = oelo[6]

st.title(learning)





