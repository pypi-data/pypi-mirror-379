from colorama import Fore, Style
from ant_cli import storage

def pprint(message: str, with_profile: bool = True):
    if with_profile:
        data = storage.load_storage()
        current, _ = storage.get_current_profile(data)
        prefix = f"[{current}]"
        print(Fore.LIGHTGREEN_EX + prefix + Style.RESET_ALL, message)
    else:
        print(message)