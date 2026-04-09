import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
from ..items import XjItem


class XjgcSpider(CrawlSpider):
    name = 'xjgc'
    allowed_domains = ['xjie.edu.cn']
    start_urls = ['https://www.xjie.edu.cn/tzgg1.htm']

    # 规则
    # 定义提取url地址的地方
    # 一个元组，有顺序顺序
    # 可以定义多个规则
    # allow=''只能写正则
    rules = (
        # 提取详情页url
        Rule(LinkExtractor(allow=r'info/1061/\d+.htm'),callback='parse_itme',follow=False),
        # 提取列表页url   翻页
        # Rule(LinkExtractor(allow=r'tzgg1/\d+.htm'))
        Rule(LinkExtractor(allow=r'[44,45,46].htm'),follow=True)

    )

    """
    Rule类 是一个类  实例化这个类得到用于提取url的规则
    LinkExtractor  链接提取器  提取url地址
       allow   正则表达式
       callback  提取url地址对应网页源代码 交给这个参数指定方法处理
       follow   当前url对应的响应是否还需要经过rules提取（不会重复提取）
    """

    def parse_itme(self, response):
        # print(response.text)
        item = XjItem()
        item['title'] = response.xpath('.//div[@class="content-title"]/h3/text()').get()
        data = response.xpath('.//div[@class="content-title"]/i/text()').get()
        item['date'] = re.split(r'\u3000',data)[0]
        print(item)
