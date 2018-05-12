import requests
from lxml import etree
import pymysql

for i in range (1,10):
    url='http://www.66ip.cn/'+str(i)+'.html'
    response=requests.get(url)
    response.encoding='gb2312'
    selector=etree.HTML(response.text)
    data=selector.xpath('//div[@id="main" and @class="container"]//table//tr//td[1]//text()')
    data2=selector.xpath('//div[@id="main" and @class="container"]//table//tr//td[2]//text()')
    ip_list=data[1:]
    duankou_list=data2[1:]
    a=[]
    for i in duankou_list:
        s=':'+i
        a.append(s)
    ip_daili_list=[]
    for i in range(0,len(ip_list)):
        # ip_daili_list.append(ip_list[i]+a[i])
        ip=ip_list[i] + a[i]
    # print(ip_daili_list[0])
        db = pymysql.connect(host='localhost', user='root', password='', port=3306, db='spiders')
        cursor = db.cursor()
        sql = 'INSERT INTO IP VALUES (%s)'
        try:
            cursor.execute(sql, (ip))
            db.commit()
        except:
            db.rollback()
        db.close()








