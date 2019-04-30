#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Kelly Hwong
# Date: Jan 29, 2019

from download_page import download_page
from bs4 import BeautifulSoup
import os
import requests
import re



class Manhuagui(object):
    """docstring for Manhuagui"""
    def __init__(self, chapterURLs):
        super(Manhuagui, self).__init__()
        if not isinstance(chapterURLs, list):
            chapterURLs = [chapterURLs]
        self.chapterURLs = chapterURLs
        # configs
        self.chapterPath = "benzi"
        self.download_processes_num = 4

    def getGalleryMetas(self, chapterURL):
        metas = dict()
        query_url = chapterURL
        '''
        query_html = download_page(query_url).decode('utf-8')

        '''
        headers = {
            "DNT": "1",
            "Referer": "https://www.cartoonmad.com/comic/582700012013001.html",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
        }
        query_html = requests.get(query_url, headers=headers).content
        query_html = query_html.decode("big5")
        with open("debugCartoon.html", "w") as f:
            f.write(query_html)
        query_soup = BeautifulSoup(query_html, "lxml")
        # div_info_block = query_soup.find("div", {"id": "info-block"})
        # gallery info
        title = query_soup.find("title")
        metas["title"] = title.text
        # print(title.text)
        pageSelect = query_soup.find("select", {"id": "pageSelect"})
        print(pageSelect)
        pageOptions = pageSelect.find_all("option")
        print(pageOptions)
        lastPageOption = pageOptions[-1]
        pageNum = lastPageOption["value"]
        # Upper is gallery thumbnails
        div_thumbnail_container = query_soup.find("div", {"class": "container", "id": "thumbnail-container"})
        # print(len(div_thumbnail_container))
        div_thumbnails = div_thumbnail_container.find_all("div", {"class": "thumb-container"})
        # div_thumbnails[0].find("a", {"class", "gallerythumb"})
        chapterURL
        single_view_links = []

        prefix = "https://www.manhuagui.com/comic/23552/294889.html#p="
        pageURLs = [prefix + str(index) for index in range(1, pageNum + 1)]
        # single_view_links, links of every page
        # print(single_view_links)
        metas["pageURLs"] = pageURLs
        # Retrieve gallery image urls
        # 单线程
        img_urls = []
        for pageURL in pageURLs:
            query_url = pageURL
            img["src"]
            query_html = download_page(query_url).decode('utf-8')
            query_soup = BeautifulSoup(query_html, "lxml")
            mangaFile = query_soup.find("img",{"id", "mangaFile"})
            img_urls.append(mangaFile["src"])
        # restore urls
        print(img_urls)
        metas["img_urls"] = img_urls
        return metas

    def downloadGalleries(self):
        base_path = os.path.abspath(".") # TODO 读取配置文件，设置下载根目录
        base_path = os.path.join(base_path, self.chapterPath)
        all_gallery_img_urls = []
        all_gallery_folder_path = []
        for chapterURL in self.chapterURLs:
            metas = self.getGalleryMetas(chapterURL)
            gallery_folder_name = metas["h2"] # 中文名
            # debug
            print(gallery_folder_name)
            gallery_folder_path = os.path.join(base_path, gallery_folder_name + '/')
            gallery_folder_paths = len(metas["img_urls"]) * [gallery_folder_path]
            all_gallery_img_urls.extend(metas["img_urls"])
            all_gallery_folder_path.extend(gallery_folder_paths)
        pool = Pool(self.download_processes_num)
        results = pool.map(saveIMG, all_gallery_img_urls, all_gallery_folder_path)
    def dowanload():
        pass

def saveIMG(img_url, gallery_folder_path):
    img_get = requests.get(img_url)
    # Method 1, 这样写有时候不对
    # image_name = os.path.split(img_url)[1]
    # Method 2, 靠谱一点
    file_url = urlparse(img_url) # 网站/后面的url
    file_name = os.path.basename(file_url.path)
    file_abs_path = os.path.join(gallery_folder_path, file_name)
    os.makedirs(os.path.dirname(file_abs_path), exist_ok=True)
    with open(file_abs_path, "wb") as f:
        f.write(img_get.content)
        print("saved to: " + file_abs_path)

def main():
    # chapterURL = "https://www.manhuagui.com/comic/23552/294889.html"
    chapterURL = "https://www.manhuagui.com/comic/17023/176171.html"
    pageURL = chapterURL
    headers = {
        "DNT": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh-HK;q=0.7,zh;q=0.6"
    }
    response = requests.get(pageURL, headers=headers)
    # print(response.headers)
    query_html = response.content.decode('utf-8')
    with open("debugCartoon.html", "w") as f:
        f.write(query_html)
    query_soup = BeautifulSoup(query_html, "lxml")
    # print(query_soup)
    manga_box = query_soup.find("div", {"id", "mangaBox"}) # 漫画图片页元素
    print(manga_box)

    # manhuagui = Manhuagui(pageURL)
    # manhuagui.getGalleryMetas(manhuagui.pageURLs[0])

if __name__ == '__main__':
    main()

#title 别当欧尼酱了！第01回_别当欧尼酱了！漫画 - 看漫画

