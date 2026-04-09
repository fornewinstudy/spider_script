import scrapy


class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['example.com']
    start_url = 'http://httpbin.org/get'

    def start_requests(self):
        for i in range(5):
            url = f"{self.start_url}?query={i}"
            yield scrapy.Request(url,callback=self.parse)


    def parse(self, response):
        # print(response.status)
        print(response.text)



