# fp-d03.md
## 字典与集合
### 散列表
1、原子类型、扁平容器都是散列的，而其他是非散列的，如果一个容器中包含非原子类型的对象的引用，那么他就会变得不散列（例如元组中包含列表）。
2、一般来讲用户自定义的类型的对象都是可散列的，散列值就是id()函数的返回值。
#### 常见字典方法
字典推导（dictcomp）
update方法处理参数m的方式，是典型的“鸭子类型”。函数首先检查m是否有keys方法，如果有那么update函数就会把它当作映射对象来处理。如果没有，函数就会退一步，转而把m当作包含了键值对(key, value)元素可迭代对象来初始化一个映射对象。
#### 如何处理查找不到得键
##### 使用setdefault处理查找不到键的情况。
两种寻找按图索骥的方法：
1. `d[key]`在无法找到正确的键的时候，python会抛出异常。
2. `d.get(k, default)`在无法找到正确的键的时候，python会给一个默认的返回值。这种方法虽然也有返回值，但是在用于更新字典的时候会显得不合适，效率低。
```python
my_dict.setdefault(key, []).append(new_value)
```
与
```python
if key not in my_dict:
    my_dict[key] = []
my_dict[key].append(new_value)
```
等同。

##### 使用defaultdict处理无法查找正确键的情况
defaultdict有点看不懂。

#### 特殊方法`__missing__`
一个特殊的方法，基类dict并没有定义这个方法，但是如果有一个类继承并提供了`__missing__`方法，那么在`__getitem__`碰到找不到键的时候，python就会自动调用它，而不是抛出KeyError。
`__missing__`方法也只会被`__getitem__`方法调用。

这`StrKeyDict0`又是咋回事？？

哦哦，这个意思。
```python
class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()
```
> P148

#### 标准库中dict类型的变种
##### 字典的变种
```python
collections.OrderedDict()  # 
collections.ChainMap()  # 
collections.Counter()  # 
collections.UserDict()  # 
```

##### UserDict()
`UserDict`是一个使用纯python实现的一个Dict基类。
> 关于从dict或者其他内置类继承到底有什么不好，详见 12.1 节。

@不可变映射类型。（**什么是映射类型**？）
#### set与frozenset类型
set是集合，frozenset是不可变集合。。。完事儿了？

集合中的元素是可散列的，set类型本身是不可散列的，而frozeset本身是可以散列的。因此可以创建一个包含不同的frozenset的set。

集合可以做交集并集运算。
```python
found = len(set1 & set2)
```
#### 散列表的工作原理
dict与set的背后。

散列表算法：

为了获取`my_dict[search_key]`背后的值，python首先会调用`hash(search_key)`来计算search_key的散列值，把这几个值最低的几位数字当作偏移量，在散列表中查找表元（具体会根据散列表的大小有所区别）。若是被找到表元是空的，则会抛出KeyError异常。
##### 执行效率。

##### 为什么dict与set是无序的？

##### 为什么并不是所有的python对象都可以当作dict的键或者set里的元素？

##### 为什么dict的键与set元素的顺序是根据他们被添加的次序而定的，以及为什么要在映射对象的生命周期中，这个顺序并不是一程不变的？

##### 为什么不应该在迭代循环dict或是set的同时往其中添加元素？


#### 散列表的潜在影响

### 
