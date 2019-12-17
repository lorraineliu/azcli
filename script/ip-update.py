# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import logging
import time

import click
from utils import func, logs
from vm import ip

logger = logs.file_logger


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
            if ip_info['ip_allcation_method'] != 'Dynamic':
                raise Exception('ip: %s is not Dynamic' % public_ip)
            url = 'http://%s:%s' % (public_ip, 80)
            if func.check_connection(url) is True:
                time.sleep(1)
        except Exception as e:
            logger.debug('error happens: %s' % e)
            ip.deallocate_vm(group, vm)
            ip.start_vm(group, vm)
            time.sleep(5)


if __name__ == '__main__':
    cli()
