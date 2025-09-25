import sys
from ant_cli.commands import version, set_value, get_value, change_prof, list_profiles, podman, docker

COMMANDS = {
    "v": version.show,
    "version": version.show,
    "set": set_value.execute,
    "get": get_value.execute,
    "prof": change_prof.execute,
    "ls": list_profiles.execute,
    "pm": podman.execute,
    "dk": docker.execute,
}

def main():
    args = sys.argv[1:]
    if not args:
        print("ant CLI. Use 'ant v', 'ant run <script.py>', 'ant gs'.")
        return

    cmd, *params = args
    if cmd in COMMANDS:
        COMMANDS[cmd](params)
    else:
        print("Unknown command:", cmd)
