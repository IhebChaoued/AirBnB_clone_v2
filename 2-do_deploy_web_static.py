#!/usr/bin/python3
"""Distribute an archive to web servers using do_deploy."""

import os.path
from fabric.api import env, put, run

env.hosts = ["100.25.48.126", "174.129.55.6"]


def do_deploy(archive_path):
    """Distributes an archive to web servers and deploys it."""
    if not os.path.isfile(archive_path):
        return False

    file = os.path.basename(archive_path)
    name = file.split(".")[0]

    if put(archive_path, f"/tmp/{file}").failed:
        return False
    if run(f"rm -rf /data/web_static/releases/{name}/").failed:
        return False
    if run(f"mkdir -p /data/web_static/releases/{name}/").failed:
        return False
    if run(f"tar -xzf /tmp/{file} -C /\
            data/web_static/releases/{name}/").failed:
        return False
    if run(f"rm /tmp/{file}").failed:
        return False
    if run(f"mv /data/web_static/releases/{name}/web_static/*\
            /data/web_static/releases/{name}/").failed:
        return False
    if run(f"rm -rf /data/web_static/releases/{name}/web_static").failed:
        return False
    if run(f"rm -rf /data/web_static/current").failed:
        return False
    if run(f"ln -s /data/web_static/releases/{name}/\
            /data/web_static/current").failed:
        return False

    return True
