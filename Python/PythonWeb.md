---
title: PythonWeb
date: 2018-12-15 12:08:21
tags: 
    - Web
categories: 
    - Python
---

💠

- 1. [Web](#web)
    - 1.1. [FastAPI](#fastapi)
    - 1.2. [Django](#django)
    - 1.3. [Flask](#flask)
        - 1.3.1. [跨域](#跨域)

💠 2024-04-22 16:41:19
****************************************

# Web
> [Awesome Python Web Frameworks](https://github.com/sfermigier/awesome-python-web-frameworks)

> python内置一个简易的W静态eb服务器 只需在静态资源的根目录下执行  
- python2 `python -m SimpleHTTPServer [8000]`
- python3 `python3 -m http.server [8000]`

## FastAPI
[Github](https://github.com/tiangolo/fastapi)

## Django
- 安装Django `pip install Django`
- 创建项目 `django-admin.py startproject first_pro . `
    - `ls first_pro`查看到创建的默认文件
- 创建SQLite数据库 `python manage.py migrate`    
- 启动项目`python3 manage.py runserver`

## Flask
开发一个简易RESTful风格的服务器
> [官方文档 ](http://www.pythondoc.com/flask-restful/first.html#python-flask-restful-api) `但是这个内置的web服务器性能很渣`
> [教程文档](https://www.tutorialspoint.com/flask/index.htm)

### 跨域
> [解决方式](https://blog.csdn.net/yannanxiu/article/details/53036508)
`pip install flask-cors`

```python
    from flask_cors import *

    app = Flask(__name__)
    CORS(app, supports_credentials=True)
```

