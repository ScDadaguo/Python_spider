import requests
import re
import time

index=2299135

while True:
    print('index为',index)

    url_news='http://games.mobileapi.hupu.com/3/7.1.20/news/createNewsDetailH5?offline=json&nid='+str(index)+'&leaguesEn=nba&entrance=&night=0&nopic=0&time_zone=Asia%2FShanghai&client=c134be5aff7be443fd3e0cf08bbcecc039c33955&webp=0'
    url_comments='http://games.mobileapi.hupu.com/3/7.1.20/news/getCommentH5?offline=json&nid='+str(index)+'&leaguesEn=nba&entrance=&night=0&nopic=0&time_zone=Asia%2FShanghai&client=c134be5aff7be443fd3e0cf08bbcecc039c33955&webp=0'
    headers={
        'User-Agent':'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;'
    }
    response = requests.get(url=url_news, headers=headers, verify=False)
    print( response.json()['data']['is_admin'])

    # 提取新闻
    response=requests.get(url=url_news,headers=headers,verify=False)
    json=response.json()
    print(json)
    try:
        title=json['data']['news']['title']
        html=json['data']['news']['content']
        dr = re.compile(r'<[^>]+>',re.S)
        dd = dr.sub('',html).replace('&ldquo;','').replace('&nbsp;','').replace('&rdquo;','')
        dd1= ''.join(dd.split())
        dd1=title+"\n"+dd1
    except Exception:
        print("暂时未更新新闻，在等待下一条新闻出现，等待时间为1分钟——————————————————————————————————")
        print("\n")
        time.sleep(60)
        continue
        # # 提取热评
    dd_last = ''
    try:
        response=requests.get(url=url_comments,headers=headers,verify=False)
        json=response.json()

        for i in json['data']['light_comments']:
            html=i['user_name'] + ':' + i['content']
            dr = re.compile(r'<[^>]+>', re.S)
            dd = dr.sub('', html).replace('&ldquo;', '').replace('&nbsp;', '').replace('&rdquo;', '')
            dd = ''.join(dd.split())+"\n"
            dd_last=dd+dd_last
        print("\n")
    except Exception :
            print("没有热评")
            index = index + 1
            continue
    index=index+1
    news=dd1+"\n"+dd_last


