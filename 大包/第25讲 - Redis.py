# Redis 数据库
# 概述：edis是一个高性能的，开源的，C语言开发的，键值对存储数据的No sql数据库。
#      NoSQL: not only sql，泛指非关系型数据库	Redis/MongoDB/Hbase Hadoop
#      关系型数据库: MySQL、oracle、SqlServer

# 为啥需要学习redis？
# 爬虫：数据存储
#   。文本: csv excel text json
#   。数据库: mongodb
#   。分布式爬虫
#   web：
#   。缓存

# redis特点
#   1.支持数据持久化、可将内存中的数据保存在磁盘上
#   2.string list set(无序集合) zset(有序集合) hash数据结构的存储
#   3.数据备份
#   4.速度快

# 应用场景
#   。用来做缓存
#   。大型系统中 实现特定功能：session共享 购物车


# redis安装
# 1、下载压缩包
# 2、解压到指定的盘符，咧如：***
# 3、配置环境变量 - cmd -redis-server
# 4、启动服务  redis-server.exe redis - redis-server.exe redis.windows.conf
# 5、链接客户端  redis-cli


# 数据操作
# .redis是k-v数据结构 每条数据都是键值对
# .键的类型是字符串
# .注意:键不能重复
# .值的类型:
#   。字符串string
#   。哈希hash
#   。列表list
#   。集合set
#   。有序集合zset


# string(字符串)
# .字符串类型的value 最多可容纳的数据长度512M
# 保存
# 设置键值: set key value
# 列如说设置一个键为name值为Mark的数据
# . set name mark
# 查看键: keys *
# 查看值: get name
# 返回字符串长度:strlen key
# 设置键值的过期时间
# setex key seconds value
# 设置key为a 过期时间为10秒 值为1
# setex a 10 1
# redis 默认提供了16个仓库  默认为第一个0这个仓库
# 切换仓库 select index
# 切换1仓库 select 1
# 设置多个键值对
#  .mset key value [key value ...]
#  .mset a1 1 a2 2 a3 3
# 追加值
#  .append key value
# 获取
#  .获取: 根据键获取值 如果不存在 则返回nil - get key
#  .获取: 根据多个键获取多个值 - mget key
# 查询
#  .查询键 参数支持正则表达式 - keys pattern
#  .查询所有的键 - keys *
#  .判断键是否存在 如果存在则返回1 不存在则返回0
#   .exists key
#  .查询键对应的值的类型 - type key
#  .查询有效时间 -1没有是时间限制 -2没有这key
#   .ttl key
# 删除
#  .删除键以及对应的值 返回1成功 0删除失败
#   .del key
#  .设置过期时间已存在键值对
#   . expire key seconds
# 其他命令
# .incr key:将key存储数字＋1
# .decr key:将key数字－1
# .incrby key increment:在key存储的值在加给定量
# .decrby key increment:在key存储的值在减给定量
# .getrange key start end:将键对应值进行截取
# .setrange key offset value:将值offset位置覆盖数据


#list(列表)
# .列表元素类型string
# .按照插入顺序排序
# 增加
# .在左侧插入数据 - lpush key value [value ...]
# .在右侧插入数据 - rpush key value [value ...]
# .在指定元素的前或者后插入新的数据
#  .linsert key BEFORE|AFTER pivot value
#  .前插入 - linsert a6 before 3 9
#  .后面插入 - linsert a6 after 3 8
# 获取
# .返回列表里指定范围的元素 -  lrange key start stop
# .返回所有范围的元素 - lrange a6 0 -1
# 修改
# .修改指定index的值
#  .lset key index value
# 删除
# .删除指定元素 -  lrem key count value
#  。count 个数
#  。count > 0 :从头到尾删除
#  。count < 0 :从尾到头删除
#  。count = 0 :移除所有














