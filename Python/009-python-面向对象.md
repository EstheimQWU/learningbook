# 009-python-面向对象
## 面向对象三大特性：封装、继承和多态
+ 封装
+ 继承
+ 多态

## 类->class、实例（对象）->instance
```python
class Student(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id
    pass


if __name__ == '__main__':
    bob = Student('bob', 1)
```

> 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别。

## 封装
当涉及类内数据的使用时，使用定义在类内部的函数去调用类内数据以达到封装数据的效果，使得数据可以被调用而无法知道内部实现的细节。

## 访问限制
一般来说，不加限制的类内数据依然是可以被外部直接访问的，为了数据的安全性，因此要限制类内数据的访问权限。

python中的`private`可以通过在变量前加上`__`实现，例如`__name`。

如果外部要访问属性，可以通过编写set与get方法实现。

`_name`这种一道下划线的情况是可以被外部访问，但是提示阅读者把她当作一个私有变量，避免在外部直接调用。常被称为保护变量，意思是只有类实例和子类实例能访问到这些变量，
需通过类提供的接口进行访问；不能用'from module import *'导入

**重点**

`__name`也没有从根本上避免这个变量从外部被调用，其原理是将其解析为另一个命名的变量，如果能够得到那个“真名”，那么依然是可以从外部对这个变量进行直接操作的。

## 继承与多态
### 继承
```python
class Animal():
    run()

class cat(Animal):
    def run(self):
        print('Dog is running~')
```

### 多态
python中的多态，一个父类拥有一个方法`run()`，继承自这个父类的子类无论怎么自定义这个`run()`方法都可以让使用这个方法的函数或者方法去调用这个`run()`。

**动态语言的python与静态语言**
由于python是动态语言且没有变量声明，因此在python中有一个bug，只要方法名字相同，就可以调用这个与父类没有关系的方法。
```python
# 父类
class Animal(object):
    def run(self):
        print("Animal is running...")
# 子类
class Dog(Animal):  
    pass
# 与Animal毫无关系的一个类
class Car(object):  
    def run(self):
        print('Car is running...')
# 由于没有变量声明，传进去的谁也不知道是啥
def run_twice(animal):
    animal.run()

# 但是都能跑
run_twice(Car())
run_twice(Cat())

# 如果是java这种静态语言就无法通过编译过程，在类型声明与检测的过程中就会报错。
```

### 获取对象类型的几种方法
1. `type(instance)`
2. `types.FunctionType`
3. `isinstance(instance, class)`->`True/False`
4. `dir()`可以返回一个包含字符串的list，其中获得一个str对象的所有属性和方法。

**tips**

hasattr(instance, name)用于判断对象内部是否拥有`name`标识的这个属性或者方法，返回`True`OR`False`。

## 实例属性与类属性
这是实例属性`name`
```python
class Student(object):
    def __init__(self, name):
        self.name = name
```

这是类属性`name`
```python
class Student(object):
    name = 'Student'
```
> 不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。
