#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Kelly Hwong
# Date: 2019.5.2
from __future__ import unicode_literals, print_function
import signal
import platform

from manhuagui.cmdline import banner, cmd_parser
from manhuagui.logger import logger
from manhuagui.constant import HEADERS, BASE_URL, SERVERS
from manhuagui.comic import Comic
from manhuagui.downloader import Downloader
from manhuagui.utils import generate_html
from manhuagui.parser import comic_parser, comic_index_parser


def main():
    banner()

    logger.info('Manhuagui: {0}'.format(BASE_URL))
    logger.info('Using mirror: {0}'.format(SERVERS[0]))
    options = cmd_parser()

    comic_ids = []
    comic_list = []

    if not comic_ids:
        comic_ids = options.id

    if comic_ids:
        for id_ in comic_ids:
            comic_index = comic_index_parser(id_)
            # if not options.vol
            # test
            # for number in range(len(comic_index.keys())):
            # 试探性爬 4 本
            for number in range(1):
                if number+1 not in comic_index.keys():
                    break
                id_vol_ = comic_index[number+1]
                comic_info = comic_parser(
                    id_=id_vol_["id"], vol_=id_vol_["vol"])
                comic = Comic(**comic_info)
                comic_list.append(comic)

    # print(comic_list)
    # print(comic_list[0].url)
    # return

    # downloader = Downloader(path=options.output_dir,
            # thread=options.threads, timeout=options.timeout)
    downloader = Downloader(thread=4)
    for comic in comic_list:
        logger.info('Starting to download doujinshi: %s %s' %
                    (comic.bname, comic.cname))

        download_queue = []
        headers = HEADERS
        headers['referer'] = comic.url

        for file in comic.files:
            url = 'https://{}{}{}?cid={}&md5={}'.format(
                SERVERS[0], comic.path, file, comic.cid, comic.sl['md5'])
            # _url_headers = (url, headers)
            download_queue.append(url)
            downloader.download(download_queue, session=comic.session,
                                headers=headers, folder=comic.foldername)


def signal_handler(signal, frame):
    logger.error('Ctrl-C signal received. Stopping...')
    exit(1)


signal.signal(signal.SIGINT, signal_handler)

if __name__ == '__main__':
    main()
