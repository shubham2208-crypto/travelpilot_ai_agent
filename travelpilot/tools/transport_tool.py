from utils.helpers import load_data_file

def get_transportation(destination: str, transport_type: str = None):
    """Returns available flights, trains, or local transportation options."""
    transports = load_data_file("transportation.json")
    filtered = [t for t in transports if t["destination"].lower() == destination.lower()]
    if transport_type:
        filtered = [t for t in filtered if t["type"].lower() == transport_type.lower()]
    return filtered