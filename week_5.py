import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#url = 'http://py4e-data.dr-chuck.net/comments_678422.xml'
url = input("Enter url")
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
tree = ET.fromstring(data)
el_list=tree.findall('comments/comment')
lst=[]
for item in el_list:
    lst.append(int(item.find('count').text))
print(sum(lst))
