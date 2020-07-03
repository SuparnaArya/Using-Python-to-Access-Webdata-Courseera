import json
import urllib.request,urllib.parse,urllib.error
import  ssl

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url="http://py4e-data.dr-chuck.net/comments_678423.json"
uh=urllib.request.urlopen(url,context=ctx)

data=uh.read().decode()

info = json.loads(data)

count_list=[]

for item in info['comments']:
    count_list.append(int(item['count']))

print(sum(count_list))
