# 013-常用内建模块
## datetime
datetime常用于处理python内的日期与时间。
```python
from datetime import datetime
now = datetime.now()
print(now)
```
`datetime.now()`返回当前的日期与时间，类型是datetime

构造datetime对象
```python
import datetime
dt = datetime.datetime(2020, 4, 15, 12, 20)
print(dt)
```

将`datetime`类型转换为timestamp：
```python
from datetime import datetime
dt = datetime(2020, 2, 1, 12 20)
dt.timestamp()
datetime.fromtimestamp(dt.timestamp())
```

使用timedelta进行时间运算
```python
from datetime import datetime. timedelta

now = datetime.now()
now + timedelta(hours=10)
```

使用`timezone`进行时区转换


## collections
collections提供了许多集合类。
`nametuple`是一个函数，用来创建一个自定义的`tuple`对象，并且规定了`tuple`元素的数量，并且可以用属性而不是索引来引用tuplp的某个元素。

`deque`不同于list的线性存储，高校实现了插入与删除操作的双向列表，适合队列与栈。
```python
from collections import deque
q = deque(['1', '2', '3'])
q.append('x')
q.pop()
q.appendLeft('y')
```

## base64
Base64是一种用64个字符来表示任意二进制数据的方法。
```python
base64.b64encode(b'binary\x00string')
```

## struct
struct模块可以辅助处理字节数据类型。
```python
import struct
struct.pack('>I', 10240099)
```
其中`pack`的第一个参数是处理命令：
> `>`表示字节的顺序是big-endian，属于网络序
> 
> `I`表示4字节无符号整数。

`unpack`可以将字节类型变为相应的数据类型

## hashlib
`hashlib`模块提供了常见的摘要算法，如MD5、SHA1等。
```python
import hashlib

md5 = hashlib.md5()
md5.update('this is a md5 test.'.encode('utf-8'))
print(md5.hexdigest())
```
如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的。
```python
import hashlib

md5 = hashlib.md5()
md5.update('this is '.encode('utf-8'))
md5.update('a md5 test.'.encode('utf-8'))
print(md5.hexdigest())
```

## hmac
Hmac算法：Keyed-Hashing for Message Authentication。它通过一个标准算法，在计算哈希的过程中，把key混入计算过程中。
```python
import hmac
message = b'hmac'
key = b'key'
h = hmac.new(key, message, digestmod='MD5')
...
h.hexdigest()
```

## itertools迭代器
1. count()无限迭代器
2. cycle()将传入的序列无限重复
3. repeat(x, y)把第一个参数重复，第二参数可以限定轮次

4. chain()将一组迭代对象串联起来，形成一个更大的迭代器
5. groupby()将迭代器中相邻的重复元素挑出来放在一起

## urllib
好用的url操作库
