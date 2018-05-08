import requests
import re
def get_one_page(url):
    headers={'User_Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}

    response=requests.get(url,headers=headers)
    if response.status_code==200:
        return response.content
    else:return None
def main():
    url='http://maoyan.com/board/4'
    html=get_one_page(url).decode('utf-8')
    print(html)
def parse_one_page(html):
    pattern=re.compile
main()
