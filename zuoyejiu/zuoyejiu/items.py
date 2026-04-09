# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZuoyejiuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 房源标题（title）
    title = scrapy.Field()
    # 所在区域（region）
    region = scrapy.Field()
    # 所在街区（block）
    block = scrapy.Field()
    # 小区（community）
    community = scrapy.Field()
    # 房间面积（area）
    area = scrapy.Field()
    # 朝向（toward）
    toward = scrapy.Field()
    # 户型（type）
    type = scrapy.Field()
    # 租金（rent）
    rent = scrapy.Field()
    # 时间（time）
    time = scrapy.Field()
