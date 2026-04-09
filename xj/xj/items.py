# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XjItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 公告标题
    title = scrapy.Field()
    # 时间
    date = scrapy.Field()
