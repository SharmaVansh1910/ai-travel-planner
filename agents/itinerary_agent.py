
from dotenv import load_dotenv
import streamlit as st
from agents.state import TravelState
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.3,
    api_key=st.secrets["GROQ_API_KEY"]
)


def itinerary_agent(state: TravelState) -> dict:
    system_prompt = """
    You are an expert travel itinerary agent.

    Your responsibilities:
    - Create a day-by-day format itinerary like morning,
      afternoon, evening and night based on the research
    - Ensure the itinerary is feasible within the given days and budget
    - Keep the response concise and actionable
    """

    human_prompt = f"""
    Create an itinerary for this travel destination.

    Destination: {state["destination"]}
    Days: {state["days"]}
    Budget: {state["budget"]}
    Number of People: {state["people"]}
    Research: {state["research"]}
    """

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=human_prompt)
    ]

    response = llm.invoke(messages)

    return {
        "itinerary": response.content
    }
