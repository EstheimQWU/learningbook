# 012-python-IO
## 同步与异步
由于CPU与内存的读写速度远远高于外设的速度，因此在IO编程中，存在着速度严重不匹配的情况。往往CPU已经处理完了数据，而磁盘无法及时接收数据，造成矛盾。
+ 同步：第一种情况是让CPU等待磁盘传输完成之后再继续执行代码。
+ 异步：不让cpu等待，让磁盘与cpu继续各自工作。

## 文件读写
程序->操作系统->文件->操作系统->程序

在现代操作系统中，程序无法直接对文件进行操作。

```python
url = 'c:/github/learningbook/readme.md'
f = open(url, 'r')  # 打开文件
f.read()  # 读取文件
f.close
```

使用`try-except`管理IO
```python
try:
    f = open(url, 'r')
    f.read()
finally:
    if f:
        f.close()
```
使用`with`管理IO
```python
with open(url, 'r') as f:
    f.read()
```
> 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。
```python
for line in f.readlines():
    print(line.strip())
```
### 二进制文件
要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件。
```python
f = open(url, 'rb')
f.read()
f.close()
```
打开之后是16进制字节码。

### 字符编码
python默认读取utf-8格式，如果要读取其他编码格式的文件：
```python
f = open(url, encoding='gbk')
f.read()
f.close()
```
## 写文件
```python
f = open('/Users/michael/test.txt', 'w')
f.write('Hello, world!')
f.close()
```
使用with写文件：
```python
with open(url, 'w') as f:  # 覆写模式，使用`a`可以追加内容
    f.write('hello')
```

## 内存读写
```python
from io import StringIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())
```

## 文件与目录
使用os模块，可以容易地操作文件与目录。

```python
import os
os.name
# 获取当前文件的绝对路径
print(os.path.abspath())
# 在指定目录下创建一个新的文件夹
os.path.join('/home/qwu/', 'newdir')
# 然后创建一个目录:
os.mkdir('/home/qwu/')
# 删掉一个目录:
os.rmdir('/home/qwu/')
```

1. 合并路径时，
2. 拆分路径时，

## OS模块的补足，shutil模块
shutil提供了用于补足OS模块的函数。

## tips
```python
print([x for x in os.listdir('.') if os.path.osdir(x)])
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
```

## 序列化
> 我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
```python
import pickle
d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))
```







