from utils.helpers import load_data_file

def get_activities(destination: str, category: str = None):
    """Returns available attractions and activities for a destination."""
    activities = load_data_file("activities.json")
    filtered = [a for a in activities if a["destination"].lower() == destination.lower()]
    if category:
        filtered = [a for a in filtered if a["category"].lower() == category.lower()]
    return filtered

def check_activity_availability(activity_name: str) -> bool:
    """Checks whether a specific activity is available."""
    activities = load_data_file("activities.json")
    for a in activities:
        if a["name"].lower() == activity_name.lower():
            return a.get("availability", True)
    return True