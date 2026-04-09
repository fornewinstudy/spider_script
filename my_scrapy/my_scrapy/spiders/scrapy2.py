import scrapy
from my_scrapy.items import MyScrapyItem


class ScrapySpider(scrapy.Spider):
    # 爬虫名称
    name = 'scrapy2'
    # 允许爬取的域名
    allowed_domains = ['quotes.toscrape.com']
    # 初始的请求

    start_urls = ['https://quotes.toscrape.com']


    def start_requests(self):
        for i in range(1, 6):
            # 方法一
            url = 'https://quotes.toscrape.com/page/{}/'.format(i)
            # 方法二
            # url = f'https://quotes.toscrape.com/page/{i}/'
            yield scrapy.Request(url, callback=self.parse)


    # 解析函数
    def parse(self, response):
        """
        解析返回响应，提取数据或者进一步生成要处理请求
        :param response:
        :return:
        """
        # print(response.text)
        res = response.xpath('//div[@class = "quote"]')
        # print(res)
        for re in res:
            # 旧方法
            # extract_first() 返回的一条数据
            # extract()  返回多条数据

            # 新方法
            # get() 返回的一条数据
            # getall() 返回多条数据
            item = MyScrapyItem()
            item['text'] = re.xpath('./span[@class = "text"]/text()').get()
            item['author'] = re.xpath('.//small[@class = "author"]/text()').get()
            item['tags'] = re.xpath('.//div[@class = "tags"]/a[@class = "tag"]/text()').getall()
            # print(text)
            # print(author)
            # print(tags)

            # 生成器
            yield item


















