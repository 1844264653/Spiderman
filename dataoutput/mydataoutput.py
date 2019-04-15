#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 0:33
# @Author  : 海心
# @Site    : 
# @File    : mydataoutput.py
# @Software: PyCharm
# @descri  : 数据存储器
import codecs

class DataOutput(object):

    def __init__(self):
        self.datas = []

    def store_data(self, data):
        # if data is None:
        if not data:
            return
        self.datas.append(data)

    def output_html(self):
        """可以保存在自己数据库中"""
        fout = codecs.open("baike.html", 'a', encoding="utf-8")
        fout.write("<html>")
        fout.write("<head><meta charset='utf-8'/></head>")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>《%s》</td>" % data['title'])
            fout.write("<td>[%s]</td>" % data['summary'])
            fout.write("</tr>")
            self.datas.remove(data)
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()


