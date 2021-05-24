python基础练习题
1、为什么学习Python？
2、通过什么途径学习的Python？
3、Python和Java、PHP、C、C#、C++等其他语言的对比？
4、简述解释型和编译型编程语言？
5、Python解释器种类以及特点？
6、位和字节的关系？
7、b、B、KB、MB、GB 的关系？
8、请至少列举5个 PEP8 规范
9、python递归的最大层数？
10、求结果：
v1 = 1 or 3 
v2 = 1 and 3
v3 = 0 and 2 and 1
v4 = 0 and 2 or 1
v5 = 0 and 2 or 1 or 4
v6 = 0 or Flase and 1
11、ascii、unicode、utf-8、gbk 区别？
12、字节码和机器码的区别？
13、三元运算规则以及应用场景？
14、列举 Python2和Python3的区别？
15、用一行代码实现数值交换：
    a = 1
    b = 2
16、Python3和Python2中 int 和 long的区别？
17、xrange和range的区别？
18、文件操作时：xreadlines和readlines的区别？
19、列举布尔值为False的常见值？
20、字符串、列表、元组、字典每个常用的5个方法？
21、lambda表达式格式以及应用场景？
22、pass的作用？
23、arg和*kwarg作用？
24、is和==的区别？
25、简述Python的深浅拷贝以及应用场景？ 
26、Python垃圾回收机制？
27、python的可变类型和不可变类型？
28、求结果：
   v = dict.fromkeys(['k1','k2'],[])
   v['k1'].append(666)
   print(v)
   v['k1'] = 777
   print(v)
29、求结果：
    def num():
        return [lambda x: i*x for i in range(4)]
    print([m(2) for m in num()])
    
30、列举常见的内置函数？
31、filter、map、reduce的作用？
32、一行代码实现9*9乘法表。
33、如何安装第三方模块？以及用过哪些第三方模块？
34、至少列举8个常用模块都有那些？
35、re的match和search区别？
36、什么是正则的贪婪匹配？
37、求结果：
a. [ i % 2 for i in range(10) ] 
b. ( i % 2 for i in range(10) )
38、求结果：
a. 1 or 2 
b. 1 and 2 
c. 1 < (2==2) 
d. 1 < 2 == 2
39、def func(a,b=[]) 这种写法有什么坑？
def func(a,b=[]):
     b.append(a)
     print(b)
40、如何实现 "1,2,3" 变成 ['1','2','3'] ?



41、如何实现[‘1’,’2’,’3’]变成[1,2,3] ?
42、比较： a = [1,2,3] 和 b = [(1),(2),(3) ] 以及 b = [(1,),(2,),(3,) ] 的区别？
43、如何用一行代码生成[1,4,9,16,25,36,49,64,81,100] ?
44、一行代码实现删除列表中重复的值 ?
45、如何在函数中设置一个全局变量 ?
46、logging模块的作用？以及应用场景？
47、常用字符串格式化哪几种？
48、简述 生成器、迭代器、可迭代对象 以及应用场景？
49、用Python实现一个二分查找的函数。
50、谈谈你对闭包的理解？
51、os和sys模块的作用？
52、如何生成一个随机数？
53、如何使用python删除一个文件？
54、谈谈你对面向对象的理解？
55、Python面向对象中的继承有什么特点？
56、面向对象深度优先和广度优先是什么？
57、面向对象中super的作用？
58、是否使用过functools中的函数？其作用是什么？
59、列举面向对象中带双下划线的特殊方法，如：new、init
60、如何判断是函数还是方法？
61、静态方法和类方法区别？
62、列举面向对象中的特殊成员以及应用场景？
63、1、2、3、4、5 能组成多少个互不相同且无重复的三位数
64、用尽量多的方法实现单例模式。
65、装饰器的写法以及应用场景。
66、异常处理写法以及如何主动跑出异常（应用场景）
67、isinstance作用以及应用场景？
68、写代码并实现：
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
        Given nums = [2, 7, 11, 15], target = 9,
        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1]
69、json序列化时，可以处理的数据类型有哪些？如何定制支持datetime类型？
70、json序列化时，默认遇到中文会转换成unicode，如果想要保留中文怎么办？
71、什么是断言？应用场景？
72、使用代码实现查看列举目录下的所有文件。
73、简述 yield和yield from关键字。
74、代码实现六位随机验证码
75、代码实现随机发红包功能
76、请尽可能列举python列表的成员方法，并给出列表操作的答案：
（1） a=[1, 2, 3, 4, 5], a[::2]=？ a[-2:]=？
（2）一行代码实现对列表a中的偶数位置的元素进行加3后求和？
（3）将列表a的元素顺序打乱，再对a进行排序得到列表b，然后把a和b按元素顺序构造一个字典d。
       
77、Python是如何进行内存管理的？
78、介绍一下except的用法和作用？
79、如何用Python来进行查询和替换一个文本字符串？
80、有没有一个工具可以帮助查找python的bug和进行静态的代码分析？
