# 1-Scrapy概述
# 1.为啥需要学习Scrapy
# 爬虫面试时必备技术
# 让我门的爬虫更快更强大
# 2.什么是Scrapy?
# 异步爬虫框架
#  Scrapy是基于python开发的爬虫框架，用于抓取网站并从其页面中提取(结构化数据)，也是当前Python爬虫生态中最流行的爬虫框架，Scrapy框架架构清晰，可扩展型强，可以灵活高效的完成各种爬虫需求。
# 3.如何学习Scrapy
# 官网:https://scrapy.org/
# 官方文档:https://docs.scrapy.org/en/latest/
# 4.Scrapy工作流程

# 快速入门
# 1.安装  pip install scrapy==2.5.1
# 安装之后在终端输入scrapy
# 2.创建项目
# scrapy startproject scrapy  项目名称(scrapy)
# 项目结构:
# my_scrapyresponse
#  my_scrapy
#   spiders
#     __init__.py
#   __init__.py
#   middlewares.py
#   pipelines.py
#   settings.py
#   item.py
#  scrapy.cfg

# 功能描述:
# scrapy.cfg:Scrapy项目的配置文件，其中定义项目的配置文件路径，部署信息等
# item.py:定义了itme数据结构 所有的itme的定义放在这里
# middlewares.py:定义了Spider Middlewares和Downloader Middlewares的实现(中间键)
# pipelines.py:定义了itme Pipeline的实现， 所有的itme Pipeline的实现都放在这里(数据保存)
# settings.py:定义了数据的全局配置
# spiders:里面包含一个个Spider的实现，每个Spider都对应一个python文件

# 创建Spider
#  打开cmder 切换的cd my_scrapy
#  scrapy genspider 文件名 www.baidu.com (域名)















