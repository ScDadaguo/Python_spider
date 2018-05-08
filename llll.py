import requests
from lxml import etree
data={'name':'germey','age':'22'}
r=requests.post("http://htttpbin.org/post",data=data)
print(r.text)
