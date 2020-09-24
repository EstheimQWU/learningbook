# 008-python-变量赋值与内存地址
python中复制对象有三种方法：
+ 赋值
+ 浅拷贝
+ 深拷贝

## 赋值
将a赋值给b
```python
a = [1, 2, 3, ['A', 'B', 'C']]
b = a
```
在上述的代码中，a是对象Obj的引用，b和a相同，也是指向这个Obj的引用，他们本质上指向同一片内存地址。

**赋值**不会开辟新的内存地址，它只是复制了对象的引用。除了b这个引用本身之外没有增加新的开支。

修改a会影响b，修改b会影响a。

## 浅拷贝
浅拷贝会创建一个新的对象，这个新对象和源对象不在同一片内存区域，但是如果其内部存在数据，他们内部存在的数据是相同的，处于同一片内存地址。
```python
L = [1, 2, 3, ['A', 'B', 'C']]
L_copy = L.copy()
```
其中L_copy与L的地址不相同，也不是同一个对象，然而他们中的`1, 2, 3, ['A', 'B', 'C']`却拥有同一片内存地址。

**重点**
如果我们修改了L中的元素，这时候要分三种情况。

第一个大类情况是修改外层元素：

第一种情况是修改`1, 2`这种不可变数据类型，那么修改的时候就相当于新建了元素，因此被修改的元素的内存地址改变了。

第二种情况是被修改是`['A', 'B', 'C']`这种可变变量本身，也就是以创建新列表的方式取代这里的列表，那么这就与第一种情况相同，属于修改外层元素，因此元素的内存地址改变了。

第二个大类是修改内层元素：

第一种情况是修改`['A', 'B', 'C']`中的`'A', 'B'`这些元素。这种情况下，这个列表的内存地址不会改变，而其中的不可变元素（原子元素）被修改时等同于重新创建，因此地址会改变，而修改可变元素（例如列表等）不会改变地址，情况与目前的情况相同。

哪一种情况是b改了，a不改的？每一种。

哪一种情况是a改了，b也改的？没有一种。

## 深拷贝
只有一种方法可以实现深拷贝，就是使用copy模块中的deepcopy函数，它可以拷贝目标对象的所有元素，包含内层元素。

## tips
1. 对于非容器类型，如数字，字符，以及其它“原子”类型，没有拷贝一说。产生的都是原对象的引用。

2. 如果元组变量值（不可变类型）包含原子类型对象，即使采用了深拷贝，也只能得到浅拷贝。

**example**
```python

if __name__ == '__main__':
    L_a = [1, 2, ',M', ['A', 'B', 'C']]  # 原型
    L_b = L_a  # 赋值
    L_copy = L_a.copy()  # 浅拷贝（copy）

    print('*************  init  **************')
    print('L: ', L_a, '    id of L_a ', id(L_a))
    print('L_b： ', L_b, '    id of L_b ', id(L_b))
    print('L_copy： ', L_copy, '    id of L_copy ', id(L_copy))

    print('*************  L_a.append(4)  **************')
    L_a.append(4)
    print('L: ', L_a, '    id of L_a ', id(L_a))
    print('L_b： ', L_b, '    id of L_b ', id(L_b))
    print('L_copy： ', L_copy, '    id of L_copy ', id(L_copy))

    print('*************  L_a[4] = ["X", "Y", "Z"]  **************')
    L_a[4] = ['X', 'Y', 'Z']
    print('L: ', L_a, '    id of L_a ', id(L_a))
    print('L_a[4]: ', L_a[4], '    id of L_a[4] ', id(L_a[4]))
    print('L_b： ', L_b, '    id of L_b ', id(L_b))
    print('L_b[4]: ', L_b[4], '    id of L_b[4] ', id(L_b[4]))
    print('L_copy： ', L_copy, '    id of L_copy ', id(L_copy))

    print('*************  L_a[4].append("M")  **************')
    L_a[4].append('M')
    print('L: ', L_a, '    id of L_a ', id(L_a))
    print('L_a[4]: ', L_a[4], '    id of L_a[4] ', id(L_a[4]))
    print('L_b： ', L_b, '    id of L_b ', id(L_b))
    print('L_b[4]: ', L_b[4], '    id of L_b[4] ', id(L_b[4]))
    print('L_copy： ', L_copy, '    id of L_copy ', id(L_copy))

    L2 = [-21, 22, 54, -3]
    print('before  ', L2, '    location: ', id(L2))
    sorted(L2, key=abs)
    print('before  ', sorted(L2, key=abs), '    location: ', id(sorted(L2, key=abs)))
    # 整了一个新的列表出来。

```