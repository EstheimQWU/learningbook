# 007-python-函数式编程
## 高阶函数
以其他函数作为输入参数的函数被称为高阶函数。
```python
def add(a, b):
    return a + b

def higher_order_func(a, b, add):
    return 5 * add(a, b)
```

## map/reduce
### map()函数
> `map()`函数接受两个参数，一个是函数，另一个是`Iterable`，`map()`将传入的函数依次作用到序列的每个元素，并把结果作为新的`Iterator`返回。


### reduce()
`reduce`会把结果继续和序列的下一个元素做累积计算。
```python
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1 x2), x3), x4)
```

## filter
`filter()`函数用于过滤序列，与`map``reduce`相同都是接收一个函数与一个序列。`filter()`会把传入的函数作用于每一个值，然后根据返回值是`True`还是`False`决定保留还是丢弃该元素。

## sorted
使用`sorted()`函数可以对list进行排序：
```python
sorted([23, 1, -22, 56, 3])
```
同时`sorted()`可以接受一个KEY函数来实现自定义的排序，比如按照绝对值大小排序。
```python
L = [-21, 22, 54, -3]
sorted(L, key=abs)
```
先使用key函数作用于每一个待排序的值上，接着对他们进行排序。

## 返回函数
高阶函数除了可以把函数作为输入参数外，还可以把函数作为输出结果返回。

返回函数在使用时需要注意到，返回值是一个函数，而不是函数的计算结果，需要调用函数才可以获取对应的计算结果。
```python
def cal(*args):
    def func():
        sum = 0
        for i in args:
            sum = sum + n
        return sum
    return sum

if __name__ == '__main__':
    f = cal(1, 2, 4, 5)
    # f -> functon
    # f() -> 12
```

### 闭包
```python
# 廖雪峰老师的例子
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(), f2(), f3())
```
在f1、f2、f3被赋值的时候，其实是把存在fs中的函数赋予了他们，而不是函数最后计算出的值。而这个最后计算出的值会等到函数被调用，执行计算的时候才去获取需要的变量，而不是函数被赋值的时候去计算。

**返回函数不要引用任何循环变量，或者后续会发生变化的变量。**

## 匿名函数
匿名函数，也就是非显性定义的函数，python对匿名函数提供了有限的支持。
```python
lambda x: x * x
```
这个函数等同于
```python
def f(x):
    return x * x
```

## 装饰器
decorator本质上是一个返回函数的高阶函数，假设我们要实现一个在函数调用前后自动打印日志的功能，但是希望将打印日志功能与函数本身的功能剥离开来。
```python
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def func():
    print(1)
```

如果装饰器自身需要又参数传入的话，情况又会发生变化。
```python
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('call')
def func():
    print(1)
```

## 偏函数
这里的偏函数不同于数学意义上的偏函数，python中通过设定参数的默认值，可以降低函数调用的难度，偏函数也可以做到这一点。

`functools.partial`可以帮助我们创建一个偏函数，不需要自己去设定参数的默认值。
```python
def func(x, base=2):
    return int(x, base)
# 等同于
func = functools.partial(int, base=2)
```
`functools.partial`的作用是，将一个函数中的某些参数固定住，并且返回一个新的函数，使得这个新函数的使用更加简单。

