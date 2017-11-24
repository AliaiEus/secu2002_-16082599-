import json
import requests
f = ('https://shapeshift.io/recenttx/50')
r = requests.get(f)
text = json.loads(r.text)

import pickle
pickle.dump(text, open('shapeshift.p', 'wb'))
