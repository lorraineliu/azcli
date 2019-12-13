# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import json
import logging
import subprocess

from utils import func

logger = logging.getLogger('azcli.vm.ip')


def get_ip_info(group, vm):
    cmd = "az vm list-ip-addresses -g %s -n %s" % (group, vm)
    try:
        out = json.loads(func.run_cmd(cmd))
        ip_address = out[0]['virtualMachine']['network']['publicIpAddresses'][0]['ipAddress']
        ip_allocation_method = out[0]['virtualMachine']['network']['publicIpAddresses'][0]['ipAllocationMethod']
        name = out[0]['virtualMachine']['network']['publicIpAddresses'][0]['name']
        return dict(
            ip_address=ip_address,
            ip_allcation_method=ip_allocation_method,
            name=name
        )
    except subprocess.CalledProcessError as e:
        logger.debug('fail to run cmd: %s' % e)
        raise e
    except Exception as e:
        raise e


def deallocate_vm(group, vm):
    cmd = "az vm deallocate -g %s -n %s" % (group, vm)
    try:
        out = func.run_cmd(cmd)
        logger.debug('stdout: %s' % out)
    except subprocess.CalledProcessError as e:
        logger.debug('fail to run cmd: %s' % e)
        raise e
    except Exception as e:
        raise e


def start_vm(group, vm):
    cmd = "az vm start -g %s -n %s" % (group, vm)
    try:
        out = func.run_cmd(cmd)
        logger.debug('stdout: %s' % out)
    except subprocess.CalledProcessError as e:
        logger.debug('fail to run cmd: %s' % e)
        raise e
    except Exception as e:
        raise e
