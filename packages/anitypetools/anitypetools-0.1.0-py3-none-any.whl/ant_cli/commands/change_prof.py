from ant_cli import storage

def execute(params):
    if not params:
        print("Usage: ant prof <name>")
        return

    name = params[0]

    data = storage.load_storage()
    if name not in data["profiles"]:
        data["profiles"][name] = {}
        print(f"Created new profile '{name}'")

    data["current"] = name
    storage.save_storage(data)

    print(f"Switched to profile '{name}'")
