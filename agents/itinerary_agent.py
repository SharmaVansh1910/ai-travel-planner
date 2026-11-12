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

def itinerary_agent(state: TravelState) -> dict:
    system_prompt = """
    You are an expert travel itinerary agent.

    Your responsibilities:
    - Create a day-by-day format  itinerary like morning,afternoon,evening and night based on the research
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
