#!/usr/bin/python3
""" this module contains a function thats generates
    .tgz of the given folder """
from fabric.api import local
from datetime import datetime


def do_pack():
    """ the function thats generates .tgz from the given folder"""

    local("mkdir versions")

    gnrtd_time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_n = f"web_static_{gnrtd_time}.tgz"
    archive_p = f"versions/{archive_n}"

    create = local(f"tar -czvf {archive_p} web_static")

    if create.succeeded:
        return archive_p
    else:
        return None
