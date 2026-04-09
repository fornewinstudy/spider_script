import scrapy
from ..items import TencentItem


class TxzahopSpider(scrapy.Spider):
    name = 'txzahop'
    allowed_domains = ['tencent.com']
    one_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1653804847510&countryId=&cityId=&bgIds=&productId=&categoryId=40001001,40001002,40001003,40001004,40001005,40001006&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
    two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1653805210719&postId={}&language=zh-cn'
    start_urls = [one_url.format(1)]

    def parse(self, response):
       data = response.json()
       # 解析出得到json数据
       for job in data['Data']['Posts']:
           item = TencentItem()
           # id
           post_id = job["PostId"]
           item['job_name'] = job['RecruitPostName']

           # 构造详情页的url
           detail_url = self.two_url.format(post_id)
           # 构造请求
           yield scrapy.Request(detail_url,callback=self.parse_datail,meta={'item':item})

        # 翻页
       for page in range(2, 11):
           url = self.one_url.format(page)
           yield scrapy.Request(url, callback=self.parse)

    def parse_datail(self,response):
        # 解析详情页面
        item = response.meta.get('item')
        data = response.json()
        item['job_duty'] = data['Data']['Requirement']
        yield item

