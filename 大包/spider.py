import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['douyu.com']
    start_urls = ['http://douyu.com/']

    def parse(self, response):
        pass
