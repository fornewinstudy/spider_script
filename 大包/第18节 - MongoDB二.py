# 查询数据
# find()  db.mark.find() 默认查询
# 精确查询
# db.mark.fiand({name:'mark'})
# 以格式化显示查询结果
# db.mark.fiand({name:'mark'}).pretty()
# 满足符合条件的第一个结果
# db.mark.findOne(name:'maek')
# 多条件查询
# db.mark.findOne(age:80,name:'mark')

# 条件＞18
# db.mark.find({age:{$gt:18}})
# 比较运算符
# 等于：默认是等于判断，没有运算符
# 小于：$lt
# 小于等于：$lte
# 大于：$gt
# 大于等于：$gte

# 查询y大于等于18的数据
# db.jerryn_collection.find({y:{$gte:18}})
# 范围运算符

# 使用$in,$nin判断是否在某个范围内查询年龄为18、28的学生
# db.jerry_collection.find({age:{$in:[18,28]}})

# 逻辑运算符
# or:使用$or，值为数组，数组中每个元素为json
# db.jerry_collection.find({$or:[{age:{$gt:18}},{gender:false}]})

# 自定义查询
# mongo shell 是一个js的执行环境
# 使用$where 写一个函数， 返回满足条件的数据
# 无法查询数值为字符串
# db.mark.find({age:{$gt:18}})
# 可以查询数值为字符串
# db.mark.find({$where:function(){return this.age>18}})

# 操作查询结果
# 查询集合里数据个数
# db.mark.find().count()
# db.mark.count()
# 查询符合条件的数据个数
# db.mark.find({age:18}).count()
# db.mark.count({age:18})
# 查询符合条件的前几条数据个数
# db.mark.find().limit(2) 注意括号里面的数据不分正负号
# # db.mark.find().limit(-2) 注意括号里面的数据不分正负号
# 跳过几条数据
# db.mark.find({age:{$gt:18}}).skip(2)
# 映射：返回该字段
# 如果为1 返回该字段
# 只显示你指定的数据和_id
# db.mark.find({},{age:1})
# 只显示你指定的数据不显示id
# db.mark.find({},{age:1,_id:0})

# 排序
# 按照年龄升序
# db.mark.find().sort(age:1)
# 按照年龄降序
# db.mark.find().sort(age:-1)

# 正则
# db.mark.find({name:{$regex:'\\w'}})

# 修改数据
# db.集合名.update()
# 1. query:查询条件
# 2.vcupdate:更新的内容
# 3.multi:默认为False 表示只更新一个符合条件的数据 为True 把满足条件的数据进行更新
# 正常更新 其余字段数据不保留
# db.mark.update({name:'mark'},{name:'马克'}) 这样会默认全部替换
# 指定字段更新 保留其余字段
# db.mark.update({name:'mark'},{$set:{name:'马克'}}) 这就只会替换需要替换的内容
# 把查询到的所有的地址为湖南的改为河南
# db.mark.update({addr:'湖南'},{$set:{addr:'河南'}},(multi:true))

# 删除数据
# 删除集合名称
# db.mark.drop()
# 删除集合下所有数据
# db.mark.remove({})
# 删除满足条件的数据
# db.mark.remove({age:18}) 默认全部删除
# db.mark.remove({age:18},{justOne:true}) 只删除第一个数据
# 下面两个效率比remove高
# db.maek.deleteOne({age:80}) 删除第一个
# db.maek.deleteOne({age:80}) 删除多个

# 索引
# 更快
# 插入数据
# for(i=0;i<100000;i++){db.test.insert({name:'test'+i,age:i})}
# 创建索引前
# db.test.find({name:'test9999'})
# db.test.find({name:'test9999'}).explain('executionStats') # 显示查询操作的详细信息
# 创建索引
# db.test.ensureIndex({name:1})
# 创建索引后
# db.test.find({name:'test9999'}).explain('executionStats')
# db.test.find({name:'test9999'}).explain('executionStats')
# 删除索引
# db.test.dropindex({name:1})
# 默认情况_id是集合的索引
# 查询集合索引db.集合名.getlndexes()


# python与MongDB交互
# 1、安装pip install pymongo
# 2、使用
import pymongo
# 创建链接  -> 有默认链接 —> 也可以更改(host='127.0.0.1') -> 端口(port=27017)普遍都是默认的
# mongo = pymongo.MongoClient(host='127.0.0.1',port=27017)
# 执行操作
# mongo['demo']['info'].insert({'name':"mark"})
# 用面向对象的方式来写
class Mongo():
    def __init__(self, name):
        self.mongo = pymongo.MongoClient(host='127.0.0.1',port=27017)
        self.db = self.mongo['demo'][name]

    # 定义添加方法
    # 添加一条数据
    def tjiao(self, data):
        # 在低版本下有insert()方法
        # 在高版本下是没有insert方法  只剩下insert_one()和insert_many()方法
        self.db.insert({data:1})
        print()

    # 定义添加方法
    # 添加多条数据
    def tjia(self, data):
        self.db.insert_many({data: 1})
        print()

    # 定义查询一条数据
    # 默认参数为query = None
    def get_one(self,query = None):
        if query is None:
            return self.db.find_one()
        else:
            return self.db.find_one(query)

    # 定义查多条数据
    def get_may(self, query = None):
        if query is None:
            return self.db.find()
        else:
            return self.db.find(query)

if __name__ == '__main__':
    md = Mongo('info')
    # 插入多条数据的时候一定要加中括号[]
    # md.tjia([{'name':"mark"},{'name':'马克'}])
    res = md.get_one()
    # print(res)
    for i in res:
        print(i)

