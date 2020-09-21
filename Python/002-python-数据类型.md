# 002-python-数据类型

## 001数字型
### 001整型
1. 使用数学方法
`1111`, `2222`, `-100`, `0`

2. 使用十六进制
`0xff00`, `0xc34d`

3. 使用'_'分隔符
对于数值非常大的数字可以使用`_`符号去分隔便于阅读，其效果与常规写法完全相同。
`100_000_000_000`, `9_9999_9999`

4. 除法
`10/3`精确除
`10//3`整除
`10%3`取余

### 002浮点型
1. 科学计数法
使用e替代10，例如
`1.1e9`, `1.23e-6`
2. 非科学计数法
`1.1`, `1.23`, `-6.2`

### 003布尔值
True、False
布尔值可以使用`and`, `or`, `not`运算。
与、或、非

### 004空值
使用`None`表示。

## 002字符串
以单引号或者双引号括住任意文本，通过转义字符可以控制一些关键字符的书写。

通过在字符串前加上r，可以使得字符串内的文本全部不转义
`r'string'`

为了简化，python允许使用'''...'''的三引号的格式表示多行内容，简而言之就是可以使得字符串换行。

### 001字符串enhanced
#### 001字符编码
ASCII -> Unicode -> utf-8
对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符。
```python
ord('A')
ord('霹')
chr(65)
chr(25991)
```
在字符串前加b可以将之转变为以自己为单位的`bytes`
这个过程可以通过`decode()`方法逆转，使得`byte`变为`str`。
```python
 b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
```
一些常见的抬头
```shell
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
```

#### 002格式化
1. 使用%实现，用%号隔开。
```python
'Hi, %s, you have $%d.' % ('Michael', 1000000)
'Hi, Michael, you have $1000000.'
```

2. 使用.format()实现
```python
'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
```

1. f-string
```python
r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')
```

## 003tuple
tuple一旦初始化就不能修改，属于不可变有序列表。

Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号。
`tuple=(1,)` install of `tuple=(1)`

当一个动态可变的数据类型处于tuple中时，这个动态可变的数据类型是可以被改变的，然而不可以把这个动态数据类型从tuple中删除。
```python
t = (1, 2, 3)
t = (1, )
```

## 004list
可变有序集合，本质上是长度动态变化的数组（cpython层面）。

常见方法可在builtins.py文件中查看。
builtins.py是一个特殊的模块，需要与phello、importlib、builtins、this与struct模块一起讲。（滑稽）

## 005dict
dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
属于无序可变列表。

这种key-value存储方式，在放进去的时候，必须根据key算出value的存放位置，这样取的时候才能根据key直接拿到value

`in`可以判断key是否存在：
```python
d={'example': 111}
'example' in d # true or false
```

**dict内部存放的顺序和key放入的顺序是没有关系的。**

和list比较，dict有以下几个特点：
+ 查找和插入的速度极快，不会随着key的增加而变慢；
+ 需要占用大量的内存，内存浪费多。

而list相反：
+ 查找和插入的时间随着元素的增加而增加；
+ 占用空间小，浪费内存很少。

所以，dict是用空间来换取时间的一种方法。

## 006set
属于无序可变列表。重复元素在set中会自动被过滤。

输入需要一个列表：
```python
s = set([1, 2, 3, 4])
# or
ss = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
```

> 两个set可以做数学意义上的交集、并集等操作。

**001\002\003是不可变数据类型**

**004\005\006是可变数据类型**