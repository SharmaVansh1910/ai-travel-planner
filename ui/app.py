import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import streamlit as st
from graph.travel_graph import build_graph

# ---------------- UI CONFIG ---------------- #
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 AI Multi-Agent Travel Planner")


# ---------------- SIDEBAR ---------------- #
with st.sidebar:
    st.header("✈️ Trip Details")

    destination = st.text_input("Destination")
    days = st.number_input("Number of Days", min_value=1, max_value=30, value=5)
    budget = st.selectbox("Budget Type", ["Budget", "Moderate", "Luxury"])
    people = st.number_input("Number of People", min_value=1, max_value=10, value=2)

    run_btn = st.button("🚀 Plan My Trip")


# ---------------- MAIN LOGIC ---------------- #
final_state = None

if run_btn:

    # Initial state
    initial_state = {
        "destination": destination,
        "days": days,
        "budget": budget,
        "people": people,
        "research": "",
        "itinerary": "",
        "budget_breakdown": "",
        "final_plan": ""
    }

    # Build graph
    graph = build_graph()

    status = st.empty()

    with st.spinner("🤖 Planning your trip..."):

        status.info("🔍 Researching destination...")
        status.info("🗓️ Creating itinerary...")
        status.info("💰 Calculating budget...")
        status.info("✍️ Writing final plan...")

        # IMPORTANT: get FULL final state
        final_state = graph.invoke(initial_state)

    status.success("✅ Travel plan ready!")


# ---------------- OUTPUT ---------------- #
if final_state:

    tab1, tab2, tab3, tab4 = st.tabs([
        "📋 Research",
        "🗓️ Itinerary",
        "💰 Budget",
        "🌍 Final Plan"
    ])

    with tab1:
        st.markdown(final_state["research"])

    with tab2:
        st.markdown(final_state["itinerary"])

    with tab3:
        st.markdown(final_state["budget_breakdown"])

    with tab4:
        st.markdown(final_state["final_plan"])
        
        
        
        
        
#next changes
# import streamlit as st
# from graph.travel_graph import build_graph

# st.set_page_config(page_title="AI Travel Chat", page_icon="🌍")

# st.title("🌍 AI Travel Assistant (Chat Mode)")

# # Initialize session state
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# if "state" not in st.session_state:
#     st.session_state.state = {
#         "destination": "",
#         "days": 0,
#         "budget": "",
#         "people": 1,
#         "research": "",
#         "itinerary": "",
#         "budget_breakdown": "",
#         "final_plan": ""
#     }

# graph = build_graph()

# # Show chat history
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(msg["content"])

# # User input
# user_input = st.chat_input("Tell me your travel plan...")

# if user_input:

#     # Show user message
#     st.session_state.messages.append({"role": "user", "content": user_input})
#     with st.chat_message("user"):
#         st.markdown(user_input)

#     # Update state intelligently (simple version first)
#     state = st.session_state.state

#     # VERY SIMPLE PARSING (we improve later)
#     if "goa" in user_input.lower():
#         state["destination"] = "Goa"

#     if "day" in user_input.lower():
#         import re
#         nums = re.findall(r"\d+", user_input)
#         if nums:
#             state["days"] = int(nums[0])

#     if "budget" in user_input.lower():
#         if "luxury" in user_input.lower():
#             state["budget"] = "Luxury"
#         elif "budget" in user_input.lower():
#             state["budget"] = "Budget"
#         else:
#             state["budget"] = "Moderate"

#     # Run graph
#     with st.spinner("Planning your trip..."):
#         result = graph.invoke(state)
#         st.session_state.state = result

#     # Show AI response (final plan)
#     response = result["final_plan"]

#     st.session_state.messages.append({"role": "assistant", "content": response})

#     with st.chat_message("assistant"):
#         st.markdown(response) 