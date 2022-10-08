#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack
execute: fab -f 1-pack_web_static.py do_pack
"""

from fabric.api import local
import datetime as dt
import os


def do_pack():
    """
    generates a .tgz archive from the contents of the web_static
    Return:
        The absolute path of the archive if created. None otherwise
    """
    local("mkdir -p versions")
    d = dt.datetime.now()
    name = f"versions/web_static_{d.year}{d.month}{d.day}"\
           + f"{d.hour}{d.minute}{d.second}.tgz"
    local("tar cvfz {} web_static".format(name))
    if os.path.exists(name):
        return os.path.abspath(name)
