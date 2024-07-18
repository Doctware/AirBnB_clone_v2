#!/usr/bin/python3
""" this module contains function do_pack, do_deploy
that inisiate full deployment """
import os
from fabric.api import run, local, put, env
from datetime import datetime
env.host = ["", ""]


def do_pack():
    """ this fuction pack/compress a file then prepare for deployment
    """
    local("mkdir versions")

    gnrt_t = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_n = f"web_static_{gnrt_t}.tgz"
    archive_p = f"versions/{archive_n}"

    create = local(f"tar -czvf {archive_p} web_static")

    if create is not None:
        return archive_p
    else:
        return None


def do_deploy(archive_path):
    """ this function deployed the packed file as biven """
    if not os.path.exists(archive_path):
        return False

    archive_n = os.path.basename(archive_p)
    archive_fn = os.path.splitext(archive_fn)

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


def deploy():
    """ creator and deplyer """
    archive = do_pack()
    if not archive:
        return False
    return do_deploy(archive_path)
