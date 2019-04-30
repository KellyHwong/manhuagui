#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Kelly Hwong
# Date: Apr 1st, 2019

import os
import requests


def dlfile(s, url, _headers, dirname, filename):
    r = s.get(url, headers=_headers)

    with open(dirname + '/' + filename, 'wb') as f:
        for chunk in r.iter_content(8192):
            f.write(chunk)

    print('%s: OK!' % filename)
