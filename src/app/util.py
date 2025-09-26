import json
from collections import OrderedDict


def load_json(filepath: str):
    print("DEBUG loading file:", filepath)
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f, object_pairs_hook=OrderedDict)


def save_json(file_path: str, data):
    """Save JSON data to a file."""
    with open(file_path, 'w', encoding="utf-8") as file:
        json.dump(data, file, indent=2)
