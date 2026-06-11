# agents/state.py
from typing import TypedDict

class TravelState(TypedDict):
    destination: str
    days: int
    budget: str
    people: int
    research: str
    itinerary: str
    budget_breakdown: str
    final_plan: str