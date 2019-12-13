# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import json
import logging
import subprocess

logger = logging.getLogger('azcli.utils.func')


def run_cmd(cmd):
    create_app = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if create_app.returncode != 0:
        raise subprocess.CalledProcessError()
    stderr = create_app.stderr.decode("utf-8")
    if stderr == '':
        return json.loads(create_app.stdout.decode("utf-8"))
    raise Exception('run cmd with error: %s' % stderr)


def check_connection(app_url):
    cmd = 'curl %s' % app_url
    try:
        out = run_cmd(cmd)
        out = json.loads(out)
        logger.debug('stdout: %s' % out)
        if 'Connection Check' in out:
            return True
        return False
    except subprocess.CalledProcessError as e:
        logger.debug('fail to run cmd: %s' % e)
        raise e
    except Exception as e:
        raise e


def setup_app():
    pass
