# MYSQL
## 安装
### 准备工作
```
rpm -qa | grep mysql
rpm -e mysql　　// 普通删除模式
rpm -e --nodeps mysql　　// 强力删除模式
```
由于centos方面不再使用

### Linux安装
#### rpm
```
# wget http://dev.mysql.com/get/mysql-community-release-el7-5.noarch.rpm
# rpm -ivh mysql-community-release-el7-5.noarch.rpm
# yum install mysql-community-server
```

#### tar.gz
```
# wget https://downloads.mysql.com/archives/get/p/23/file/mysql-5.7.24.tar.gz
```

#### 权限设置
```
chown mysql:mysql -R /var/lib/mysql
```
#### 初始化
```
mysqld --initialize
```

#### 启动
```
systemctl start mysqld
```

#### 查看运行状态
```
systemctl status mysqld
```

#### 创建密码
```
mysqladmin -uroot password "new_password";
```

#### 登录
```
mysql -h 主机名 -u 用户名 -p 密码
```

### MySql管理
#### 用户设置
##### 新增用户
```
```

### MySql语句
**INSERT**
```
INSERT INTO table_name ( field1, field2,...fieldN )
                       VALUES
                       ( value1, value2,...valueN );
```
**SELECT**
```
SELECT column_name,column_name
FROM table_name
[WHERE Clause]
[LIMIT N][ OFFSET M]
```
**WHERE**
```
SELECT field1, field2,...fieldN 
FROM table_name1, table_name2...
[WHERE condition1 [AND [OR]] condition2.....
```
**UPDATE**
```
UPDATE table_name 
SET field1=new-value1, field2=new-value2
[WHERE Clause]
```
**DELETE**
```
DELETE FROM table_name [WHERE Clause]
```
**LIKE**
```
SELECT field1, field2,...fieldN 
FROM table_name
WHERE field1 LIKE condition1 [AND [OR]] filed2 = 'somevalue'
```
**UNION**
```
SELECT expression1, expression2, ... expression_n
FROM tables
[WHERE conditions]
UNION [ALL | DISTINCT]
SELECT expression1, expression2, ... expression_n
FROM tables
[WHERE conditions];
```
**SORT**
```
SELECT field1, field2,...fieldN FROM table_name1, table_name2...
ORDER BY field1 [ASC [DESC][默认 ASC]], [field2...] [ASC [DESC][默认 ASC]]
```
**JION**
+ NNER JOIN（内连接,或等值连接）：获取两个表中字段匹配关系的记录。
+ LEFT JOIN（左连接）：获取左表所有记录，即使右表没有对应匹配的记录。
+ RIGHT JOIN（右连接）： 与 LEFT JOIN 相反，用于获取右表所有记录，即使左表没有对应匹配的记录。

TBC.

