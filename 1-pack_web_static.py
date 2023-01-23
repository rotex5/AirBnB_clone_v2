#!/usr/bin/python3
#  script that generates a .tgz archive from the contents of the web_static

from fabric.api import local
import time


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
