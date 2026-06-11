from typing import TypedDict

from langgraph.graph import StateGraph, START, END
from agents.state import TravelState

from agents.research_agent import research_agent
from agents.itinerary_agent import itinerary_agent
from agents.budget_agent import budget_agent
from agents.final_plan_agent import final_plan_agent


# ---------------- GRAPH BUILDER ---------------- #

def build_graph():

    builder = StateGraph(TravelState)

    # Nodes
    builder.add_node("research", research_agent)
    builder.add_node("itinerary", itinerary_agent)
    builder.add_node("budget", budget_agent)
    builder.add_node("final_plan", final_plan_agent)

    # Flow
    builder.add_edge(START, "research")
    builder.add_edge("research", "itinerary")
    builder.add_edge("itinerary", "budget")
    builder.add_edge("budget", "final_plan")
    builder.add_edge("final_plan", END)

    graph = builder.compile()

    return graph