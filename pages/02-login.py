import streamlit as st
from src.database.player_repository import login_user



st.title("Coach for tech students")

nombre = st.text_input("Nickname of character")

contraseña = st.text_input("Write your password", type="password"
)

if st.button("LOGIN"):

    if not nombre:
        st.error("Nickname is required.")

    elif not contraseña:
        st.error("Password is required.")

    elif login_user(nombre, contraseña):
        st.success(f"Welcome {nombre}")
        # st.switch_page()

    else:
        st.error("Invalid username or password.")

      

   

