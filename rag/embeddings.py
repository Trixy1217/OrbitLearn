from langchain_ollama import OllamaEmbeddings

def getembeddings():
    return OllamaEmbeddings(model="nomic-embed-text")

