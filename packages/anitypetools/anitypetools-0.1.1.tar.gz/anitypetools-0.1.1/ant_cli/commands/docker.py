import subprocess
from ant_cli.utils import pprint
from ant_cli import storage

def execute(params):
    if not params:
        pprint("Usage: ant dk <build|push> <image>")
        return

    action = params[0]

    if action == "build":
        if len(params) < 2:
            pprint("Usage: ant dk build <image>")
            return

        image = params[1]
        full_tag = f"{image}:latest"

        pprint(f"[ant] docker build -t {full_tag} .")
        subprocess.run(["docker", "build", "-t", full_tag, "."])

    elif action == "push":
        if len(params) < 2:
            pprint("Usage: ant dk push <image>")
            return

        image = params[1]
        repo = storage.get_value("repo")

        if not repo:
            pprint("Error: repo not set. Use 'ant set repo <name>' first.")
            return

        src_tag = f"{image}:latest"
        dst_tag = f"{repo}/{image}:latest"

        pprint(f"[ant] docker tag {src_tag} {dst_tag}")
        subprocess.run(["docker", "tag", src_tag, dst_tag])

        pprint(f"[ant] docker push {dst_tag}")
        subprocess.run(["docker", "push", dst_tag])

    else:
        pprint(f"Unknown docker command: {action}")
