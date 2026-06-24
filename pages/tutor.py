import streamlit as st
from llms.gemma2b import model_gemma2b
from prompts.tutorsimpleprompt import SYSTEMPROMPT, SYSTEMPROMPT1
from langchain_core.prompts import PromptTemplate
from rag.retriever import retrieve_context
from src.database.player_repository import get_player
from langchain_core.messages import AIMessage,SystemMessage, HumanMessage


llm = model_gemma2b()


st.title("📚 Tutor AI")

if "messages" not in st.session_state:
    st.session_state.messages = []


for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

query = st.chat_input("Haz una pregunta al tutor...")


if query:
  

    st.session_state.messages.append(

        {
            "role": "user",
            "content": query
        }
    )
    clase = "backend"

    current_id = 1
    clase = "backend"

    results = retrieve_context(current_id, query)

    context = "\n\n".join(
        doc.page_content for doc, score in results
    )

    best_score = results[0][1]

    if best_score < 0.35:
         use_context = True

    else:
         use_context = False


    

  #  prompt_template = PromptTemplate.from_template(SYSTEMPROMPT)
   # string = prompt_template.format(clase = clase,context = context, question =query)


    with st.chat_message("user"):
        st.write(query)

   
    with st.chat_message("assistant"):
         
         placeholder = st.empty()
         

         placeholder.write("Pensando...")

         responselite = llm.invoke(SYSTEMPROMPT1.format(clase = clase, query=query)) 
            
            
         if use_context == True:
                messages = [SystemMessage(content=SYSTEMPROMPT.format(clase=clase)),
                            HumanMessage(
                                content=f"""CONTEXTO:
                                        {context}

                                        PREGUNTA:
                                        {query}
                                        """
                                        )] 

                response = llm.invoke(messages) 

         if use_context == False:
              
                    response = llm.invoke(query) 




         st.session_state.messages.append(

         {
            "role": "assistant",
            "content": response.content
         }
    )




         placeholder.write(response.content)

     
    player_id = st.session_state.get("player_id")
    player = get_player(player_id)

   
    



    st.success(context)





   

    


