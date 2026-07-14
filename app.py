
import streamlit as st

st.set_page_config(
    page_title="OrbitLearn",
    page_icon="🚀",
    layout="centered"
)

st.markdown(
    """
    <h1 style='text-align: center;'>🚀OrbitLearn</h1>
    <br>
    <h3 style='text-align: center;'>Tu aventura de aprendizaje comienza aquí</h3>
    <br>
    <br>
    <br>
    <h3 style='text-align: center;'> 🌌 ¿Estás preparado para comenzar?</h3>
    """,
    
    unsafe_allow_html=True
)

st.write("")

col1, col2, col3 = st.columns([1,2,1])

with col2:
    if st.button("Comenzar misión", use_container_width=True):
        st.switch_page("pages/01-character.py")