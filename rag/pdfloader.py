from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.database.player_repository import get_id_player_with_nickname


def pdfloader(path: str, nombre: str):

    try:
            # 1. Cargar PDF
            pdf_loader = PyPDFLoader(path)
            documents = pdf_loader.load()
            current_id = get_id_player_with_nickname(nombre)


            # 2. Split (SIN perder metadata)
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )

            chunks = splitter.split_documents(documents)

            # 3. Agregar metadata propia
            for i, chunk in enumerate(chunks):
                chunk.metadata.update({
                    "user_id": current_id,
                    "chunk_index": i
                })

            oe = chunks[0].metadata["user_id"]  
            kind = type(oe)

            return chunks,current_id
    except Exception as e:
          print("PDFLOADER ERROR:", e)
          return  None