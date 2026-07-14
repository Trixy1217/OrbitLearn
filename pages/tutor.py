import streamlit as st
from llms.gemma2b import model_gemma2b
from llms.smollm2 import model_smollm2
from prompts.tutorsimpleprompt import SYSTEMPROMPT, SYSTEMPROMPT_DESICION
from langchain_core.prompts import PromptTemplate
from rag.retriever import retrieve_context
from src.database.player_repository import get_player
from langchain_core.messages import AIMessage,SystemMessage, HumanMessage
from llms.gemini import gemini_model
import json


#llm = model_gemma2b()

llm = gemini_model()

llmdecision = gemini_model()


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

  
  #  best_score = results[0][1]

  #  if best_score < 0.35:
  #       use_context = True

  #  else:
  #       use_context = False


         ## QUE EL LLM TOME LA DECISIÓN UNN LLM MAS PEQUEÑO DEA CUERDO AL SYSTEM PROMPT


    

  #  prompt_template = PromptTemplate.from_template(SYSTEMPROMPT)
   # string = prompt_template.format(clase = clase,context = context, question =query)


    with st.chat_message("user"):
        st.write(query)

   
    with st.chat_message("assistant"):
         
         placeholder = st.empty()
         

         placeholder.write("Pensando...")

         decision_messages = [
        SystemMessage(content=SYSTEMPROMPT_DESICION),
        HumanMessage(content=query)
        ]

         response_decision = llmdecision.invoke(decision_messages)


                
         if response_decision.content == "RAG":
                  results = retrieve_context(current_id, query)

                  context = "\n\n".join(
                     doc.page_content for doc, score in results
                  )

                  messages = [SystemMessage(content=SYSTEMPROMPT.format(clase=clase)),
                            HumanMessage(
                                content=f"""CONTEXTO:
                                        {context}

                                        PREGUNTA:
                                        {query}
                                        """
                                        )] 

                  response = llm.invoke(messages) 

         if response_decision.content == "NORAG":
                    context = None
              
                    response = llm.invoke(query) 




         st.session_state.messages.append(

         {
            "role": "assistant",
            "content": response.content
         }
    )




         placeholder.write(response.content)
         placeholder.write(response_decision.content)


     
    player_id = st.session_state.get("player_id")
    player = get_player(player_id)

   
    



    if context:
      st.success(context)





   

    


