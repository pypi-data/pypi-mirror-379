import requests


for i in range(3):
    res = requests.get("https://www.baidu.com")
    print(res.content)
