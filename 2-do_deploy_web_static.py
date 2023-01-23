#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers
"""
from fabric.api import *
from os import path

env.hosts = ["54.172.37.10", "54.82.176.244"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """ Deploy arcives to web servers
    """
    if not path.exists(archive_path):
        return False

    if path.exists(archive_path):
        filename = archive_path.split("/")[-1].split(".")[0]
        filename_ext = archive_path.split("/")[-1]

        put(archive_path, "/tmp/{}".format(filename_ext))
        run("mkdir -p /data/web_static/releases/{}".format(filename))

        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(filename_ext, filename))

        run("rm -f /tmp/{}".format(filename_ext))

        run("mv /data/web_static/releases/{}/web_static/* \
                /data/web_static/releases/{}/".format(filename, filename))

        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(filename))

        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/  \
                /data/web_static/current".format(filename))
        print("New version deployed!")
        return True
    else:
        return False
