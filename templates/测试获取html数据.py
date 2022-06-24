import requests

a = 'http://127.0.0.1:8000/'
res = requests.get(a).text
print(res)