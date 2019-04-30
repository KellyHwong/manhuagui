# coding: utf-8
from __future__ import print_function, unicode_literals
import os
import json
import errno
import threading

import requests
import execjs

# from manhuagui.settings import HEADERS, SERVERS
# from manhuagui.utils import find_between, LZjs, format_filename

# debug
from settings import HEADERS, SERVERS
from utils import find_between, LZjs, format_filename
from downloader import dlfile


class ComicInfo(dict):
    def __init__(self, **kwargs):
        super(ComicInfo, self).__init__(**kwargs)

    def __getattr__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            return ''


class Comic(object):
    def __init__(self, name=None, id=None, url=None, img_id=None, ext='', pages=0, **kwargs):
        self.name = name
        self.id = id
        self.img_id = img_id
        self.ext = ext
        self.pages = pages
        self.downloader = None
        self.url = url
        # self.url = '%s/%d' % (DETAIL_URL, self.id)
        self.info = ComicInfo(**kwargs)
        self.filename = format_filename(
            '[%s][%s][%s]' % (self.id, self.info.artist, self.name))


def get_pic(url):
    s = requests.Session()

    r = s.get(url, headers=HEADERS)  # 这一步不需要Referer

    js = find_between(r.text, r'["\x65\x76\x61\x6c"]', '</script>')
    # print(js)
    # return
    info = execjs.compile(LZjs).eval(js)
    # print(info)
    # return
    # info = find_between(info, 'cInfo=', '||{};')
    info = find_between(info, 'SMH.imgData(', ').preInit();')
    info = json.loads(info)

    print(info)

    comic_name = info['bname']
    vol_name = info['cname']
    path = info['path']
    pages = info['len']

    # dir_name = '%s-%sp' % (vol_name, pages)
    dir_name = '[%s][%s]' % (comic_name, vol_name)
    print(dir_name)
    loc = os.path.dirname(__file__)
    dir_abs_path = os.path.join(loc, dir_name)
    print(dir_abs_path)
    try:
        os.mkdir(dir_abs_path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("错误")
            raise

    args_list = []
    i = 0
    for filename in info['files']:
        i += 1
        # 生成图片 url
        pic_url = 'https://{}{}{}?cid={}&md5={}'.format(
            SERVERS[0], path, filename, info["cid"], info["sl"]["md5"])
        print(pic_url)

        _headers = HEADERS
        _headers['referer'] = url

        args_list.append((s, pic_url, _headers, dir_abs_path, filename))
        # ext = os.path.splitext(filename)[1]
        # args_list.append((s, pic_url, _headers, dir_name, '%s%s' % (i, ext)))

    threads = [threading.Thread(target=dlfile, args=a) for a in args_list]
    [t.start() for t in threads]
    [t.join() for t in threads]


if __name__ == '__main__':
    URL = "https://www.manhuagui.com/comic/23552/294889.html"
    '''
    test = Doujinshi(name='test onichan comic', id="23552"
                     url=URL)
    print(test)
    test.show()
    try:
        test.download()
    except Exception as e:
        print('Exception: %s' % str(e))
    '''
    get_pic(URL)
