
import os
import streamlit as st

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq


def get_llm(gemini_model):
    try:
        groq_key = st.secrets.get("GROQ_API_KEY")
    except Exception:
        groq_key = os.getenv("GROQ_API_KEY")

    if not groq_key:
        raise ValueError("GROQ_API_KEY is missing from Streamlit Secrets")

    gemini = ChatGoogleGenerativeAI(
        model=gemini_model,
        temperature=0.3
    )

    groq = ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0.3,
        api_key=groq_key
    )

    return gemini.with_fallbacks([groq])
