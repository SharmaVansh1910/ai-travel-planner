
from dotenv import load_dotenv
from typing import TypedDict
from agents.state import TravelState
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
import streamlit as st

load_dotenv()

# Groq fallback model
groq_llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.3,
    api_key=st.secrets["GROQ_API_KEY"]
)

# Gemini first, Groq if Gemini fails
llm = gemini_llm.with_fallbacks([groq_llm])


def research_agent(state: TravelState) -> dict:

    system_prompt = """
    You are an expert travel research agent.

    Your responsibilities:
    - Research the destination
    - Mention best time to visit
    - Suggest top attractions
    - Recommend local foods
    - Share cultural tips
    - Keep the response concise and informative
    """

    human_prompt = f"""
    Research this travel destination.

    Destination: {state["destination"]}
    Days: {state["days"]}
    Budget: {state["budget"]}
    Number of People: {state["people"]}
    """

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=human_prompt)
    ]

    response = llm.invoke(messages)

    return {
        "research": response.content
    }
