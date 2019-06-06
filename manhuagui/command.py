#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Kelly Hwong
# Date: 2019.5.2
from __future__ import unicode_literals, print_function
import signal
import platform

from manhuagui.cmdline import banner, cmd_parser
from manhuagui.logger import logger
from manhuagui.constant import BASE_URL, SERVERS
from manhuagui.utils import generate_html
from manhuagui.parser import comic_parser


def main():
    banner()
    # '''
    logger.info('Manhuagui: {0}'.format(BASE_URL))
    logger.info('Using mirror: {0}'.format(SERVERS[0]))
    options = cmd_parser()

    comic_ids = []
    comic_list = []

    if not comic_ids:
        comic_ids = options.id

    if comic_ids:
        for id_ in comic_ids:
            comic_info = comic_parser(id_)
            comic_list.append(comic_info)
    # '''


def signal_handler(signal, frame):
    logger.error('Ctrl-C signal received. Stopping...')
    exit(1)


signal.signal(signal.SIGINT, signal_handler)

if __name__ == '__main__':
    main()
