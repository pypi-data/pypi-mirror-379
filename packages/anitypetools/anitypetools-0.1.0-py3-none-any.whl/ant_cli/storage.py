import json
import os

CONFIG_PATH = os.path.expanduser("~/.ant_profiles.json")

def load_storage():
    if not os.path.exists(CONFIG_PATH):
        data = {"current": "default", "profiles": {"default": {}}}
        save_storage(data)
        return data

    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_storage(data):
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def get_current_profile(data):
    return data["current"], data["profiles"].setdefault(data["current"], {})

# 🔑 удобные функции для кода
def get_value(key, default=None):
    data = load_storage()
    _, profile = get_current_profile(data)
    return profile.get(key, default)

def set_value(key, value):
    data = load_storage()
    current, profile = get_current_profile(data)
    profile[key] = value
    save_storage(data)
    return current, key, value