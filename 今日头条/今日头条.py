import requests
from urllib.parse import urlencode

def get_page(offset):
        params={
            'offset':offset,
            'format':'json',
            'keyword':'街拍',
            'autoload':'true',
            'count':'20',
            'cur_tab':'1',
            # 'from':'search_tab'
        }
        url='https://www.toutiao.com/search_content/?'+urlencode(params)
        try:
            response=requests.get(url)
            if response.status_code==200:
                return response.json()
        except requests.ConnectionError:
            return None

def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            title=item.get('title')
            images=item.get('image_list')
            try:
                for image in images:
                    yield{
                        'image':image.get('url'),
                        'title':title
                    }
            except:
                pass


import os
from hashlib import  md5

def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        response=requests.get('http:'+item.get('image'))
        if response.status_code==200:
            file_path='{0}/{1}.{2}'.format(item.get('title'),md5(response.content).hexdigest(),'jpg')
            if not os.path.exists(file_path):
                with open(file_path,'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloaded',file_path)
    except requests.ConnectionError:
        print('Failed to Save image')

def main(offset):
    json=get_page(offset)
    print(get_images(json))
    for item in get_images(json):
        try:
            print(item)
            # save_image(item)
        except:
            pass


main(0)
