# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import logging
import subprocess

from utils import func, logs


logger = logs.file_logger


def init_app():
    cmd = "az vm run-command invoke -g %s -n %s --command-id RUnShellScript --scripts \"pip3 install flask && python3 /home/test01/app.py &\""
    try:
        out = func.run_cmd(cmd)
        logger.debug('init_app stdout: %s' % out)
    except subprocess.CalledProcessError as e:
        logger.error('fail to run init_app cmd: %s' % e)
        raise e
    except Exception as e:
        logger.error('fail to run init_app cmd: %s' % e)
        raise e


def start_app():
    cmd = "az vm run-command invoke -g %s -n %s --command-id RUnShellScript --scripts \"python3 /home/test01/app.py &\""
    try:
        out = func.run_cmd(cmd)
        logger.debug('start_app stdout: %s' % out)
    except subprocess.CalledProcessError as e:
        logger.error('fail to run start_app cmd: %s' % e)
        raise e
    except Exception as e:
        logger.error('fail to run start_app cmd: %s' % e)
        raise e


def stop_app():
    pass
