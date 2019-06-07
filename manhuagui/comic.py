# coding: utf-8
from __future__ import print_function, unicode_literals
import os
import json
import errno
import threading

import requests
import execjs

from manhuagui.constant import HEADERS, SERVERS, DETAIL_URL
from manhuagui.utils import find_between, LZjs, format_filename


from enum import Enum, IntEnum, unique

# 单卷/单话的类型
@unique
class VolType(IntEnum):
    SINGLE_EPISODE = 1
    EXTRA_EPISODE = 2
    SINGLE_BOOK = 3
    ORIGINAL_VERSION = 4


class ComicIndex(object):
    '''
    ComicIndex class for a entire comic

    Args:
        bid (int): The bid is used for...
        bname (str): The bname is used for...
        *args: The variable arguments are used for...
        **kwargs: The keyword arguments are used for...

    Attributes:
        arg (str): This is where we store arg,
    '''

    def __init__(self, bid=None, bname=None, bpic=None, **kwargs):
        self.bid = bid
        self.bname = bname
        self.bpic = bpic


class ComicInfo(dict):
    def __init__(self, **kwargs):
        super(ComicInfo, self).__init__(**kwargs)

    def __getattr__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            return ''


class Comic(object):
    def __init__(self, bid=None, bname=None, bpic=None, cid=None, cname='', files=None, len=0, path='', nextId=0, sl=None, session=None, **kwargs):
        self.bid = bid
        self.bname = bname
        self.bpic = bpic
        self.cid = cid
        self.cname = cname
        self.files = files
        self.len = len
        self.path = path
        self.nextId = nextId
        self.sl = sl
        self.session = session
        self.downloader = None
        self.url = '%s/%d/%d.html' % (DETAIL_URL, self.bid, self.cid)
        self.info = ComicInfo(**kwargs)
        # self.info.artist 作者名要在漫画首页拿
        # self.foldername = format_filename('[%s][%s]' % (self.bname, self.cname))
        self.foldername = '[%s][%s]' % (self.bname, self.cname)


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
