from ant_cli import storage

def execute(params):
    data = storage.load_storage()
    current = data["current"]

    print("Profiles:")
    for name in data["profiles"]:
        marker = "*" if name == current else " "
        print(f"{marker} {name}")
