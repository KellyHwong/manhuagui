==========
manhuagui
==========
manhuagui 漫画下载

|travis|
|pypi|
|license|

============
Installation
============
Install from PyPI
.. code-block:: bash

    pip3 install manhuagui

Install with this repo with Git
.. code-block:: bash

    git clone https://github.com/KellyHwong/manhuagui

    cd manhuagui

    python3 setup.py install

=====
Usage
=====
下载 别当欧尼酱了 第一话 https://www.manhuagui.com/comic/23552

Download 别当欧尼酱了 1st vol

.. code-block:: python

    manhuagui --id=23552 --vol=1 # 下载第一话

.. code-block:: python

    manhuagui --id=23552 --vol=i # 下载第 i 话

.. code-block:: python

    manhuagui --id=23552 --vol=1,2,3,4 # 下载（1,2,3,4）前 4 话


注意：不要作死下载过多话，虽然提供下载所有话的命令，但这样容易被封 ip

.. code-block:: python

    # Not recommendded!

    manhuagui --id=23552 --vol=all # 下载所有话

为了保护你宝贵的IP，不输入--vol默认等同于[--vol=1]，即只下载第一话

For the concern of your IP, no --vol input is equivalent with [--vol-1], i.e., only download the 1st vol.
.. code-block:: python

    manhuagui --id=23552 [--vol=1] # 默认只下载第一话

====
webp
====

webp 是 Google 的图像存储格式，Google Chrome 等浏览器可以识别和浏览。

TODO feature: 漫画图片文件夹下自动生成了 index.html 模板，可以直接打开，里面实现了简单的图片浏览器。

===============
Acknowledgement
===============

Thanks to [RicterZ@Github](https://github.com/RicterZ)'s code in [nhentai](https://github.com/RicterZ/nhentai), his code is very pretty and inspiring, and, very useful.

And thanks to this repository [manhuagui-dl](https://github.com/ysc3839/manhuagui-dl)

.. |travis| image:: https://travis-ci.org/KellyHwong/manhuagui.svg?branch=master
    :target: https://travis-ci.org/KellyHwong/manhuagui

.. |pypi| image:: https://img.shields.io/pypi/dm/manhuagui.svg
    :target: https://pypi.org/project/manhuagui/

.. |license| image:: https://img.shields.io/github/license/kellyhwong/manhuagui.svg
    :target: https://github.com/KellyHwong/manhuagui/blob/master/LICENSE
