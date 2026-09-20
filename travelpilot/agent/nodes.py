from services.planner import generate_full_itinerary
from tools.budget_tool import calculate_trip_cost
from tools.conflict_tool import detect_schedule_conflicts

def parse_request_node(state):
    state["audit_log"].append("Parsed user trip requirements successfully.")
    state["status"] = "Parsing"
    return state

def create_goal_node(state):
    state["audit_log"].append(f"Created trip goal for destination: {state['destination']}.")
    state["status"] = "Goal Created"
    return state

def retrieve_data_node(state):
    state["transportation"] = {"type": "Flight", "cost": 350, "status": "Confirmed"}
    state["accommodation"] = {"name": "Central Hotel", "cost": 500, "status": "Confirmed"}
    state["audit_log"].append("Retrieved hotels, transport, and destination profiles.")
    return state

def generate_activities_node(state):
    state["itinerary"] = generate_full_itinerary(
        state["destination"], state["start_date"], state["end_date"], state["interests"]
    )
    state["audit_log"].append(f"Generated day-by-day itinerary spanning {len(state['itinerary'])} days.")
    return state

def calculate_budget_node(state):
    state["costs"] = calculate_trip_cost(state["itinerary"], state["accommodation"]["cost"], state["transportation"]["cost"])
    state["audit_log"].append(f"Calculated total estimated cost: {state['costs']['total']}.")
    return state

def detect_conflicts_node(state):
    state["conflicts"] = detect_schedule_conflicts(state["itinerary"])
    state["audit_log"].append(f"Conflict check completed. Found {len(state['conflicts'])} issues.")
    state["status"] = "Ready"
    return state