#!/usr/bin/python  
#-*-coding:utf-8-*-  
from agents import AGENTS
import random  
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware  
  
class RotateUserAgentMiddleware(UserAgentMiddleware):  
    def __init__(self, user_agent=''):  
        self.user_agent = user_agent  
  
    def process_request(self, request, spider):  
        ua = random.choice(AGENTS)  
        if ua:  
            # print ua  
            request.headers.setdefault('User-Agent', ua)
        else:
            print "no user agents"      
  
    