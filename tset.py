import requests
from lxml import etree


headers = {
            'Referer': 'https://github.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Host': 'github.com'
        }
login_url = 'https://github.com/login'
post_url = 'https://github.com/session'
logined_url = 'https://github.com/settings/profile'
session = requests.Session()

# 建立会话
response = session.get('https://github.com/login')
selector = etree.HTML(response.text)
token = selector.xpath('//form/input[2]/@value')
print(token[0])

post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': token[0],
            'login': 'scdadaguo',
            'password': 'guohao808'
        }
response=session.post(post_url, data=post_data, headers=headers)
if response.status_code == 200:
    pass

response2=session.get(logined_url, headers=headers)
if response2.status_code == 200:
    selector2 = etree.HTML(response2.text)
    print(response2.text)
    name = selector2.xpath('//div[@class="col-9 float-left"]//div[@class="column two-thirds"]//dd/input/@value')[0]
    print(name)


