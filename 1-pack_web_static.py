#!/usr/bin/python3
""" this module contains a function thats generates
    .tgz of the given folder """
from fabric.api import local
from datetime import datetime


def do_pack():
    """ the function thats generates .tgz from the given folder"""

    local("mkdir versions")

    gnrtd_time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_n = "web_static_{}.tgz".format(gnrtd_time)
    archive_p = "versions/{}".format(archive_n)

    create = local("tar -czvf {} web_static".format(archive_p))

    if create is not None:
        return archive_p
    else:
        return None
