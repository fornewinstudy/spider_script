import scrapy
import random


class YanyshiSpider(scrapy.Spider):
    name = 'yanyshi'
    allowed_domains = ['www.httpbin.org']
    start_urls = ['https://www.httpbin.org/get']

    cookies = {"name":'mark'}

    data = {'class':"16"}

    def start_requests(self):
        # headers = [
        # {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4951.54 Safari/537.36"},
        # { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"},
        # { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4951.54 Safari/537.36"}
        # ]
        #
        # yield scrapy.Request(self.start_urls[0],headers=random.choice(headers),cookies=self.cookies,meta={'age':18},cb_kwargs={'num':1})

        yield scrapy.http.FormRequest(self.start_urls[0],callback=self.parse,formdata=self.data,meta={'age':18},cb_kwargs={'num':1})
        # yield scrapy.http.JsonRequest(self.start_urls[0], callback=self.parse, data=self.data, meta={'age': 18},cb_kwargs={'num': 1})

    def parse(self, response,num):
        print(num)
        print(response.meta.get('age'))
        print(response.text)
        print('*'*50)
        print(response.url)
        print(response.status)
        print(response.body)
        print(response.ip_address)  # 服务器ip地址
