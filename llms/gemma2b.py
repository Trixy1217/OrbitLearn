from langchain_ollama import ChatOllama

def model_gemma2b():

    llm = ChatOllama(model="gemma:2b")


    return llm


