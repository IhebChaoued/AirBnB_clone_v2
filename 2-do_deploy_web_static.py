#!/usr/bin/python3
"""Distribute an archive to web servers using do_deploy."""

from fabric.api import env, put, run, local
from os.path import exists
from datetime import datetime

env.hosts = ['100.25.48.126', '174.129.55.6']


def do_deploy(archive_path):
    """Distributes an archive to web servers and deploys it."""
    if not exists(archive_path):
        return False

    try:
        archive_filename = archive_path.split("/")[-1]
        no_extension = archive_filename.split(".")[0]

        put(archive_path, "/tmp/")

        run("mkdir -p /data/web_static/releases/{}/".format(no_extension))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(archive_filename, no_extension))
        run("rm /tmp/{}".format(archive_filename))
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(no_extension, no_extension))
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(no_extension))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(no_extension))

        print("New version deployed!")

        return True
    except Exception as e:
        return False
