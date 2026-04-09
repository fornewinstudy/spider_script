import scrapy
from ..items import DaomuItem
# 深浅拷贝
from copy import deepcopy
import re
import os
from scrapy_redis.spiders import RedisSpider


class DmSpider(RedisSpider):
    name = 'dm'
    allowed_domains = ['daomubiji.com']
    # start_urls = ['http://www.daomubiji.com/']
    redis_key = 'daomuniji'

    # 解析一级页面
    def parse(self, response):
        a_list = response.xpath('//li[contains(@id, "menu-item-")]/a')
        for a in a_list:
            item = DaomuItem()
            # 获取大标题
            item['first_title'] = a.xpath('./text()').get()

            # 先对不能出现再文件名中的字符做替换 一般都是英文状态下的
            item['first_title'] = re.sub(r'[\\\/\:\*\?\<\>\| ]', "_", item['first_title'])

            # 获取到大标题之后 创建只文件夹
            # 生成文件路径
            dir_path = './novel/{}/'.format(item['first_title'])
            # 根据文件路径进行创建
            # 在创建之前需要进行判断
            if not os.path.exists(dir_path):
                # 如果有 就创建
                os.makedirs(dir_path)

            # 获取二级页面的链接
            second_title= a.xpath('./@href').get()

            # 二级页面的请求
            yield scrapy.Request(
                url=second_title,
                callback=self.parst_article,
                meta={'item':deepcopy(item)}
            )
    # 解析二级页面
    def parst_article(self, response):
        item = response.meta.get('item')

        a_list = response.xpath('//article/a')
        for a in a_list:
            # 获取小标题
            item['second_title'] = a.xpath('./text()').get()
            # 获取三级页面的链接
            third_url = a.xpath('./@href').get()

            # 构造三级页面的请求
            yield scrapy.Request(
                url=third_url,
                callback=self.parse_content,
                meta={'item':deepcopy(item)}
            )

    # 解析小说具体内容
    def parse_content(self, response):
        item = response.meta.get('item')
        content_lst = response.xpath('//article[@class="article-content"]/p/text()').getall()
        # 拼接列表内容成一个完整的字符串
        item['content'] = '\n'.join(content_lst)

        yield item





