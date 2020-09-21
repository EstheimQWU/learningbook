# 005-python-函数
## 001函数返回值
返回值默认为`return None`，等同于`return`或者没有返回值。

## 空函数
使用`pass`可以创建空函数，`pass`可以用作空的占位符，一个空白函数中如果缺少了`pass`，代码就无法运行。

## 参数检查
参数错误有类型错误与参数数量错误等情况，可以使用`isinstance()`函数是实现检测，再结合错误抛出可以定位输入错误的情况。

## 返回多值
python函数无法返回真正意义上的多值，当使用return语句返回多值时，其实返回的是一个包含多个值的tuple。

## 函数参数
### 位置参数
```python
def power(a, n):
    return a ** n
```
最常见的参数类型，a与n都是位置参数。

### 默认参数
```python
def power(a, n = 2):
    return a ** n
```
这里的n就是默认参数。

**问题1 为什么必选参数在前，默认参数在后？**


**问题2 设置默认参数的好处？**
设置默认参数可以降低调用函数的难度。

**问题3 默认参数本质是什么？**

**问题4 如何设置默认参数？**


### 可变参数
即，传入数量可变的参数，具体为任意个（包括0）。
```python
def num_plus(*args):
    sum = 0
    for n in args:
        sum +=
    return sum
```

**这里的numbers既可以是多个参数，也可以是一个list或者tuple**

### 关键字参数
即，关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
```python
def person(name, age, **kw):
    print('name', name, 'age', age, 'other', kw)
```

```python
>>> person('', 30, city='beijing')
name: Bob age: 35 other: {'city': 'Beijing'}
```

一般用于拓展函数功能，作为非必要信息的提供手段。

### 命令关键字参数

+ 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
```python
def person(name, age, *, city, job):
    print(name, age, city, job)
```
这个`*`后面的参数会被视为命名关键字参数。（这个参数是可变的，可以为空，但是其他的参数会无法输入。）

如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
```python
def rename_func(name, age, *, city, job):
    print(name, age, city, job)


def rename_func2(name, age, *args, city, job):
    print(name, age, args, city, job)


if __name__ == '__main__':
    rename_func('gutian', 18, city='shenzhen', job='engineer')
    rename_func2('gutian', 19, 'box', 2, 'mixed', city='shanghai', job='engineer')


> gutian 19 ('box', 2, 'mixed') shanghai engineer
```

### 参数组合
> 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：

**必选参数->默认参数->可变参数->命名关键字参数->关键字参数。**

因此能够读取所有的参数的函数就出现了：
```python
def func_1(*args, **kw):
    pass
```

或者
```python
def func_2(a, b, *, c, **kw):
    pass
```

当args是list或者tuple，kw是dict的时候，这两个变量可以作为参数输入函数中。

<u>同时使用太多的组合，会导致函数接口的可理解性很差。</u>


**默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！**

## 递归函数
```python
def factorial(n):
    if n = 1:
        return 1
    return n * factorial(n-1)
```

计算机通过栈结构实现递归算法， 如果递归层级过多会导致栈溢出。

> 解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。（然而Python解释器也没有做优化，所以还是会栈溢出）
