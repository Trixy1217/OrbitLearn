import streamlit as st
from src.database.player_repository import get_player_with_nickcname



st.title("Coach for tech students")

nombre = st.text_input("Nickname of character")

contraseña = st.text_input("Write your password")

if st.button("LOGIN"):
    try:
        player = get_player_with_nickcname(nombre)
    except Exception as e:
        st.error(e)
        st.stop()

    if player is None:
        st.error("El usuario no existe.")
    else:
        idplayer = player[0]
        passw = player[2]
        name = player[1]

        if contraseña == passw:
            st.success("Successful")
            st.session_state["player_id"] = idplayer
        else:
            st.error("Contraseña incorrecta.")

