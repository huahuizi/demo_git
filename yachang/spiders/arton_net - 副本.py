# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup as bs4
import socket,re
socket.setdefaulttimeout(5)
from scrapy.http import Request
from yachang.items import YachangItem
import sys
import pymongo
reload(sys)
sys.setdefaultencoding('utf-8')
class ArtonNetSpider(scrapy.Spider):
    name = "bobao"
    allowed_domains = ["shop.artxun.com"]
    start_urls = ['http://shop.artxun.com/']

    def parse(self, response):
        soup = bs4(response.body,'lxml')
        item = YachangItem()
        item['title']=re.search('<title>(.*?)</title>',response.body,re.S).group(1)
        item['url']=response.url 
        item['st']=response.status
        # print response.headers
        # item['keywords']=re.search('<meta name="keywords" content="(.*?)"/>',response.body,re.S).group(1)
        # item['desc']=re.search('<meta name="description" content="(.*?)"/>',response.body,re.S).group(1)
        yield item
        for i in soup.find_all('a'):
            link = str(i.get('href'))
            if link.startswith('http://shop.artxun.com'):
                # print i.get('href')
                url = i.get('href')
                if 'net?id=' in url:
                    pass
                else:
                    
                    try:
                        yield Request(url, callback=self.parse)
                    except Exception as e:
                        pass
                
            else:
                url = 'http://shop.artxun.com'+ link
                # print "++++++++++++++++++++"
                # print url
                if 'net?id=' in url:
                    pass
                else:
                    
                    try:
                        yield Request(url, callback=self.parse)
                    except Exception as e:
                        pass
                   
