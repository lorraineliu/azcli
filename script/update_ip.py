# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import logging
import time
from utils import func
from vm import ip
import click


logger = logging.getLogger('azcli.script.update_ip')


@click.group()
def cli():
    pass


@cli.command()
@click.argument('group')
@click.argument('vm')
def ip_assign(group, vm):
    while True:
        try:
            ip_info = ip.get_ip_info(group, vm)
            public_ip = ip_info.get('ip_address', '')
            if ip_info['ip_allcation_method'] is not 'Dynamic':
                raise Exception('ip: %s is not Dynamic' % public_ip)
            url = 'htpp://%s:%s' % (public_ip, 80)
            time.sleep(5)
            if func.check_connection(url) is not True:
                ip.deallocate_vm(group, vm)
                ip.start_vm(group, vm)
            else:
                time.sleep(1)
        except Exception as e:
            logger.debug('error happens: %s' % e)
            break


if __name__ == '__main__':
    cli()
