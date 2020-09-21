# 006-python-高级特性
## 切片
通过在数据类型后面添加`[:]`实现截取。

```python
L = [0, 1, 2]
L[:3] # 0, 1, 2
L[1:3] # 1, ,2 
```

6种数据类型中的5种都可以使用这种方法。（数字型不可以）

## 迭代
python的for可以迭代所有的可迭代对象，无论她是否有下标。

如何迭代dict:
```python
d = {"d1": 1, "d2": 2, "d3": 3}
# solution 1 默认迭代key，如果要迭代value
for one in d:
    print(one)
    print(d[one])

# solution 2 使用for value in d.values()
for value in d.values():
    print(value)

# solution 3 同时迭代key与value
for k, v in d.items():
    print(k ": " d)
```

### 如何判断一个对象是可迭代对象？
使用collections模块的Iterable类型判断可以判断一个对象是不是可迭代的。
```python
from collections import Iterable
if isinstance('abb', Iterable):
    pass
```

### 使用下标迭代
通过`enumerate`函数可以可以将一个list变为\[索引-元素\]对，这样就可以在for循环中迭代索引和元素本身。
```python
L = [1, 2, 3]
for i, value in enumerate(L):
    pass
```

## 列表生成式
### 条件筛选的列表生成
```python
# 一层
L1 = [x * x for x in range(1, 11)]

# 一层条件判断
L2 = [x * x for x in range(1, 11) if x % 2 == 0]

# 二层
L3 = [m + n for m in 'ABC' for n in 'XYZ']

# 一层条件循环
L4 = [x if x % 2 == 0 else -x for x in range(1, 11)]
```
