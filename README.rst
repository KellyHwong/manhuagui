========================
Installation 安装 (pip3)
========================
.. code-block:: bash

    pip3 install ip138

=============================
Installation 安装 (git clone)
=============================
.. code-block:: bash

    git clone https://github.com/KellyHwong/ip138
    cd ip138
    python3 setup.py install

==========
Usage 用法
==========
.. code-block:: bash

    ip138 --ip={Your Query IP Address}

============
Example 例子
============
.. code-block:: bash

    ip138 --ip=172.217.161.164

======================
import usage import 使用
======================
.. code-block:: python

    from ip138.ip138 import ip138
    ip138("111.111.111.111")

==========
manhuagui
==========
manhuagui 漫画下载

|travis|
|pypi|
|license|

# Usage

TODO：目前只实现了下载第 i 话

下载 别当欧尼酱了 第一话 https://www.manhuagui.com/comic/23552

manhuagui --id=23552 [--vol=1] # 默认只下载第一话

manhuagui --id=23552 --vol=1 # 下载第一话

manhuagui --id=23552 --vol=i # 下载第 i 话

manhuagui --id=23552 --vols=4 # 下载前 4 话

注意：不要作死下载过多话，虽然提供下载所有话的命令，但这样容易被封 ip
manhuagui --id=23552 --vols=all # 下载所有话

# webp

webp 是 Google 的图像存储格式，Google Chrome 等浏览器可以识别和浏览。

TODO feature: 漫画图片文件夹下自动生成了 index.html 模板，可以直接打开，里面实现了简单的图片浏览器。

# Acknowledgement

Thanks to [RicterZ@Github](https://github.com/RicterZ)'s code in [nhentai](https://github.com/RicterZ/nhentai), his code is very pretty and inspiring, and, very useful.

And thanks to this repository [manhuagui-dl](https://github.com/ysc3839/manhuagui-dl)

.. |travis| image:: https://travis-ci.org/RicterZ/nhentai.svg?branch=master
:target: https://travis-ci.org/RicterZ/nhentai

.. |pypi| image:: https://img.shields.io/pypi/dm/manhuagui.svg
:target: https://pypi.org/project/manhuagui/

.. |license| image:: https://img.shields.io/github/license/kellyhwong/ip138.svg
:target: https://github.com/KellyHwong/ip138/blob/master/LICENSE
