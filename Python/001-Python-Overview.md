# 001-Python-Overview
## 001python生态
### 001python虚拟机
CPython->使用C实现的Python；
PyPy->使用python语言实现的python；
Jypython->使用Java实现，并且运行在Java虚拟机上；
IronPython使用.Net CLR实现的Python。
通常、也是最标准得实现方式是CPtyhon，这也是其他虚拟的实现原型。

### 002Python的包（package）
#### 001python的包管理机制
python没有默认的包管理工具，同时包概念在python中也非常松散。
python代码依据模块（module）划分。一个模块，可以是只有一个函数的单文件，亦可以是包含一个或者多个子模块的文件夹。包与模块之间的区别非常小，每个模块同时也可以视作一个包。

#### 002python中查找模块的方法

> 与其他编程环境类似，Python中也有一些函数和类（比如str，len和Exception）是存在于全局作用域（global scope，在Python中被称为builtin scope）的，其他的函数和类则需要通过import语句进行引用。

只有存在于文件系统某处并且被标记在python虚拟机的记录中的地址才能够被import语句发现，一般在安装python虚拟机时会自动设置一部分这些地址，由于平台不同，这些地址也存在差异。

通过sys.path语句查看系统中的这些包路径。（这是一个包含路径信息的python列表）

python会从路径中一直往下检索，直到找到匹配的路径名。换而言之，如果有两个不同的文件夹包含了两个同名的包，那么包检索会返回其遇到的第一个绝对匹配地址，不会在继续检索下去。

因此可以通过修改包检索路径，做到特定的包被第一个发现。
`>>> sys.path.insert(0, '/mypackage')`

由于这个方法会造成默认路径的改变，因此请勿滥用这个方法，仅仅在必要时使用。

#### 003PythonPath环境变量
PYTHONPATH是一个可以用来增强默认包检索路径的环境变量。通过这个环境变量可以追加前文的包检索路径。

可以把它看作是一个PATH变量，但是一个只针对Python的变量。它只是一些包含有Python模块的文件路径列表（不是sys.path所返回的Python列表），每个路径之间以：分隔。设置方法很简单，如下：
```
export PYTHONPATH=/path/to/some/directory:/path/to/another/directory:/path/to/yet/another/directory
```

PYTHONPATH、sys.path.insert`和其他类似的方法，一般情况下最好不要使用。如果他们能够解决本地开发环境出现的问题可以使用，但是不应该存在生产环境中使用这些技巧。

> 包就是一个或多个模块/子模块的集合，一般都是以经过压缩的tarball文件形式传输，这个文件中包含了：1. 依赖情况（如果有的话）；2.将文件复制到标准的包检索路径的说明；3. 编译说明——如果文件中包含了必须要经过编译才能安装的代码。

#### 004第三方包
安装第三方包的三种办法：
+ 使用系统自带的包管理系统，例如deb、rpm等
+ 使用社区开发的pip、easy_install等工具
+ 通过源文件安装

```
这三种方法做的几乎是同一件事情，即安装依赖包，视情况编译代码，然后把包中模块复制到标准包检索路径。
```
**尝试找到不同操作系统下的三种包安装方法**

#### 005获取第三方包
+ 使用系统自带的包管理工具rpm
+ python包索引工具（pypi）
+ 代码托管平台（github、bitbucket）

1. pip安装
   可以轻松的管理包的版本与使用情况，是优先考虑的方法。
2. 源文件安装
   在无法
3. 安装需要编译的包
   当包内包含有C或者C++代码时，安装使用前需要事先编译。

### 003虚拟环境
1. virtualenv
2. pipenv
3. anaconda

### 004一些工具
1. pyflakes源码检查
2. Requests易用的http库
3. fabric
4. pipenv与virtualenvwrapper

