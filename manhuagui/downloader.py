#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Kelly Hwong
# Date: Apr 1st, 2019

from __future__ import unicode_literals, print_function
from future.builtins import str as text
import os
import requests
import threadpool
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

from manhuagui.constant import PROXY
from manhuagui.logger import logger
# from manhuagui.parser import request
from manhuagui.utils import Singleton


requests.packages.urllib3.disable_warnings()


def request(method, url, headers=None, **kwargs):
    if not hasattr(requests, method):
        raise AttributeError(
            '\'requests\' object has no attribute \'{0}\''.format(method))

    return requests.__dict__[method](url, headers, proxies=PROXY, verify=False, **kwargs)


class ManhuaguiImageNotExistException(Exception):
    pass


class Downloader(Singleton):

    def __init__(self, path='', thread=1, timeout=30):
        if not isinstance(thread, (int, )) or thread < 1 or thread > 15:
            raise ValueError('Invalid threads count')
        self.path = str(path)
        self.thread_count = thread
        self.threads = []
        self.thread_pool = None
        self.timeout = timeout

    def _download(self, url, session=None, headers='', folder='', filename='', retried=0):
        logger.info('Starting to download {0} ...'.format(url))
        filename = filename if filename else os.path.basename(
            urlparse(url).path)
        base_filename, extension = os.path.splitext(filename)
        try:
            if os.path.exists(os.path.join(folder, base_filename.zfill(3) + extension)):
                logger.warning('File: {0} exists, ignoring'.format(os.path.join(folder, base_filename.zfill(3) +
                                                                                extension)))
                return 1, url

            response = None
            with open(os.path.join(folder, base_filename.zfill(3) + extension), "wb") as f:
                i = 0
                while i < 10:
                    try:
                        if session:
                            response = session.get(url, headers=headers,
                                                   stream=True, timeout=self.timeout, proxies=PROXY, verify=False)
                        else:
                            response = request(
                                'get', url, headers=headers, stream=True, timeout=self.timeout)
                        if response.status_code != 200:
                            raise ManhuaguiImageNotExistException

                    except ManhuaguiImageNotExistException as e:
                        raise e

                    except Exception as e:
                        i += 1
                        if not i < 10:
                            logger.critical(str(e))
                            return 0, None
                        continue

                    break

                length = response.headers.get('content-length')
                if length is None:
                    f.write(response.content)
                else:
                    for chunk in response.iter_content(2048):
                        f.write(chunk)

        except (requests.HTTPError, requests.Timeout) as e:
            if retried < 3:
                logger.warning(
                    'Warning: {0}, retrying({1}) ...'.format(str(e), retried))
                return 0, self._download(url=url, folder=folder, filename=filename, retried=retried+1)
            else:
                return 0, None

        except ManhuaguiImageNotExistException as e:
            os.remove(os.path.join(folder, base_filename.zfill(3) + extension))
            return -1, url

        except Exception as e:
            logger.critical(str(e))
            return 0, None

        return 1, url

    def _download_callback(self, request, result):
        result, data = result
        if result == 0:
            logger.warning('fatal errors occurred, ignored')
            # exit(1)
        elif result == -1:
            logger.warning('url {} return status code 404'.format(data))
        else:
            logger.log(15, '{0} downloaded successfully'.format(data))

    def download(self, queue, session=None, headers='', folder=''):
        if not isinstance(folder, text):
            folder = str(folder)

        if self.path:
            folder = os.path.join(self.path, folder)

        if not os.path.exists(folder):
            logger.warn(
                'Path \'{0}\' does not exist, creating.'.format(folder))
            try:
                os.makedirs(folder)
            except EnvironmentError as e:
                logger.critical('{0}'.format(str(e)))
                exit(1)
        else:
            logger.warn('Path \'{0}\' already exist.'.format(folder))

        queue = [([url], {'session': session, 'headers': headers, 'folder': folder})
                 for url in queue]

        self.thread_pool = threadpool.ThreadPool(self.thread_count)
        requests_ = threadpool.makeRequests(
            self._download, queue, self._download_callback)
        [self.thread_pool.putRequest(req) for req in requests_]

        self.thread_pool.wait()
