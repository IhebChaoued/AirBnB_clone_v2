#!/usr/bin/python3
"""Fabric script that deletes out-of-date archives"""
from fabric.api import local, env, run
from fabric.context_managers import cd
from datetime import datetime

env.hosts = ['100.25.48.126', '174.129.55.6']


def do_clean(number=0):
    """Deletes out-of-date archives"""
    number = int(number)
    if number < 2:
        number = 1
    else:
        number += 1

    local_archives = sorted(local("ls -1t versions", capture=True).split('\n'))
    server_archives = run("ls -1t /data/web_static/releases").split('\n')

    for archive in local_archives[number:]:
        local("rm -f versions/{}".format(archive))

    with cd("/data/web_static/releases"):
        for archive in server_archives[number:]:
            run("rm -rf {}".format(archive))
