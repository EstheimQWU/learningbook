# 010-python-面向对象2
## 给实例绑定属性与方法
从类中实例化出的实例是可以被额外添加属性与方法的。
```python
class Man(object):
    pass

m = Man()
m.name = 'tom'
print(dir(m))  # m中有name这个属性

def set_name(self, age):
    self.age = age

m.set_age = MethodType(set_age, s)  # 添加方法
```
也可以通过给类class绑定方法使得所有从这个类被实例化的实例都可以使用这个被绑定的方法。

这种动态绑定功能是动态语言区别与静态语言的一种特性。

### 使用__slots__限制类内允许绑定的属性或者方法
```python
class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称
```
`__slots__`传入的是一个元组。

`__slots__`仅对当前类有作用，对于继承其的子类是没有作用的。

如果希望子类也有作用，需要在子类中定义`__slots__`，这样子类就会拥有自身的`__slots__`与父类的`__slots__`了。

## @property装饰器
@property装饰器在保持代码简洁的情况下，保证了对参数进行必要检查的过程。
```python
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
```

## 多重继承
通过多重继承，一个子类就可以同时获得多个父类的所有功能。

## 为什么java不可用多重继承，而python可以（重点）
暂略

## MixIn
> 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。

> MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。

> 由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。

> 只允许单一继承的语言（如Java）不能使用MixIn的设计。

