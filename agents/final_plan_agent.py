
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


def final_plan_agent(state: TravelState) -> dict:

    system_prompt = """
    You are an expert AI travel planner.

    Your task is to combine:
    - destination research
    - itinerary
    - budget breakdown

    into ONE beautiful, organized, traveler-friendly final report.

    The final response should:
    - be clean and well-structured
    - use headings and emojis
    - be practical and easy to read
    - summarize important information clearly
    - feel like a professional travel guide

    Keep formatting neat and modern.
    """

    human_prompt = f"""
    Create a complete final travel plan using the information below.

    Destination: {state["destination"]}
    Days: {state["days"]}
    Travelers: {state["people"]}
    Budget Type: {state["budget"]}

    Research Information:
    {state["research"]}

    Itinerary:
    {state["itinerary"]}

    Budget Breakdown:
    {state["budget_breakdown"]}

    Format the response EXACTLY like this:

    🌍 Travel Plan: [Destination] ([Days] Days, [People] People)

    📋 DESTINATION OVERVIEW
    - Include best time to visit
    - Top attractions
    - Local food
    - Cultural tips

    🗓️ DAY BY DAY ITINERARY
    - Day-wise travel plan

    💰 BUDGET BREAKDOWN
    - Accommodation
    - Food
    - Transport
    - Activities
    - Miscellaneous
    - Total cost in INR

    ✅ TRAVEL TIPS
    - Important travel advice
    - Packing tips
    - Safety tips
    - Local etiquette
    """

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=human_prompt)
    ]

    response = llm.invoke(messages)

    return {
        "final_plan": response.content
    }
