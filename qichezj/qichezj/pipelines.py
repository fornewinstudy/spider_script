# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
from scrapy.pipelines.images import ImagesPipeline
from .settings import IMAGES_STORE
import scrapy
import random


class QichezjPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        image_url = item['picture']
        # 不需要指定回调方法，默认自带
        yield scrapy.Request(image_url)

    def file_path(self, request, response=None, info=None, *, item=None):
        image_guid = item['name']
        return f'{image_guid}.jpg'
