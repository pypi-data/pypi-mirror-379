import subprocess
from ant_cli import storage

def execute(params):
    if not params:
        print("Usage: ant pm <build|push> <image>")
        return

    action = params[0]

    if action == "build":
        if len(params) < 2:
            print("Usage: ant pm build <image>")
            return

        image = params[1]
        full_tag = f"{image}:latest"

        print(f"[ant] podman build -t {full_tag} .")
        subprocess.run(["podman", "build", "-t", full_tag, "."])

    elif action == "push":
        if len(params) < 2:
            print("Usage: ant pm push <image>")
            return

        image = params[1]
        repo = storage.get_value("repo")

        if not repo:
            print("Error: repo not set. Use 'ant set repo <name>' first.")
            return

        src_tag = f"{image}:latest"
        dst_tag = f"{repo}/{image}:latest"

        print(f"[ant] podman push {src_tag} {dst_tag}")
        subprocess.run(["podman", "push", src_tag, dst_tag])

    else:
        print(f"Unknown podman command: {action}")