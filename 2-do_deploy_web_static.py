#!/usr/bin/python3
"""This module contains a Fabric script based on 1-pack_web_static.py
that distributes an archive to the given web server."""

import os
from fabric.api import run, env, put

env.hosts = ["54.146.76.26", "54.209.140.150"]


def do_deploy(archive_path):
    """This function distributes an archive file to the given servers."""
    # Check if the given path is available
    if not os.path.exists(archive_path):
        return False

    # Getting the file
    archive_n = os.path.basename(archive_path)  # archive_name
    archive_fn = os.path.splitext(archive_n)[0]  # archive_filename

    # Defining the remote path
    remote_tmp_path = f"/tmp/{archive_n}"
    remote_release_path = f"/data/web_static/releases/{archive_fn}/"

    # Uploading to the /tmp/ Directory of the given servers
    put(archive_path, remote_tmp_path)

    # Making changes to the distributed folder on the remote server
    run(f"mkdir -p {remote_release_path}")
    run(f"tar -xzf {remote_tmp_path} -C {remote_release_path}")
    run(f"rm {remote_tmp_path}")
    run(f"mv {remote_release_path}web_static/* {remote_release_path}")
    run(f"rm -rf {remote_release_path}web_static")

    # Deleting the old symbolic link
    run("rm -rf /data/web_static/current")

    # Creating a new symbolic link
    run(f"ln -s {remote_release_path} /data/web_static/current")
    return True
