from utils.helpers import load_data_file

def get_hotels(destination: str, max_price: float = None):
    """Returns available hotels matching the destination and optional budget."""
    hotels = load_data_file("hotels.json")
    filtered = [h for h in hotels if h["destination"].lower() == destination.lower()]
    if max_price:
        filtered = [h for h in filtered if h["price_per_night"] <= max_price]
    return filtered