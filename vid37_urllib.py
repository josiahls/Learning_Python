"""
This is module 'urllib', you can access the web by python
NOTE THAT YOU SHOULD USE API
ESPECIALLY ON LARGE WEBSITES WITH LARGE AMOUNTS
OF DATA
"""

# you have to do it this way for py 3
import urllib.request

# performs a get request tot he website
# THIS IS A GET
# x = urllib.request.urlopen('http://www.google.com')
# print(x.read())

import urllib.parse

# THIS IS A POST
url = 'http://pythonprogramming.net'
# values that we are looking for
values = {'s': 'basic', 'submit': 'search'}

# use encoding for adding values, since it
# will handle the questions marks, spaces ect...
data = urllib.parse.urlencode(values)
# what kind of ecoding do we want to use
data = data.encode('utf-8')
# the actual request
req = urllib.request.Request(url, data)
# actually respond
resp = urllib.request.urlopen(req)
respData = resp.read()

print(respData)

# this will fail
# since google will not allow bots
try:
    x = urllib.request.urlopen('http://www.google.com/search?q=test')
    print(x.read())
except Exception as e:
    print(str(e))

# you can get around this by:
try:
    url = 'http://www.google.com/search?q=test'
    # header contian diferent things about you that
    # that websites use to identify you
    headers = {}
    # this is  user agent
    # i just went and copied one form the web
    # it was easy, and will trick the website
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    # add the data to the file
    saveFile = open('withHeaders.txt', 'w')
    saveFile.write(str(respData))
    saveFile.close()
except Exception as e:
    print(str(e))
