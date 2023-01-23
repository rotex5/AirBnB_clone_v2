#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers
"""
from fabric.api import env, local, put, run
from os import path
import time

env.hosts = ["54.172.37.10", "54.82.176.244"]
env.user = "ubuntu"


def do_pack():
    """
    generates a .tgz archive from
    the contents of the web_static folder
    """
    try:
        local("mkdir -p versions")

        t = time.strftime("%Y%m%d%H%M%S")
        gen_path = "versions/web_static_{}.tgz".format(t)

        local("tar -cvzf {} web_static".format(gen_path))

        get_size = local('wc -c {}'.format(gen_path), capture=True)
        get_size = get_size.split(" ")[0]

        print("web_static packed: {} -> {}Bytes".format(gen_path, get_size))
        return gen_path
    except Exception:
        return None


def do_deploy(archive_path):
    """ Deploy arcives to web servers
    """
    if not path.exists(archive_path):
        return False

    filename = path.splitext(archive_path)[0].split("/")[-1]
    filename_ext = archive_path.split("/")[-1]

    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p /data/web_static/releases/{}".format(filename))
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}"
            .format(filename_ext, filename))
        run("sudo rm -f /tmp/{}".format(filename_ext))
        run("sudo rm -f /data/web_static/current")
        run("sudo ln -sf /data/web_static/releases/{}  \
                /data/web_static/current".format(filename))
        print("New version deployed!")
        return True
    except Exception:
        return False
