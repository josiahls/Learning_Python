"""
Parsing websites
"""

import urllib.request
import urllib.parse
import re

url = 'http://pythonprogramming.net'
values = {'s':'basics', 'submit':'search'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

print(respData)

# what we are going through: <p> content grfdgstrsgstrgr <\p>
# so we want to parse everything between paragraph tags
# the statement: .*? means any character except for new line, 0
# or more repetitions, and 0 or 1 repetitions
paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))

for eachP in paragraphs:
    print(eachP)