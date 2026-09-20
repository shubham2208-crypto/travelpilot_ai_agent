def find_alternative_activity(current_activity_name, destination):
    from utils.helpers import load_data_file
    activities = load_data_file("activities.json")
    for a in activities:
        if a["destination"].lower() == destination.lower() and a["name"].lower() != current_activity_name.lower():
            return a
    return {"name": "Local City Park Stroll", "cost": 0, "category": "Nature"}