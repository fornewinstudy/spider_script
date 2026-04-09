'''
(必做题1)将数据集1的数据通过python插入到MongoDB数据库中：
1、数据库名字为crawl_one;
2、集合名字为collection_one;
3、提交方式：
      将py文件命名为 16期爬虫-07-MongoDB作业-上课昵称(真实姓名).py
      再将py文件添加到邮箱附件中，邮件主题的命名格式为：16期爬虫-07-MongoDB作业-上课昵称(真实姓名)
'''

#方法一：
# import pymongo
# import csv
# # 读取csv里面的数据
# f = open('movie_world.csv', 'r', encoding='utf-8')
# cs = csv.DictReader(f)
# # 循环遍历出数据
# for c in cs:
#     # print(c)
#     py = pymongo.MongoClient('localhost',port=27017)
#     # 创建数据库
#     md = py['crawl_one']
#     # 插入数据
#     md.collection_one.insert_many([c])
#     # print(c)


# 方法二：
# import csv
# import pymongo
# mongo_cliend = pymongo.MongoClient()
# with open('movie_world.csv', 'r', encoding='utf-8') as f:
#     reade = csv.DictReader(f)
#     # print(reade)
#     for i in reade:
#         # print(i)
#         mongo_cliend['crawl_one']['collection_one'].insert_one(dict(i))



















