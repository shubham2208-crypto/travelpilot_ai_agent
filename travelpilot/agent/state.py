from typing import TypedDict, List, Dict, Any

class TravelState(TypedDict):
    destination: str
    start_date: str
    end_date: str
    budget: float
    interests: List[str]
    preferences: str
    transportation: Dict[str, Any]
    accommodation: Dict[str, Any]
    itinerary: List[Dict[str, Any]]
    costs: Dict[str, float]
    conflicts: List[str]
    audit_log: List[str]
    disruption_active: bool
    status: str