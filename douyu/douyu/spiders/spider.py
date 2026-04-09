import scrapy
import json
from ..items import DouyuItem

class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['douyu.com']
    url = 'https://m.douyu.com/api/room/list?page={}&type=dance'
    page = 1
    start_urls = [url.format(page)]

    def parse(self, response):
        datas = json.loads(response.text)['data']['list']
        for dat in datas:
            item = DouyuItem()
            item['nickname'] = dat['nickname']
            item['verticalSrc'] = dat['verticalSrc']

            yield item

        self.page += 1

        yield scrapy.Request(self.url.format(self.page),callback=self.parse)


