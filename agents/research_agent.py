from dotenv import load_dotenv
from typing import TypedDict
from agents.state import TravelState
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

# Load environment variables
load_dotenv()



# Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0.3
)


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
