# coding: utf-8
from __future__ import print_function
import sys
from optparse import OptionParser
from manhuagui import __version__
try:
    from itertools import ifilter as filter
except ImportError:
    pass

import manhuagui.constant as constant
from manhuagui.utils import urlparse, generate_html
from manhuagui.logger import logger

try:
    if sys.version_info < (3, 0, 0):
        import codecs
        import locale
        sys.stdout = codecs.getwriter(
            locale.getpreferredencoding())(sys.stdout)
        sys.stderr = codecs.getwriter(
            locale.getpreferredencoding())(sys.stderr)

except NameError:
    # python3
    pass


def banner():
    logger.info(u'''Manhuagui ver %s: 漫画柜
/***
 *       ____          _        _                   
 *      / __ \        (_)      | |                  
 *     | |  | | _ __   _   ___ | |__    __ _  _ __  
 *     | |  | || '_ \ | | / __|| '_ \  / _` || '_ \ 
 *     | |__| || | | || || (__ | | | || (_| || | | |
 *      \____/ |_| |_||_| \___||_| |_| \__,_||_| |_|
 *      _____          _              _     _       
 *     |  __ \        (_)            | |   (_)      
 *     | |  | |  __ _  _  ___  _   _ | | __ _       
 *     | |  | | / _` || |/ __|| | | || |/ /| |      
 *     | |__| || (_| || |\__ \| |_| ||   < | |      
 *     |_____/  \__,_||_||___/ \__,_||_|\_\|_|      
 *                                                  
 *                                                  
 */
 你要成为欧尼酱嘛？''' % __version__)


def cmd_parser():
    parser = OptionParser()
    parser.add_option('--id', type='string', dest='id',
                      action='store', help='comic ids set, e.g. 23552')
    parser.add_option('--vol', type='string', dest='vol',
                      action='store', help='comic vols set, e.g. 1,2,3, or "all" if you want :-)')
    parser.add_option('--threads', '-t', type='int', dest='threads', action='store', default=4,
                      help='thread count for downloading comic')
    parser.add_option('--timeout', '-T', type='int', dest='timeout', action='store', default=30,
                      help='timeout for downloading comic')
    try:
        sys.argv = list(map(lambda x: unicode(
            x.decode(sys.stdin.encoding)), sys.argv))
    except (NameError, TypeError):
        pass
    except UnicodeDecodeError:
        exit(0)

    args, _ = parser.parse_args(sys.argv[1:])

    if args.id:
        _ = map(lambda id: id.strip(), args.id.split(','))
        args.id = set(map(int, filter(lambda id_: id_.isdigit(), _)))

    if args.vol:
        _ = map(lambda vol: vol.strip(), args.vol.split(','))
        args.vol = set(map(int, filter(lambda vol_: vol_.isdigit(), _)))

    return args
