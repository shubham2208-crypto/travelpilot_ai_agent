def calculate_trip_cost(itinerary, accommodation_cost, transport_cost):
    activities_total = sum(item["cost"] for day in itinerary for item in day["schedule"])
    total_cost = activities_total + accommodation_cost + transport_cost
    return {
        "activities": activities_total,
        "accommodation": accommodation_cost,
        "transportation": transport_cost,
        "food": 200,
        "miscellaneous": 50,
        "total": total_cost + 250
    }