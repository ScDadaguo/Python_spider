from urllib import request
import json
req=request.Request('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')
with request.urlopen(req) as f:
    data = f.read().decode('utf-8','ignore')
    print('Status:', f.status, f.reason)
    print('\n')
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('\n')
    print(data)
    print(type(data))
    data=json.loads(data)
    print(type(data))