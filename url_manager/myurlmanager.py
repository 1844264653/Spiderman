#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/15 23:55
# @Author  : 海心
# @Site    : 
# @File    : myurlmanager.py
# @Software: PyCharm
# @descri  : 写一个爬虫的url  管理器  后续加入算法优化

class URLManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def has_new_url(self):
        # 判断是否有未爬取的  url
        return self.new_url_size()!=0

    def get_new_url(self):
        # 获取一个未爬取的链接
        new_url = self.new_urls.pop()
        # 提取之后，将其添加到已爬取的链接中
        self.old_urls.add(new_url)

    def add_new_url(self, url):
        # 将新链接添加到未爬取的集合里-单个链接
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        # 将新链接添加到未爬取的集中中-集合
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def new_url_size(self):
        # 获取未爬取的 url 集合的大小
        return len(self.new_urls)

    def old_url_size(self):
        # 获取已爬取url集合的大小
        return len(self.old_urls)