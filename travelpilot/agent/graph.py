from langgraph.graph import StateGraph, END
from agent.state import TravelState
from agent.nodes import (
    parse_request_node, create_goal_node, retrieve_data_node,
    generate_activities_node, calculate_budget_node, detect_conflicts_node
)

def build_travel_graph():
    workflow = StateGraph(TravelState)
    
    workflow.add_node("parse_request", parse_request_node)
    workflow.add_node("create_goal", create_goal_node)
    workflow.add_node("retrieve_data", retrieve_data_node)
    workflow.add_node("generate_activities", generate_activities_node)
    workflow.add_node("calculate_budget", calculate_budget_node)
    workflow.add_node("detect_conflicts", detect_conflicts_node)
    
    workflow.set_entry_point("parse_request")
    workflow.add_edge("parse_request", "create_goal")
    workflow.add_edge("create_goal", "retrieve_data")
    workflow.add_edge("retrieve_data", "generate_activities")
    workflow.add_edge("generate_activities", "calculate_budget")
    workflow.add_edge("calculate_budget", "detect_conflicts")
    workflow.add_edge("detect_conflicts", END)
    
    return workflow.compile()