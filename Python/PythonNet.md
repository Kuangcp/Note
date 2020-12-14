---
title: Python网络编程
date: 2018-12-15 12:08:54
tags: 
categories: 
    - Python
---

**目录 start**

1. [网络编程](#网络编程)
    1. [WebAPI](#webapi)
        1. [JSON](#json)
    1. [Web工具](#web工具)
1. [爬虫](#爬虫)
    1. [安装所需模块](#安装所需模块)

**目录 end**|_2020-12-14 19:57_|
****************************************
# 网络编程
## WebAPI
### JSON
```python
    # json response
    import requests
    import json

    def main():
        url = "https://xxxx.com/user/get"
        request = requests.get(url)
        re_dict = json.loads(request.text)
        for i in range(len(re_dict)):
            event = re_dict[i]
            print(event['project']['path'])
```

```python
    # json request
    import http.client
    import json
    import time

    test_url = 'xxx.net'

    conn = http.client.HTTPSConnection(online)
    headers = {'Content-type': 'application/json',"Cookie":"JSESSIONID=c946645a-21d4-4c57-b061-26c3f4a1b8ce"}

    def request(id):
        foo = {
            "id": id,
            "pass": True
        }

        json_data = json.dumps(foo)
        conn.request('POST', '/submit', json_data, headers)
        response = conn.getresponse()
        print(response.read().decode())
```


## Web工具
- `pip install httpie` 
    - `http --json URL` 格式化输出json

- `curl URL|python -m json.tool ` 格式化输出JSON

# 爬虫
## 安装所需模块

`解析HTML`
- bs4 ：`sudo pip3 install bs4`
- lxml :`sudo pip3 install lxml`
