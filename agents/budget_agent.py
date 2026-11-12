from dotenv import load_dotenv
from typing import TypedDict
from agents.state import TravelState
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

# Load environment variables
load_dotenv()




# Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    temperature=0.3
)

def budget_agent(state: TravelState) -> dict:
    system_prompt = """
    You are an expert travel budget agent.

    Your responsibilities:
    - Create a budget breakdown for the itinerary
    - Ensure the itinerary is feasible within the given days and budget
    - Keep the response concise and actionable
    -give costs in Indian Rupees since you're in India as we r making a travel agent for indian people who want to travel to other states of india or to other so indian pepople need cost in indian rupees to undertand the costs.
    - Format the response as a bulleted list with the following categories:
    🏠 Accommodation
    🍜 Food
    🚗 Transport
    🎯 Activities
    🛍️ Shopping/Miscellaneous
    💰 Total Estimated cost
    
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


