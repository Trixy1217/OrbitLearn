from rag.vectorstore import load_vectorstore

db = load_vectorstore()

def retrieve_context(current_id, query:str, k: int = 3):




    return db.similarity_search_with_score(query, k=k, filter={"user_id": current_id})