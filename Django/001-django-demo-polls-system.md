> The include() function allows referencing other URLconfs. Whenever Django encounters include(), it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing.

## 配置数据库
使用`pip install mysqlclient`命令安装数据库

## 修改数据库
Migrations are very powerful and let you change your models over time, as you develop your project, without the need to delete your database or tables and make new ones - it specializes in upgrading your database live, without losing data. We’ll cover them in more depth in a later part of the tutorial, but for now, remember the three-step guide to making model changes:

1. Change your models (in models.py).
2. Run `python manage.py makemigrations` to create migrations for those changes
3. Run `python manage.py migrate` to apply those changes to the database.

## 模型
1. 新建表单
```python
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
```

2. 配置表单
在`myapp.models`模块中配置
```python
INSTALLED_APPS = [
    #...
    'myapp',
    #...
]
```

3. 字段类型
模型中每一个字段都应该是某个 Field 类的实例， Django 利用这些字段类来实现以下功能：

字段类型用以指定数据库数据类型（如：INTEGER, VARCHAR, TEXT）。
在渲染表单字段时默认使用的 HTML 视图 (如： <input type="text">, <select>)。
基本的有效性验证功能，用于 Django 后台和自动生成的表单。

## 关联关系
### 多对一关联
定义一个多对一的关联关系，使用 django.db.models.ForeignKey 类。就和其它 Field 字段类型一样，只需要在你模型中添加一个值为该类的属性。

ForeignKey 类需要添加一个位置参数，即你想要关联的模型类名。
```python
from django.db import models

class Manufacturer(models.Model):
    # ...
    pass

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    # ...

```
> 你也可以创建 自关联关系 （一个模型与它本身有多对一的关系）和 与未定义的模型间的关联关系 ；

### 多对多关联
定义一个多对多的关联关系，使用 django.db.models.ManyToManyField 类。就和其他 Field 字段类型一样，只需要在你模型中添加一个值为该类的属性。

ManyToManyField 类需要添加一个位置参数，即你想要关联的模型类名。
```python
from django.db import models

class Topping(models.Model):
    # ...
    pass

class Pizza(models.Model):
    # ...
    toppings = models.ManyToManyField(Topping)
```

### 一对一关联
使用 OneToOneField 来定义一对一关系。就像使用其他类型的 Field 一样：在模型属性中包含它。

当一个对象以某种方式“继承”另一个对象时，这对该对象的主键非常有用。

OneToOneField 需要一个位置参数：与模型相关的类。

例如，当你要建立一个有关“位置”信息的数据库时，你可能会包含通常的地址，电话等字段。接着，如果你想接着建立一个关于关于餐厅的数据库，除了将位置数据库当中的字段复制到 Restaurant 模型，你也可以将一个指向 Place OneToOneField 放到 Restaurant 当中（因为餐厅“是一个”地点）；事实上，在处理这样的情况时最好使用 模型继承 ，它隐含的包括了一个一对一关系。

和 ForeignKey 一样，可以创建 自关联关系 也可以创建 与尚未定义的模型的关系 。
```python
from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return "%s the place" % self.name

class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant" % self.place.name

class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "%s the waiter at %s" % (self.name, self.restaurant)
```