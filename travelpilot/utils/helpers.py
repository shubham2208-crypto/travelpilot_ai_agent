import json

def load_data_file(filename):
    try:
        with open(f"data/{filename}", "r") as f:
            return json.load(f)
    except Exception:
        return []