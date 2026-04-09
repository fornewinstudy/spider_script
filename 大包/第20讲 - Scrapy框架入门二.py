# 1、案例练习:
# 目标网站:https://quotes.toscrape.com/
#        https://quotes.toscrape.com/page/2/
#     数据需求：
#       1.名言
#       2.名人
#       3.标签
# 分析网站：数据静态加载
# 1、创建项目：scrapy startproject my_scrapy # 项目名
# 2、创建Spider: cd my_scrapy —>> scrapy genspider scrapy www.baidu.com
# 3、创建item: item 是保存爬取数据的容器，定义爬取结果的数据
# 4、Spider:
# 定义出事请求
# 定义解析逻辑
# 5、保存数据
# 1.命令保存(支持文件；csv, json, ....):scrapy crawl scrapy -o demo.csv
# 2.pipelines.py:
# class MyScrapyPipeline:
#     def process_item(self, item, spider):
#         with open('demo.text', 'a', encoding='utf-8') as f:
#             f.write(item['text'] + '\n')
#         return item
# 6、翻页
#


# 运行项目:
# 1、命令启动：scrpay crawl scrapy # 爬虫名字
# 2、文件启动：
# 新建文件名 -> from  scrapy import cmdline
# cmdline.execute('scrapy crawl scrapy'.split())


# 拓展
"""
解析工具
1.正则表达式  效率高  语法难记
2.xpath   效率中等  语法中等
3.BS4(bs语法和css选择器) 效率低  语法简单
"""
from bs4 import BeautifulSoup
import parsel  # 第三方(正则, xpath, css)
html = """
<html><head><title>The Dormouse's story</title></head>

    <p class="title"><b>The Dormouse's story</b></p>
    
    <p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/lacie" class="sister1" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister2" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister3" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p >
"""

# 解析
sop = BeautifulSoup(html,'lxml')
# css
# 1、通过标签名查找
# print(sop.select('a'))
# 2、通过类名称查找  - class不用写直接用.代替
# print(sop.select('.sister1'))
# 3、通过ID查找    - ID用＃代替
# print(sop.select('#link1'))
# 4、通过组合来查找
# print(sop.select('p  #link1'))
# print(sop.select('p > #link1'))
# print(sop.select('p > .sister1'))
# 5、获取内容
# 标签里面的获取文本内容
# print(sop.select('title')[0].get_text())
# 获取超链接
# print(sop.select('a#link1')[0]['href'])

# parsel
# 解析
selector = parsel.Selector(html)
# print(selector.re())
# print(selector.xpath())
# print(selector.css())
# 1、通过标签名查找
# print(selector.css('a').get())
# print(selector.css('a').getall())
# 2、通过类名称查找  - class不用写直接用.代替
# print(selector.css('.sister1').get())
# 3、通过ID查找    - ID用＃代替
# print(selector.css('#link1').get())
# 4、通过组合来查找
# print(selector.css('p  #link1').get())
# print(selector.css('p > #link1').get())
# print(selector.css('p > .sister1').get())
# 5、获取内容
# 标签里面的获取文本内容
# print(selector.css('p  #link1::text').get())
# 获取超链接
# print(selector.css('p  #link1::attr(href)').get())
# 6、伪类选择器
# print(selector.css('a').getall()[1])
# 在这个伪类选择器中是从1开始response
# print(selector.css('a:nth-child(1)').get())







