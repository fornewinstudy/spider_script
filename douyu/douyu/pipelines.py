# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy
import os
from .settings import IMAGES_STORE


class DouyuPipeline(ImagesPipeline):
    # 专门用来下载图片
    def get_media_requests(self, item, info):
        image_url = item['verticalSrc']
        # 不需要指定回调方法，默认自带
        yield scrapy.Request(image_url)

    # 使用这种方法不会创建一个full的文件夹
    # 方法二：
    def file_path(self, request, response=None, info=None, *, item=None):
        image_guid = item['nickname']
        return f'{image_guid}.jpg'

    # # 下载完毕执行
    # 方法一：
    # def item_completed(self, results, item, info):
    #     # 方法一： 直接指定路劲
    #     # path = 'D:/zgqpycharm/爬虫基础代码/douyu/image'
    #     # 方法二：调用
    #     path = IMAGES_STORE
    #     # results 默认保存的路劲
    #     # path(results)
    #     img_url = results[0][1]['path']
    #     os.rename(path + '/' + img_url, path + '/' + item['nickname'] + '.jpg')

