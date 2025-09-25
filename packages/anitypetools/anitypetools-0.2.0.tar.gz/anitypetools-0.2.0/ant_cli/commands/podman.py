import subprocess
from ant_cli import storage
from ant_cli.utils import pprint

def execute(params):
    if not params:
        pprint("Usage: ant pm <build|push> <image>")
        return

    action = params[0]

    if action == "build":
        if len(params) < 2:
            print("Usage: ant pm build <image>")
            return

        image = params[1]
        full_tag = f"{image}:latest"

        pprint(f"[ant] podman build -t {full_tag} .")
        subprocess.run(["podman", "build", "-t", full_tag, "."])

    elif action == "push":
        if len(params) < 2:
            print("Usage: ant pm push <image>")
            return

        image = params[1]
        repo = storage.get_value("repo")

        if not repo:
            pprint("Error: repo not set. Use 'ant set repo <name>' first.")
            return

        src_tag = f"{image}:latest"
        dst_tag = f"{repo}/{image}:latest"

        pprint(f"[ant] podman push {src_tag} {dst_tag}")
        subprocess.run(["podman", "push", src_tag, dst_tag])

    else:
        pprint(f"Unknown podman command: {action}")