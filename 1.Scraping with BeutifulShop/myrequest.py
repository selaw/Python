import urllib.request

req = urllib.request.Request("https://www.pythonprograming.net", headers={'User-Agent':'Mozilla/5.0'})

resp=urllib.request.urlopen(req)

#print(resp.read())

import urllib.parse

url = 'https://www.pythonprogramming.net'
values={'q':'python'}

data=urllib.parse.urlencode(values)

data=data.encode('utf-8')

req=urllib.request.Request(url,data)

resp=urllib.request.urlopen(req)

RespData=resp.read()

print(RespData)