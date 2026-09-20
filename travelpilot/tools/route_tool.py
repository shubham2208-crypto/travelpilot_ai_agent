import math

def calculate_distance(lat1, lon1, lat2, lon2):
    """Calculates distance between two coordinates in kilometers using Haversine approximation."""
    R = 6371.0 # Earth radius in km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
    c = 2 * math.asin(math.sqrt(a))
    return R * c

def get_travel_time(lat1, lon1, lat2, lon2, mode="transit"):
    """Estimates travel time in minutes between two locations based on distance."""
    dist = calculate_distance(lat1, lon1, lat2, lon2)
    # Average urban transit speed ~ 20 km/h
    speed_kmh = 20.0 if mode == "transit" else 15.0
    hours = dist / speed_kmh
    return max(int(hours * 60), 15) # Minimum 15 mins travel time

def optimize_route(activities_list):
    """Attempts to minimize unnecessary travel by sorting activities by spatial coordinates."""
    if not activities_list:
        return []
    # Simple nearest-neighbor sorting or sorting by latitude/longitude cluster
    return sorted(activities_list, key=lambda x: (x.get("latitude", 0), x.get("longitude", 0)))