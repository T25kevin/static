import requests
import re
import json
url = 'https://www.bilibili.com/video/BV1NL4y1c7gJ/?spm_id_from=333.788&vd_source=9463419dd8aeecb05b5889b2ce361772'

a = requests.get(url)
b = re.search('<script>window.__playinfo__=(.*?)</script>', a.text).group(1)
c = json.loads(b)
print(type(c))
print(c)
print(c['data'])

