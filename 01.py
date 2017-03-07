#!/usr/bin/env python
#coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


for x in xrange(1,1712893):
    open('users.txt','a+').write("http://blog.artron.net/space-%d.html"%x+"\n")
