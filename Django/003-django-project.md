# 003-vue-django-project
## 001创建一个django项目
使用`django-admin startproject project-name`创建项目根目录。
```
    manage.py
    project-name/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

## 002配置外部数据库
打开`settings.py`文件，修改其中的`databases`项，配置数据库资料。
```python
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.mysql',   # 数据库引擎
        'NAME': 'django001',  # 数据库名，先前创建的
        'USER': 'root',     # 用户名，可以自己创建用户
        'PASSWORD': '123456',  # 密码
        'HOST': '127.0.0.1',  # mysql服务所在的主机ip
        'PORT': '3306',         # mysql服务端口
    }
}
```

## 003在项目中新建应用模块
使用`python manage.py startapp appname`命令创建新的应用模块。

创建后应用模块的目录应该如图所示
```
    polls/
        /migrations
            __init__.py
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py
```
添加`urls.py`文件，用来配置url路径。

在根应用下的settings.py文件中注册应用模块。
```python
INSTALLED_APPS = [
    'appname.apps.PollsConfig', # !
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

使用`python manage.py makemigrations polls`命令完成数据库迁移

## 004在view中编写返回值
```python
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

def userid(request):
    return HttpResponse(int(1111), content_type='application/json')
```

## 005新建一个vue项目
使用`vue init webpack vue-project`命令创建新项目

配置项目文件

## 006安装axios
`npm install axios --save`

## 007配置axios
1. 引入模块

main.js
```javascript
import axios from 'axios'

const Axios = axios.create({
  // 请求接口
  baseURL: '/api',
  // 超时设置
  timeout: 8000,
  // 请求头设置
  headers: {
    'accept': 'application/json',
    'Content-Type': 'application/json'
  }
})

Vue.prototype.$http = Axios

new Vue({
  el: '#app',
  axios,
  components: { App },
  template: '<App/>',
  render: h => h(App)
})
```
2. 代理跨域配置

添加`proxyTable`中的内容

/config/index.js
```javascript
module.exports = {
  dev: {
    // Paths
    assetsSubDirectory: 'static',
    assetsPublicPath: '/',
    proxyTable: {
      '/api': {
        target: 'http://127.0.0.1:8000/',   //这里填自己的接口地址
        changeOrigin: true,
        pathRewrite: {
          '^/api': '/'
        }
      }
    },
  }
}
```
## 008编写axios请求
编写axios请求
```javascript
methods: {
    httptest () {
      this.$http({
        method: 'get',
        url: 'userid/'  // url
      }).then((response) => {
        console.log(response.data)
      }).catch((error) => {
        console.log(error)
      })
    }
  },
```

