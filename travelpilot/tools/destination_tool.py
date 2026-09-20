from utils.helpers import load_data_file

def get_destination_data(destination_name):
    destinations = load_data_file("destinations.json")
    for d in destinations:
        if d["name"].lower() == destination_name.lower():
            return d
    return {"name": destination_name, "country": "Unknown", "currency": "USD", "description": "Custom destination"}