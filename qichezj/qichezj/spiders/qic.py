import scrapy
from ..items import QichezjItem


class QicSpider(scrapy.Spider):
    name = 'qic'
    allowed_domains = ['autohome.com.cn']
    # start_urls = ['https://www.autohome.com/']
    # https://car.autohome.com.cn/photolist/series/65/p2/
    # https://car.autohome.com.cn/photolist/series/65/p3/
    # https://car.autohome.com.cn/photolist/series/54011/7190635.html#pvareaid=3454450

    base_url = 'https://car.autohome.com.cn/photolist/series/65/p{}/'
    page = 1
    start_urls = [base_url.format(page)]

    def parse(self, response):
        img = response.xpath('//div[@class="js-grid-main column grid-main"]//ul[@id="imgList"]/li')
        num = 1
        for res in img:
            qc = QichezjItem()
            # endswith以什么结尾
            lic = res.xpath('./a/img/@src').get()
            if lic.endswith('.gif'):
                qc['picture'] = 'https:' + res.xpath('./a/img/@src2').get()
            else:
                qc['picture'] = 'https:' + lic
            qc['name'] = str(num) + '_' + res.xpath('./a/img/@alt').get()
            num += 1
            yield qc

        self.page += 1
        # 指定回调函数callback=
        yield scrapy.Request(self.base_url.format(self.page), callback=self.parse)
