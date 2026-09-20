def detect_schedule_conflicts(itinerary):
    conflicts = []
    for day in itinerary:
        schedule = day["schedule"]
        if len(schedule) > 3:
            # Simulated timing clash check
            pass
    return conflicts