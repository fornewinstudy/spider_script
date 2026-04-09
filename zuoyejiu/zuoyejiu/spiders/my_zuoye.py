import scrapy
# 如果导入有红色波浪线，就写成..就可以了
from ..items import ZuoyejiuItem

# 方法一:
# class MyZuoyeSpider(scrapy.Spider):
#     name = 'my_zuoye'
#     allowed_domains = ['cs.zu.ke.com']
#     start_urls = ['https://cs.zu.ke.com']
#
#     def start_requests(self):
#         for i in range(1,11):
#             # 方法一
#             url = 'https://cs.zu.ke.com/zufang/pg{}/'.format(i)
#             yield scrapy.Request(url, callback=self.parse)
#
#
#     def parse(self, response):
#         res = response.xpath('//*[@id="content"]/div[1]/div[1]/div')
#         # print(res)
#         for i in res:
#             # print(i)
#             kf = ZuoyejiuItem()
#             kf['title'] = i.xpath('//p[1]/a[@class="twoline"]/text()').get().strip()
#             # print(title)
#             kf['region'] = i.xpath('//p[@class="content__list--item--des"]/a[1]/text()').get().strip()
#             kf['block'] = i.xpath('//p[@class="content__list--item--des"]/a[2]/text()').get().strip()
#             kf['community'] = i.xpath('.//p[@class="content__list--item--des"]/a[3]/text()').get().strip()
#             kf['area'] = i.xpath('//p[@class="content__list--item--des"]/text()[5]').get().strip()
#             kf['toward'] = i.xpath('//p[@class="content__list--item--des"]/text()[6]').get().strip()
#             kf['type'] = i.xpath('//p[@class="content__list--item--des"]/text()[7]').get().strip()
#             kf['rent'] = i.xpath("//span[@class = 'content__list--item-price']/em/text()").get().strip()
#             kf['time'] = i.xpath("//span[@class = 'content__list--item-price']/text()").get().strip()
# # # 分别是房源标题（title）、所在区域（region）、所在街区（block）、小区（community）、房间面积（area）、朝向（toward）、户型（type）、租金（rent）、时间（time）
#             yield kf
#         yield from response.follow_all(response.xpath('//url[@display:hidden]/li/a'), callback=self.parse)


# 方法二:
class MyZuoyeSpider(scrapy.Spider):
    name = 'my_zuoye'
    allowed_domains = ['cs.zu.ke.com']
    start_urls = ['https://cs.zu.ke.com']

    def start_requests(self):
        for page in range(1,11):
            url = 'https://cs.zu.ke.com/zufang/pg{}'.format(page)
            yield scrapy.Request(url,callback=self.parse)

    def parse(self, response):
        div_list = response.xpath('//div[@class="content__list--item--main"]')
        for div in div_list:
            itm = ZuoyejiuItem()
            itm['title'] = div.xpath('.//a/@title').get()
            # print(itm['title'])
            data = div.xpath('.//p[@class="content__list--item--des"]/a/text()').getall()
            # print(data)
            itm['region'] = data[0]
            itm['block'] = data[1]
            itm['community'] = data[2]
            data1 = div.xpath('.//p[@class="content__list--item--des"]/text()').getall()
            # print(data1)
            itm['area'] = data1[-4].strip()
            itm['toward'] = data1[-3].strip()
            itm['type'] = data1[-2].strip()
            itm['rent'] = div.xpath('./span[@class="content__list--item-price"]/em/text()').get()+"元/月"
            # print(itm['rent'])
            itm['time'] = div.xpath('./p[@class="content__list--item--brand oneline"]/span/text()').getall()[-1]

            yield itm

