from urllib  import request
import re
import json

def write_to_file(content):
    with open('result.txt','a',encoding=('utf-8')) as f:
        f.write(json.dump(content,ensure_ascii=False)+'\n')

url='http://maoyan.com/board/4'
headers={'User_Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
req=request.Request(url=url,headers=headers,method='GET')
response=request.urlopen(req).read().decode('utf-8')

pat1=' <p class="name"><a href="/films/.*?" title=".*?" data-act="boarditem-click" data-val="{movieId:.*?}">(.*?)</a></p>'
pat2='''<p class="star">
                主演：(.*?)
        </p>'''
pattern_film=re.compile(pat1,re.S)
pattern_action=re.compile(pat2,re.S)
items_film=re.findall(pattern_film,response)
items_action=re.findall(pattern_action,response)
a=dict
b=[]
for i  in range (0,10):
    a={'film':items_film[i],'action':items_action[i]}
    with open('result.txt','a',encoding=('utf-8')) as f:
            f.write(str(a))






