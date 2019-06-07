# coding: utf-8
from __future__ import unicode_literals, print_function
import os
from manhuagui.utils import urlparse

# BASE_URL = os.getenv('MANHUAGUI', 'https://www.manhuagui.com')
BASE_URL = os.getenv('MANHUAGUI', 'https://www.manhuagui.com')
DETAIL_URL = '%s/comic' % BASE_URL

HEADERS = {
    'DNT': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
    'Referer': 'https://www.manhuagui.com/comic/23552/294889.html'
}


SERVERS = [
    'i.hamreus.com',
    'us.hamreus.com',
    'dx.hamreus.com',
    'eu.hamreus.com',
    'lt.hamreus.com'
]

PROXY = {}
