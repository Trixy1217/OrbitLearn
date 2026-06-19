from rag.vectorstore import load_vectorstore

db = load_vectorstore()

def retrieve_context(query:str, k: int = 3):

    return db.similarity_search(query, k=k)