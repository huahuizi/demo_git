# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup as bs4
import socket,re,requests
from lxml import etree
socket.setdefaulttimeout(5)
from scrapy.http import Request
from yachang.items import YachangItem
import sys,re
import chardet
import pymongo
reload(sys)
sys.setdefaultencoding('utf-8')
class ArtonNetSpider(scrapy.Spider):

    item = YachangItem()
    name = "luntan"
    allowed_domains = ["blog.artron.net"]
    # start_urls = []
    # for cateurl in open('users.txt','r'):
    #     start_urls.append(cateurl.strip('\n'))

    # def get_or_not(self):
    #     try:
    #         item['title']=re.search('<title>(.*?)</title>',response.body,re.S).group(1).decode('gbk').encode('utf8')
    #     except Exception as e:
    #         item['title']= 'no data'
    def start_requests(self):
        for x in xrange(1, 1712893, 1):
            url = "http://www.jiemian.com/article/%d.html" % x
            #http://www.jiemian.com/article/492490.html
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        # soup = bs4(response.body,'lxml')
        item = YachangItem()
        title= re.search('<title>(.*?)</title>',response.body,re.S).group(1)
        #print response.url
        open("titles.txt",'a+').write(title+"\n")