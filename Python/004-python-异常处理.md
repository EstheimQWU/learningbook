# 004-python-异常处理.md
## 异常
```python
try:
    pass
except ValueError as e:
    pass
finally:
    pass
```
如果发生了不同类型的错误，应该由不同的except语句块处理。
Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，也覆盖其子类。

https://docs.python.org/3/library/exceptions.html#exception-hierarchy

> 出错的时候，一定要分析错误的调用栈信息，才能定位错误的位置。

## 抛出异常
```python
# err_raise.py
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')
```

## 调试
### 打印-print
```python
x = 10
print(x)
```

### 断言-assert
```python
assert n !=0, 'n is zero'
```
assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。

如果断言失败，assert语句本身就会抛出AssertionError。

### 日志-logging
```python
import logging
n = 10
logging.info('n =%d' % n)
```

### 调试器pdb
```python
s = '10'
n = int(s)
print(10 / n)
```

### IDE调试
略
