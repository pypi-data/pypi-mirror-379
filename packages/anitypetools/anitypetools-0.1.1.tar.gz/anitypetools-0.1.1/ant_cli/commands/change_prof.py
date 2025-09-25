from ant_cli import storage
from ant_cli.utils import pprint

def execute(params):
    if not params:
        pprint("Usage: ant prof <name>")
        return

    name = params[0]

    data = storage.load_storage()
    if name not in data["profiles"]:
        data["profiles"][name] = {}
        pprint(f"Created new profile '{name}'", False)

    data["current"] = name
    storage.save_storage(data)

    pprint(f"Switched to profile '{name}'", False)
