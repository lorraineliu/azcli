# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import json
import logging
import subprocess

logger = logging.getLogger('azure.utils')

def run_cmd(cmd):
    create_app = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if create_app.returncode != 0:
        raise subprocess.CalledProcessError()
    stderr = create_app.stderr.decode("utf-8")
    if stderr == '':
        return json.loads(create_app.stdout.decode("utf-8"))
    raise Exception('run cmd with error: %s' % stderr)


def ping_app():
    pass


def setup_app():
    pass
