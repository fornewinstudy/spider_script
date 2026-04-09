# 1、课前答疑
#   imagePipeline图片没有保存成功
#     解决方法
#       IMAGES_STORE
#       解析数据为空
#         网页源代码没有
#         解析语法不清楚
#        pillow安装 pip install pillow
#    关闭scrapy日志
#     在settings.py里设置LOG_ENABLED = False


# 2、下载器中间件
#   Downloader Middleware也就是下载器中间件，它是处于scrapy的引擎和下载器之间的处理模块。在引擎把调度器获取的reques请求发给下载器的过程中，以及下载器把reponse发送回引擎的过程中，reques和response都会经过下载器中间件的处理。
# 应用:
# 1、修改UA
# 2、处理重定向
# 3、设置代理
# 4、失败重试
# 5、设置cookies
# 。。。。。。




# 3、爬虫中间件































