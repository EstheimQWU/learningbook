# Redis
## what is redis
Redis是一个高性能的KEY-VALUE数据库。
+ 支持数据持久化，可以将内存中的数据保存在磁盘中，重新启动时可以加载使用。
+ 提供除了KEY-VALUE类型之外的数据结构，例如LIST, SET, ZSET, HASH等等。
+ 支持出局的备份，即MASTER-SLAVE模式的数据备份。

**Redis 优势**
- 性能高、读110,000次/s，写的速度是8,1000次/s。
- 丰富的数据类型
- 原子性（事务性）
- 丰富的特性——Redis支持public/subscribe，通知，key过期等特性。

**Redis与其他key-valus存储有什么不同？**
> + Redis有着更为复杂的数据结构并且提供对他们的原子性操作，这是一个不同于其他数据库的进化路径。Redis的数据类型都是基于基本数据结构的同时对程序员透明，无需进行额外的抽象。
> + Redis运行在内存中但是可以持久化到磁盘，所以在对不同数据集进行高速读写时需要权衡内存，因为数据量不能大于硬件内存。在内存数据库方面的另一个优点是，相比在磁盘上相同的复杂的数据结构，在内存中操作起来非常简单，这样Redis可以做很多内部复杂性很强的事情。同时，在磁盘格式方面他们是紧凑的以追加的方式产生的，因为他们并不需要进行随机访问。

## 安装与配置
Redis的配置文件是安装目录下的**redis.conf**。

1、Redis Config 命令格式

`redis 127.0.0.1:6379 > CONFIG GET` **CONFIG_SETTING_NAME**

`redis 127.0.0.1:6379 > CONFIG GET` **CONFIG_SETTING_NAME** **CONFIG_SETTING_NAME**

## Redis数据类型
https://redis.io/commands
### string
string是基础数据类型，其值最大能存储512MB，能够存储jpg图片或者序列化的对象。
```
redis 127.0.0.1：6379 > SET key value
redis 127.0.0.1：6379 > GET key
```
### hash
Redis hash 是一个键值(key=>value)对集合。

Redis hash 是一个 string 类型的 field 和 value 的映射表，hash 特别适合用于存储对象。
```
HMSET key field1 value1 [field2 value2 ]
HGET key field
```

### list
Redis 列表是简单的字符串列表，按照插入顺序排序。你可以添加一个元素到列表的头部（左边）或者尾部（右边）。
```
LPUSH key value1 [value2]
BLPOP key1 [key2 ] timeout
BRPOP key1 [key2 ] timeout
```
### set
Redis 的 Set 是 string 类型的无序集合。

集合是通过哈希表实现的，所以添加，删除，查找的复杂度都是 O(1)。
```
SADD key member1 [member2]
SMEMBERS key
```

### zset(sorted set)
> Redis zset 和 set 一样也是string类型元素的集合,且不允许重复的成员。不同的是每个元素都会关联一个double类型的分数。redis正是通过分数来为集合中的成员进行从小到大的排序。
```
ZADD key score1 member1 [score2 member2]
ZREVRANGE key start stop [WITHSCORES]
ZREVRANGEBYSCORE key max min [WITHSCORES]
```

## Redis事务

Redis 事务特征：

+ 批量操作在发送 EXEC 命令前被放入队列缓存。
+ 收到 EXEC 命令后进入事务执行，事务中任意命令执行失败，其余的命令依然被执行。
+ 在事务执行过程，其他客户端提交的命令请求不会插入到事务执行命令序列中。
```
开始事务->命令入队->执行事务
```
| 操作 | 功能 |
| ---- | ---- |
| DISCARD | 取消事务，放弃执行事务块内的所有命令。|
| EXEC | 执行所有事务块内的命令。|
| MULTI | 标记一个事务块的开始。|
| UNWATCH | 取消 | 
| WATCH | 命令对所有 key 的监视。|
| WATCH key [key ...] | 监视一个(或多个) key ，如果在事务执行之前这个(或这些) key 被其他命令所改动，那么事务将被打断。|

## 其他
### Redis脚本
### Redis连接
### Redis服务器