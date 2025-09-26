from ant_cli.utils import pprint
from ant_cli import storage

def execute(params):
    if len(params) < 2:
        pprint("Usage: ant set <key> <value>")
        return

    key, value = params[0], params[1]

    data = storage.load_storage()
    _, profile = storage.get_current_profile(data)

    profile[key] = value
    storage.save_storage(data)

    pprint(f"{key} = {value}")
