import scrapy
import json
from ..items import BqbItem


class BiaoqbSpider(scrapy.Spider):
    name = 'biaoqb'
    allowed_domains = ['bbsnet.com']
    # start_urls = ['http://www.bbsnet.com/doutu']
    url = 'http://www.bbsnet.com/doutu/page/{}'
    page = 1
    start_urls = [url.format(page)]


    def parse(self, response):
        datas = response.xpath('//div/ul/li[@class="post box row fixed-hight"]')
        # print(datas)
        for data in datas:
            item = BqbItem()
            item['picture'] = data.xpath('./div[@class="thumbnail"]/a/img/@src').get()
            item['name'] = data.xpath('./div[@class="thumbnail"]/a/img/@alt').get()
            # print(item['name'])
            yield item

        self.page += 1
        # 指定回调函数callback=
        yield scrapy.Request(self.url.format(self.page), callback=self.parse)






