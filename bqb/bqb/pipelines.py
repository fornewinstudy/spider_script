# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy


class BqbPipeline(ImagesPipeline):
    # 专门用来下载图片
    def get_media_requests(self, item, info):
        image_url = item['picture']
        # 不需要指定回调方法，默认自带
        yield scrapy.Request(image_url)

    def file_path(self, request, response=None, info=None, *, item=None):
        image_guid = item['name']
        return f'{image_guid}.jpg'
