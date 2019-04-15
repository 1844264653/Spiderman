#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 0:17
# @Author  : 海心
# @Site    : 
# @File    : myhtmlparser.py
# @Software: PyCharm
# @descri  : HTML  解析器
import re
from bs4 import BeautifulSoup


class HTMLParser(object):

    def parser(self, page_url, html_cont):
        """
        用于解析网页的内容，抽取url 和 数据
        :param page_url:  下载页面的url
        :param html_cont: 下载的网页内容
        :return: 返回url  和  数据
        """
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, "html.parser")
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        """
        抽取新的url 集合
        :param page_url: 下载页面的 url
        :param soup:  soup 数据（万物都是节点哈哈哈）
        :return: 返回一个新的url
        """
        new_urls = set()
        for link in range(1, 100):
            "添加新的url"
            new_url = "http://runoob.com/w3cnote/page/"+str(link)
            new_urls.add(new_url)
            print(new_urls)
        return new_urls

    def _get_new_data(self, page_url, soup):
        """
        抽取有效数据
        :param page_url: 下载页面的 url
        :param soup:
        :return: 返回有效的数据
        """
        data = {}
        data['url'] = page_url
        title = soup.find("div", class_="post-intro").find("h2")
        print(title)
        data['title'] = title.get_text()
        summary = soup.find("div", class_="post-intro").find("p")
        data["summary"] = summary.get_text()
        return data