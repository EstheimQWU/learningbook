# python第三方库requests
## pip install requests

## 请求
```python
import requests

r1 = requests.get('https://www.github.com/estheimqwu')
r2 = requests.get(url='https://dict.baidu.com/s', params={'wd': 'python'})
```

多种方法
```python
r1 = requests.get('https://github.com/timeline.json')                                # GET请求
r2 = requests.post('http://httpbin.org/post')                                        # POST请求
r3 = requests.put('http://httpbin.org/put')                                          # PUT请求
r4 = requests.delete('ttp://httpbin.org/delete')                                     # DELETE请求
r5 = requests.head('http://httpbin.org/get')                                         # HEAD请求
r6 = requests.options('http://httpbin.org/get')                                      # OPTIONS请求
```

## 相应内容
```python
r.encoding = 'utf-8'
r.text
r.content
r.headers
r.status_code
r.raw
r.ok
r.json()
r.raise_for_status()
```

posts发送json请求
```python
import requests
import json

r = requests.post('https://api.github.com/some/endpoint', data = json.dumps({'key': 'value'}))
print(r.json())
```

## 定制头与cookie信息
### 定制头
```python
header = {'user-agent': 'my-app/0.0.1''}
cookie = {'key':'value'}
r = requests.get/post('your url',headers=header,cookies=cookie) 
```

### cookie信息
```python
data = {'some': 'data'}
headers = {'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
 
r = requests.post('https://api.github.com/some/endpoint', data=data, headers=headers)
print(r.text)
```

## 相应状态码
### 编码
```python
r = requests.get('https://estheimqwu')
print(r.text, '\n{}\n'.format('*'*10), r.encoding)
r.encoding = 'GBK'
print(r.text, '\n{}\n'.format('*'*79), r.encoding)
```

### 响应码
```python
import requests

r = requests.get('https://github.com/estheimqwu')        # 最基本的不带参数的get请求
print(r.status_code)                                # 获取返回状态
r1 = requests.get(url='http://dict.baidu.com/s', params={'wd': 'python'})      # 带参数的get请求
print(r1.url)
print(r1.text)                                      # 打印解码后的返回数据
```
使用`r.status_code`方法可以抛出异常。

