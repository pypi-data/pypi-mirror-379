from ant_cli import storage
from ant_cli.utils import pprint

def execute(params):
    if not params:
        pprint("Usage: ant get <key>")
        return

    key = params[0]

    data = storage.load_storage()
    _, profile = storage.get_current_profile(data)

    if key in profile:
        pprint(profile[key])
    else:
        pprint(f"key '{key}' not found")
