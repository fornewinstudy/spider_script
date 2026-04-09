import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['gitee.com']
    start_urls = ['https://gitee.com/login']

    def parse(self, response):
       print(response.text)
