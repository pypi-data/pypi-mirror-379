from ant_cli import storage
from ant_cli.utils import pprint

def execute(params):
    data = storage.load_storage()
    current = data["current"]

    pprint("Profiles:", False)
    for name in data["profiles"]:
        marker = "*" if name == current else " "
        pprint(f"{marker} {name}", False)
