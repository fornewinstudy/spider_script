# MongoDB的特点
# 无数据结构 (方便爬虫)
# 高性能(具有非常高的读写能力)
# 良好的支持(完善文档、跨平台、稳定)

# 启动mongd   输入mongo
# show dbs 查看mongodb当前库有哪些 默认有三个库(admin   0.000GB、config  0.000GB、local   0.000GB)
# 链接mongodb

# cmder
# 放大字体或缩小字体: 按住Ctrl+鼠标滑轮滚动
# cd ..  退到上一级
# cmder 的基本命令
# cls 清屏
# use 数据库名 使用数据库/创建数据库(数据库里面必须要有数据才能创建成功)
# db 查看当前使用数据库的名字
# db.make.insert({x:1})  db 代表当前数据库 make 插入的数据库里的表 {x:1} 插入一行数据
# show collections/ shao tables 查询当前使用数据库下面集合(表)
# db.dropDatabase() 删除当前正在使用的数据库

# 插入数据
# insert()
# 1、不手动创建的表, (当前没有这个表的时候，插入一条数据，表自动创建)  db.mark.insert({x:1})
# 2、手动创建, ()  db.createCollection(name, option)表的名称一定要是字符串的形式，不然则报错
#    name: 创建的集合名称
#    option:是一个文档 指定集合的配置(capped, size, max)
#           capped:boolean类型 默认为False 没有设置上限 True设置上限
#           size:表示设置上限的大小 单位(字节)  如果设置大小<256  默认为256  db.createCollection('mark',{capped:true,size:10})
#           max: number  指定上限集合中允许的最大文档数量(最大行数)  db.createCollection('mark',{capped:true,size:5000,max:4})
#           db.表名.isCapped()  检查当前表有没有设置上限  有为true  没有为false
#           db.表名.drop() 删除集合(表)

# 插入多条数据
# db.mark.insert([{name:'mark'},{name:'amy'}])
# for(i=3;i<10;i++)db.mark.insert({x:i})

# 查询数据
# db.mark.find() 查询表里的数据

# save() 根据指定_id  找到就更新  没找到就插入
# db.mark.save({_id:***,name:'yueyue'})
























