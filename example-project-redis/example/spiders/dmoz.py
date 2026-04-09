from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
# 普通

class DmozSpider(CrawlSpider):
    """Follow categories and extract links."""
    name = 'dmoz'   # 爬虫文件的名字
    allowed_domains = ['dmoz-odp.org']  # 允许的爬取范围
    start_urls = ['http://www.dmoz-odp.org/']   # 起始的url

    rules = [
        Rule(LinkExtractor(
            restrict_css=('.top-cat', '.sub-cat', '.cat-item')
        ), callback='parse_directory', follow=True),
    ]

    def parse_directory(self, response):
        for div in response.css('.title-and-desc'):
            yield {
                'name': div.css('.site-title::text').extract_first(),
                'description': div.css('.site-descr::text').extract_first().strip(),
                'link': div.css('a::attr(href)').extract_first(),
            }
