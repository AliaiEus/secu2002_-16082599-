import json
import requests
f = ('https://api.github.com/repos/smeiklej/secu2002_2017/commits')
r = requests.get(f)
text = json.loads(r.text)


#for x in text:
    #print x['commit']['message']

print map(lambda x: x['commit']['message'], text)
