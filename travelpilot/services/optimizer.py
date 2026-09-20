def optimize_activities(activities):
    # Sort or cluster activities by coordinates to minimize travel distance
    return sorted(activities, key=lambda x: x.get("latitude", 0))