# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import json
import logging
import subprocess

from utils import logs

logger = logs.file_logger


def run_cmd(cmd):
    create_app = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stderr = create_app.stderr.decode("utf-8")
    if create_app.returncode != 0:
        raise Exception('run cmd with error: %s' % stderr)
    return create_app.stdout.decode("utf-8")


def check_connection(app_url):
    cmd = 'curl %s' % app_url
    try:
        out = run_cmd(cmd)
        logger.debug('stdout: %s' % out)
        if 'Connection Check!' in out:
            return True
        return False
    except subprocess.CalledProcessError as e:
        logger.debug('fail to run cmd: %s' % e)
        raise e
    except Exception as e:
        raise e


def init_app():
    """
    steps
        1.cp app.y into vm
        2.sudo apt install python-pip
        3.pip install flask
        4.sudo python app.py &
    :return:None
    """
    pass
