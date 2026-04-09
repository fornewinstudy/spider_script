# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QichezjItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 汽车名字
    name = scrapy.Field()
    # 汽车图片
    picture = scrapy.Field()
