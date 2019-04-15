#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 0:42
# @Author  : 海心
# @Site    : 
# @File    : myscheduler.py
# @Software: PyCharm
# @descri  : 调度器
from ..dataoutput.mydataoutput import DataOutput
from ..HTMLParser.myhtmlparser import HTMLParser
from ..url_manager.myurlmanager import URLManager
from ..downloader.mydownloader import HTMLDownloader


class SpiderMan(object):

    def __init__(self):
        self.manager = URLManager()
        self.downloader = HTMLDownloader()
        self.parser = HTMLParser()
        self.output = DataOutput()

    def crawl(self, root_url):
        """想想广度和深度优先的算法哦"""
        while self.manager.get_new_url() and self.manager.old_url_size():
            try:
                # 从管理器获取新得url
                new_url = self.manager.get_new_url()
                print(new_url)
                #Html 下载器下载网页
                html = self.downloader.download(new_url)
                # 解析器抽取网页数据
                new_urls, data = self.parser.parser(new_url, html)
                print(new_urls)
                # 将抽取到的 url 添加到url管理器中
                self.manager.add_new_urls(new_urls)
                # 存储数据
                self.output.store_data(data)
                print("抓取 %s 个链接"%self.manager.old_url_size())
            except Exception as e:
                print("Failed")
                print(e)
            # 数据存储器将文件输出成指定的格式
            self.output.output_html()

if __name__ == '__main__':
    spider_man = SpiderMan()
    spider_man.crawl("http://www.runoob.com/w3cnote/page/1")

