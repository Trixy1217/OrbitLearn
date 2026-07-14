import streamlit as st
import tempfile
from rag.pdfloader import pdfloader

from src.database.player_repository import create_player, get_player
from rag.vectorstore import create_vectorstore


st.set_page_config(
    page_title="OrbitLearn",
    page_icon="🚀",
    layout="centered")


col1,hero = st.columns([3,2])



st.title("WAIT!, do you have any pdf document of your teacher of it could add information")

pdf_file = st.file_uploader(
    "Select your pdf file: ",
    type=["pdf"]
    )
if pdf_file is not None:
     st.success(f"Archivo cargado: {pdf_file.name}")
     
     #leer contenido en bytes



with col1:
        st.title("Coach for tech students")

        nombre = st.text_input("Nickname of character")

        contraseña = st.text_input("Password of character")
 

        clase = st.selectbox("Choose your class:",["Backend","Frontend","Data", "Cybersecurity"])
        


        if st.button("Create a player"):
            
         


            creator = create_player(nombre,contraseña,clase)
            if creator:
               
               if pdf_file is not None:
                 
                 with tempfile.NamedTemporaryFile(
                      delete=False,
                      suffix=".pdf"
                 ) as temp_pdf:
                      
                      temp_pdf.write(pdf_file.getbuffer())

                      pdf_path = temp_pdf.name


                 chunks,current_id= pdfloader(pdf_path,nombre)

                 vector_store =  create_vectorstore(chunks)

                 if chunks:
                     st.session_state["player_id"] = current_id
                     st.success(f"User has been created. ID: {current_id}")


                 if vector_store:
                     
                     st.success("Vector has been created")

                 else:
                     st.error("ERROR: Creating vector")






                 st.success(
            f"PDF procesado correctamente. Se generaron {len(chunks)} chunks."
                 )

                 st.write(chunks[:3])
               
                 
               st.success(f"{nombre} has been created with class: {clase}")

            
            
            
               """RECORDAR MEJORAR EL SWITCHPAGE PARA TEMAS DE ERRORES"""


               st.switch_page("pages/03-cuestionario_vak_tdah.py")



            
            elif creator == False:
                 
                st.error(f"Currently exist a problem")

                 

        if st.button("I have a account"):
            st.switch_page("pages/02-login.py")

                 
                 



        


st.divider()

hero = st.container()

with hero:
    st.image("img/character.png", width=180)
    st.title("OrbitLearn")
    st.caption("Aprende mientras avanzas en tu aventura")

st.subheader("Jugadores registrados:")

players = get_player(4)

st.write(players)


