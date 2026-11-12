
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


def budget_agent(state: TravelState) -> dict:
    system_prompt = """
    You are an expert travel budget agent.

    Your responsibilities:
    - Create a budget breakdown for the itinerary
    - Ensure the itinerary is feasible within the given days and budget
    - Keep the response concise and actionable
    - Give costs in Indian Rupees (INR)
    - Format the response as a bulleted list with:
      Accommodation
      Food
      Transport
      Activities
      Shopping/Miscellaneous
      Total Estimated Cost

    Also include:
    - Cost per person
    - Total cost for all travelers
    """

    human_prompt = f"""
    Create a budget breakdown for this travel destination.

    Destination: {state["destination"]}
    Days: {state["days"]}
    Budget: {state["budget"]}
    Number of People: {state["people"]}
    Research: {state["research"]}
    Itinerary: {state["itinerary"]}
    """

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=human_prompt)
    ]

    response = llm.invoke(messages)

    return {
        "budget_breakdown": response.content
    }
