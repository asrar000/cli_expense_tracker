import json
import os

DATA_FILE = "data/expenses.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"version": 1, "expenses": []}

    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except Exception:
        raise IOError("Failed to read data file")

def save_data(data):
    os.makedirs("data", exist_ok=True)
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)
    except Exception:
        raise IOError("Failed to write data file")
