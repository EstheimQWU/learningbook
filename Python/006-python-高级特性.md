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

## 生成器
通过生成器可以动态地生成列表的一部分并且投入使用中。
```python
# 直接定义
G = (x * x for x in range(10))
```
这里的G是一个算法，而不是一个确切的数据结构，因此其中的内容是无法被直接访问的，需要通过计算后才能得到。虽然使用`next(G)`可以按顺序访问到单个的元素，但是这种方法太奇怪了也不方便操作，因此一般不会采取这种操作方式。使用迭代是常见的访问方式。
```python
g = (x for x in range(10, 100, 5))
for i in g:
    print(i)
```

**yield**

在函数中添加`yield`可以将一个函数转换为一个generator。如果一个函数中包含了`yield`关键字那么它的类型就变成了生成器对象（generator）。

> function与generator的执行流程不一样，前者是顺序执行，遇到`return`或者迭代结束就返回，而后者在每次调用next()时执行，遇到`yield`语句时返回，再次执行时从上次返回的`yield`处继续执行。

换而言之，只要有`yield`后面还有代码，generator就会认为后续还可以继续生成元素（输出正确的同时，会报错）；如果后面没有代码，则不会再执行，也不会报错。

**generator的返回值**
使用for循环调用generator时，发现无法获取generator的return语句的返回值。如果想要拿到返回值，则必须捕获`StopIteration`错误，返回值包含在`StopIteration`的value中。（利用异常获取需要的值）

## 迭代器
### 什么是迭代器
这些可以直接作用于for循环的对象统称为可迭代对象：`Iterable`，`Iterable`包含：
+ 集合数据类型，即除了数字型以外的基础数据类型。
+ generator，包含生成器与携带`yield`的生成器函数。

前文有提到使用`isinstance()`可以判断一个对象是否是`Iterable`对象。
```python
isinstance([], Iterable)
```

> 可以被next()函数调用并不断返回下一个值的对象，直到最后抛出`StopIteration`错误的被称为迭代器：Iterator。

### 判断迭代器
生成器都是`Iterator`对象，而`str`, `list`, `dict`虽然是`Iterable`，但是却不是`Iterator`，这里可以用`isinstance()`判断是不是，注意**参数**。
```python
isinstance([], Iterator)
```

### 转换为迭代器
使用`iter()`函数可以把`list`, `dict`, `str`等`Iterable`类型转换为`Iterator`类型。

**tips:** `Iterator`对象是一个数据流，表示一个惰性计算的有序序列。

*for循环的实现->next()*