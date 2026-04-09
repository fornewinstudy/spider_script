# hash(哈希)
#  .hash用于存储对象 对象的结构为属性、值
#  .值的类型字符串
# 增加和修改
# 设置单个属性
#  . hset key field value
#  . 咧: hset use name mark
# 设置多个属性
#  . hmset key field value [field value ...]
#  . 咧: hmset use age 18 sex 'namex'
# 获取
# 获取指定的键所有属性
#  . hkeys key
#  . 咧:hkeys use
# 获取一个属性对应的值
#  . hget key field
#  . 咧:hget use name
# 获取多个属性对应的值
#  . hmget key field [field ...]
#  . 咧: hmget use name age sex
# 获取所有属性值
#  . hvals key
#  . 咧:hvals use
# 删除
# 删除整个hash键以及值 使用del
# 删除属性 属性对应的值会被一起删除
# . hdel key field [field ...]
# . 咧:hdel use sex


# set(集合)
#  .无序集合
#  .元素为string类型
#  .元素具有唯一性 不重复
# 增加
# 添加元素
#  . sadd key member [member ...]
#  . 咧:sadd u1 zs ls ww
# 获取
# 返回所有元素
#  . smembers key
#  . 咧:smembers u1
# 删除
# 删除del
# 删除指定元素
#  . srem key member [member ...]
#  . 咧:srem u1 ww
# 随机弹出
#  . count 个数
#  . spop key [count]
#  . 咧:spop u1 1
# 查询
# 判断集合里元素是否存在 1表示存在 0表示不存在
#  . sismember key member
#  . 咧:sismember u2 ww
# 移动(两个集合之间元素移动)
#  . smove source destination member
#  . 咧:smove u2 u1 ww  把u2中的ww移到u1里


# zset
#  .有序集合
#  .元素为string类型
#  .元素具有唯一性 不重复
#  .每个元素都会关联一个double类型的score,表示权重通过权重将元素从小到大排序
# 增加
# 添加
#  . zadd key [NX|XX] [CH] [INCR] score member [score member ...]
#   向键u3的集合里添加元素 权重 值
#  . 咧:zadd u3 4 zhangs 5 lishi 6 wangw 3 laoliu
# 获取
# 返回指定范围内的元素
#  . zrange key start stop [WITHSCORES]
#  . 咧:zrange u3 0 -1
# 返回score值在min和max之间的元素
#  . zrangebyscore key min max [WITHSCORES] [LIMIT offset count]
#  . 咧:zrangebyscore u3 3 5
# 返回某个成员的权重值
#  . zscore key member
#  . 咧:zscore u3 wangw
# 删除
# 输出del
# 删除指定元素
#  . zrem key member [member ...]
#  . 咧:zrem u3 wangw
# 删除权重值在指定范围内的元素
#  . zremrangebyscore key min max
#  . 咧:zremrangebyscore u3 3 5



# python与Redis交互
# 安装 pip install redis

import redis

# 创建StrictRedis对象  与redis服务链接
# sr = redis.StrictRedis()
# sr.set('u3', 'mark')

class StringRedis:
    def __init__(self):
        # 端口号 port - 默认端口号6379
        # 数据库 db - 默认数据库0
        # 解析响应内容 decode_responses - 默认为Fals - 如果想要把中文输入到库里这将False改为True
        self.con = redis.StrictRedis(port=6379, db=0, decode_responses=True)

    def string_set(self ,k ,v):
        # 写
        res = self.con.set(k,v)
        print(res)

    def string_get(self,k):
        # 读
        ras = self.con.get(k)
        print(ras)

if __name__ == '__main__':
    s = StringRedis()
    s.string_set('u4','马克')
    s.string_get('u4')

# 在Python中写入到redis的中文是无法在redis中显示的,要想显示则需要在redis输入中加入redis-cli --raw


#分布式
# 分布式爬虫
# 分布式爬虫是由一组通过网络进行通信、为了完成共同的爬虫任务而协调工作的计算机节点组成的系统。分布式爬虫是将多台计算机组合起来，共同完成一个任务，这将大大提高爬取效率
# 为啥需要分布式爬虫
# 不要把鸡蛋放到一个篮子里
# Scrapy—Redis
# 默认scrap框架不支持分布式,需要使用基于redis的Scrapy-Redis组件才能实现分布式功能
# 正常scrapy是单机爬虫
# Scrapy并不会共享调度队列,也就是说Scrapy是不支持分布式的.为了支持分布式,我们需要让Scrapy支持共享调度队列,也就是改造共享调度和去重的工能.
















