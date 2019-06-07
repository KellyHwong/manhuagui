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
from manhuagui.comic import Comic, VolType
from manhuagui.downloader import Downloader
from manhuagui.logger import logger
from manhuagui.utils import find_between, LZjs, format_filename

SERVER = SERVERS[0]


def comic_index_parser(id_, type_=VolType.SINGLE_EPISODE):
    '''根据漫画id，爬取漫画主页，返回漫画单话的链接

    :param id_: The id of the entire comic
    :param type_: The type of the single comic volumn
    :returns: list of urls
    :rtype: list
    '''
    s = requests.Session()
    url = '%s/%d' % (DETAIL_URL, id_)
    # print(url)
    r = s.get(url, headers=HEADERS)
    # with open("test.html", "w", encoding="utf-8") as f:
        # f.write(r.text)

    # XPath
    import html
    # text = html.unescape(r.text)
    text = r.text
    from lxml import etree
    root = etree.HTML(text)

    # TODO 根据VolType选择列表
    items = root.xpath("//div[@class='chapter-list cf mt10'][1]//a")  # 单话 a
    extra_items = root.xpath(
        "//div[@class='chapter-list cf mt10'][2]//a")  # 番外篇

    urls = [item.xpath("@href") for item in items]
    urls = [url[0] for url in urls]
    titles = [item.xpath("@title") for item in items]
    titles = [title[0] for title in titles]

    vols = []
    import re
    for url in urls:
        # print(url)
        m = re.findall(r'\d+', url)
        # print(m[1])
        # input()
        vols.append(m[1])

    comic_index = dict()
    titles = list(reversed(titles))
    vols = list(reversed(vols))
    for number in range(len(titles)):
        comic_index[number +
                    1] = dict({"title": titles[number], "id": id_, "vol": int(vols[number])})

    # print(comic_index)

    return comic_index


def comic_parser(id_, vol_):
    '''如果我们知道comic和vol的ID，就可以合成url

    :param id_: The id of the comic

    :returns: list of urls
    :rtype: list
    '''
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
    # downloader = Downloader(thread=4)

    # 别当欧尼酱了
    id = 23552
    vol = 294889
    # test comic parser
    '''
    # id = 9414
    # vol = 94568
    comic_info = comic_parser(id, vol)
    print(comic_info)
    comic = Comic(**comic_info)
    '''

    # test comic index parser
    comic_index_parser(id_=id)


if __name__ == "__main__":
    main()
