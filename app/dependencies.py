from langchain_openai import ChatOpenAI
from app.config import MODEL_NAME, TEMPERATURE


def llm():
    """Initialzed the model"""
    return ChatOpenAI(model=MODEL_NAME, temperature=TEMPERATURE)
