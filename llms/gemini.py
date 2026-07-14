from dotenv import load_dotenv
import os


load_dotenv()


from langchain_google_genai import ChatGoogleGenerativeAI

def gemini_model():
    llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY2")
    )

    return llm




