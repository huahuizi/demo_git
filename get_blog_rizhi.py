#!/usr/bin/env python
#coding:utf-8
import sys,re,requests

reload(sys)
sys.setdefaultencoding("utf-8")
url = "http://blog.artron.net/space-183160.html"
# http://blog.artron.net/space-183160.html

def getHtml(user_id):
    url = "http://blog.artron.net/space-%d.html"%user_id
    html = requests.get(url).content
    # print html
    # user_id = 183160
    try:
        zonglogs= re.search('''日志</a><em>\((.*?)\)</em></li>''', html, re.S).group(1)
        if zonglogs:
            print divmod(int(zonglogs), 10)[0]
            if divmod(int(zonglogs), 10)[1]>0:
                pages = divmod(int(zonglogs), 10)[0]+1
                for page in range(1,pages+1):
                    user_log_url = "http://blog.artron.net/space.php?uid=%d&do=blog&view=me&page=%d&ajaxdiv=maincontent&inajax=1&ajaxtarget=maincontent&inajax=1"%(user_id,page)
                    userlog = requests.get(user_log_url).content
                    for pageurl in re.findall(r'<h4><a href="(.*?)" target="_blank" >', userlog, re.S):
                        open('pageurls.txt','a+').write(pageurl+"\n")
    except Exception as e:
        pass

            # print re.findall(r'<h4><a href="(.*?)" target="_blank" >',userlog, re.S)

'''
onclick="getindex('blog');">日志</a><em>(106)</em></li>
<a href="javascript:;" onclick="getindex('blog');">日志</a>
</span>
<h4><a href="http://blog.artron.net/space-183160-do-blog-id-1040311.html" target="_blank">今日美术馆照片</a></h4>
'''

if __name__ == '__main__':
    for i in xrange(10,1000):
        getHtml(i)
