from langchain_community.vectorstores import Chroma
from rag.embeddings import getembeddings

def create_vectorstore(chunks):

    embeddings = getembeddings()
    
    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )


    """  OPCIONAL:  TENER EN CUENTA PARA LA SEGUNDA VERSIÓN DE ASOCIAR UNA COLECCIÓN COMO INDICE CON UN JUGADOR

    ACTUALIZACIÓN: YA NO TENER EN CUENTA LA IMPLEMENTACIÓN PERO MANTENER COMO POSIBLE CAMBIO
    
    def create_vectorstore(chunks, player_name):

    embeddings = getembeddings()

    db = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        persist_directory="./chroma_db",
        collection_name=f"player_{player_name}"
    )
   """
    return db


def load_vectorstore():
    embeddings = getembeddings()

    return Chroma(persist_directory="./chroma_db",
                  embedding_function=embeddings
                  )