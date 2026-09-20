import streamlit as st
from agent.graph import build_travel_graph
from tools.disruption_tool import find_alternative_activity

st.set_page_config(
    page_title="TravelPilot — Intelligent Trip Planning",
    page_icon="✈️",
    layout="wide"
)

# Custom CSS for clean & modern attractive look
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #e03e3e;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "trip_state" not in st.session_state:
    st.session_state.trip_state = {
        "destination": "Paris",
        "start_date": "2026-10-10",
        "end_date": "2026-10-15",
        "budget": 1500.0,
        "interests": ["Culture", "Food"],
        "preferences": "Balanced",
        "transportation": {},
        "accommodation": {},
        "itinerary": [],
        "costs": {},
        "conflicts": [],
        "audit_log": [],
        "disruption_active": False,
        "status": "Idle"
    }

# Sidebar Styling
st.sidebar.markdown("## ✈️ TravelPilot Control")
st.sidebar.markdown("---")
destination = st.sidebar.text_input("🌍 Destination City", value="Paris")
budget = st.sidebar.number_input("💰 Budget (€)", value=1500, step=50)
start_date = st.sidebar.date_input("📅 Start Date")
end_date = st.sidebar.date_input("📅 End Date")
interests = st.sidebar.multiselect("🎯 Interests", ["Culture", "Food", "Shopping", "Nature", "Museums"], default=["Culture", "Food"])

st.sidebar.markdown("---")
if st.sidebar.button("🚀 Generate Itinerary"):
    with st.spinner("Agent is planning your trip..."):
        graph = build_travel_graph()
        initial_state = {
            "destination": destination,
            "start_date": str(start_date),
            "end_date": str(end_date),
            "budget": float(budget),
            "interests": interests,
            "preferences": "Balanced",
            "transportation": {},
            "accommodation": {},
            "itinerary": [],
            "costs": {},
            "conflicts": [],
            "audit_log": [],
            "disruption_active": False,
            "status": "Initializing"
        }
        final_state = graph.invoke(initial_state)
        st.session_state.trip_state = final_state
    st.sidebar.success("Itinerary generated successfully!")

# Main Dashboard Header
st.title("✈️ TravelPilot")
st.markdown("#### *Intelligent Trip Planning & Disruption Management Agent*")
st.markdown("---")

state = st.session_state.trip_state

if state["itinerary"]:
    # Metrics Row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("🌍 Destination", state["destination"])
    with col2:
        st.metric("💳 Total Budget", f"€{state['budget']}")
    with col3:
        st.metric("💸 Estimated Cost", f"€{state['costs'].get('total', 0)}")
    with col4:
        remaining = state["budget"] - state["costs"].get('total', 0)
        st.metric("💰 Remaining", f"€{remaining}", delta=f"€{remaining}")

    st.markdown("---")
    st.markdown("### 📅 Day-by-Day Itinerary")
    
    for day in state["itinerary"]:
        with st.expander(f"🗓️ Day {day['day']} — {day['date']}", expanded=True if day['day'] == 1 else False):
            for item in day["schedule"]:
                st.markdown(f"**⏰ {item['time']}** &nbsp;|&nbsp; 🏷️ **{item['name']}** *({item['category']})* &nbsp;|&nbsp; 💶 **€{item['cost']}**")

    st.markdown("---")
    st.markdown("### ⚡ Disruption Management Simulator")
    col_sim, col_desc = st.columns([1, 2])
    with col_sim:
        if st.button("⚠️ Simulate Disruption"):
            state["disruption_active"] = True
            state["audit_log"].append("Disruption Detected: Primary activity cancelled unexpectedly.")
            alt = find_alternative_activity("Museum", state["destination"])
            state["audit_log"].append(f"Alternative selected & replanned: {alt['name']}")
            if len(state["itinerary"]) > 0 and len(state["itinerary"][0]["schedule"]) > 1:
                state["itinerary"][0]["schedule"][1]["name"] = f"{alt['name']} (Replacement)"
                state["itinerary"][0]["schedule"][1]["cost"] = alt["cost"]
            st.success(f"Disruption handled! Replaced with **{alt['name']}**.")
    with col_desc:
        st.info("Is button par click karke aap check kar sakte hain ki agar koi attraction cancel ho jaye, toh agent kaise real-time mein replanning karta hai.")

    st.markdown("---")
    st.markdown("### 🤖 Agent Audit Trail & Reasoning Log")
    with st.expander("🔍 View Live Agent Execution Logs"):
        for log in state["audit_log"]:
            st.text(f"• {log}")
else:
    st.info("👈 Apni trip ki details sidebar mein enter karein aur **Generate Itinerary** button par click karein.")

st.markdown("---")
st.caption("Demo uses synthetic travel data. Prices, availability, and schedules are simulated.")