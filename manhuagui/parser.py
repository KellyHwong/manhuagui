# coding: utf-8
from __future__ import unicode_literals, print_function

import os
import re
import json
import threadpool
import threading
import requests
import time
import errno
import requests
import execjs
from tabulate import tabulate

from manhuagui.constant import BASE_URL, DETAIL_URL, HEADERS, SERVERS, PROXY
from manhuagui.comic import Comic
from manhuagui.downloader import Downloader
from manhuagui.logger import logger
from manhuagui.utils import find_between, LZjs, format_filename

SERVER = SERVERS[0]


def comic_parser(id_, vol_=294889):
    # vols = get_vols(id_)
    url = '%s/%d/%d.html' % (DETAIL_URL, id_, vol_)
    # 一个本子一个session
    s = requests.Session()
    r = s.get(url, headers=HEADERS)  # 这一步不需要Referer

    js = find_between(r.text, r'["\x65\x76\x61\x6c"]', '</script>')

    comic = execjs.compile(LZjs).eval(js)
    comic = find_between(comic, 'SMH.imgData(', ').preInit();')
    comic = json.loads(comic)

    comic['session'] = s

    return comic


def main():
    # downloader = Downloader(path=options.output_dir,
                            # thread=options.threads, timeout=options.timeout)
    downloader = Downloader(thread=4)
    id = 23552
    vol = 294889
    # id = 9414
    # vol = 94568
    comic_info = comic_parser(id, vol)

    print(comic_info)

    comic = Comic(**comic_info)

    logger.info('Starting to download doujinshi: %s %s' %
                (comic.bname, comic.cname))

    download_queue = []
    headers = HEADERS
    headers['referer'] = comic.url

    print(headers)
    input()

    for file in comic.files:
        url = 'https://{}{}{}?cid={}&md5={}'.format(
            SERVERS[0], comic.path, file, comic.cid, comic.sl['md5'])
        # _url_headers = (url, headers)
        download_queue.append(url)

    foldername = comic.foldername
    downloader.download(download_queue, session=comic.session,
                        headers=headers, folder=foldername)


if __name__ == "__main__":
    main()
