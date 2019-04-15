#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 0:10
# @Author  : 海心
# @Site    : 
# @File    : mydownloader.py
# @Software: PyCharm
# @descri  : html 下载器

import requests

class HTMLDownloader(object):
    def download(self, url):
        if url is None:
            return
        s = requests.Session()  # 使用session，方便保存cookie
        # 可优化称ua池  cookie池  IP池
        s.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        res = s.get(url)
        # 判断是否正常获取
        if res.status_code == 200:
            res.emcoding = 'utf-8'
            res = res.text
            return res
        return