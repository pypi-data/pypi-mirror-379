from ant_cli import storage

def execute(params):
    if not params:
        print("Usage: ant get <key>")
        return

    key = params[0]

    data = storage.load_storage()
    current, profile = storage.get_current_profile(data)

    if key in profile:
        print(profile[key])
    else:
        print(f"[{current}] key '{key}' not found")
