import requests

url='https://games.mobileapi.hupu.com/3/7.1.20/nba/getNews?clientId=34059763&pre_count=0&advId=248CFDD3-C6B1-4EE7-91F3-BBA7D02740B6&nid=0&token=MjMwNTkxMg==%7CMTUyMDA1OTMwMA==%7C4c60492873940f934a697eaa96b4ed04&num=20&direc=next&preload=0&night=0&crt=1526104482&client=c134be5aff7be443fd3e0cf08bbcecc039c33955&time_zone=Asia%2FShanghai&sign=12eb65ece30aab1402779f33f7f07e2d'
URL='https://bbs.mobileapi.hupu.com/3/7.1.20/forums/getForumsInfoList?sign=070e5cdd56446fdf70ce08f2d2720da0&clientId=34059763&advId=248CFDD3-C6B1-4EE7-91F3-BBA7D02740B6&fid=1048&type=2&token=MjMwNTkxMg==%7CMTUyMDA1OTMwMA==%7C4c60492873940f934a697eaa96b4ed04&stamp=0&night=0&crt=1526109042&time_zone=Asia%2FShanghai&client=c134be5aff7be443fd3e0cf08bbcecc039c33955&page=1'
headers={
    'User-Agent':'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;'
}
response=requests.get(url=url,headers=headers,verify=False)
json=response.json()
print(json)
print(type(json))
a=json['result']['data'][0]
print(a)


