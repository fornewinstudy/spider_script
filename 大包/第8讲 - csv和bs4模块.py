# csv的写入
# import csv  # 内置的模块
#
# intes = [{
#     "name":"张三",
#     "age":"18"
# },
# {
#     "name":"李四",
#     "age":"19"
# }
# ]
# # 如果不用csv，直接写
# # with open("demo2.csv","w",encoding="utf-8") as a:
# #     a.write("name,age")
# #     a.write("\n")
#
# # with open("demo3.csv","w",encoding="utf-8",newline="") as a:
# #     # 把文件对象传参进去，文件头
# #     res = csv.DictWriter(a,fieldnames=["name","age"],)
# #     res.writeheader()
# #     # 方法一
# #     # for i in intes:
# #     #     res.writerow(i)
# #     # 方法二
# #     res.writerows(intes)
#
#
# res = [
#     ["张三","19"],
#     ["李四","20"]
# ]
# with open("demo4.csv","w",encoding="utf-8",newline="") as a:
#     wd = csv.writer(a)
#     wd.writerow(["name","age"])
#     # 方法一
#     # for i in res:
#     #     wd.writerow(i)
#     # 方法二
#     wd.writerows(res)

# 酷我歌单保存到csv
# import requests
# import re
# import csv
# dat = []
# url = "http://www.kuwo.cn/playlist_detail/3331622979"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
# }
# response = requests.get(url,headers=headers)
# html = response.content.decode("utf-8")
# result = re.findall('<a title="(.*?)" href="(.*?)" class="name" data-v-1344465b>.*?</a> ',html,re.S)
# print(result)
# for i in result:
#     # 定义一个字典用来保存数据的
#     item = {}
#     # print(i)
#     item["name"] = i[0]
#     item["url"] = "http://www.kuwo.cn" + i[1]
#     # print(item)
#     dat.append(item)
# with open("酷我歌单.csv","w",encoding="utf-8",newline="") as a:
#     asd = csv.DictWriter(a,["name","url"])
#     # 写入表头
#     asd.writeheader()   # writeheader 写入头
#     asd.writerows(dat)


# bs4模块的基本使用
# 安装
# pip install bs4
# pip install BeautifulSoup4
# Beautiful Soup适用于Python 2.6及更高版本。如果使用lxml，效果会更好,和/或html5lib。

from bs4 import BeautifulSoup

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<b><!--同学们好坚持学习--></b>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
# 创建一个soup对象
# soup = BeautifulSoup(html_doc,'html.parser')
# soup = BeautifulSoup(html_doc,'lxml')
# print(soup.prettify())
# print(type(soup))  # <class 'bs4.BeautifulSoup'>
# print(soup.text)   # 把文本提取出来，但是文本内容不完整
# print(soup)        # 创建对象一个soup对象，直接打印会自动把标签补齐
# 提取head标签
# print(soup.head)   # 如果想要里面的标签，直接在soup.head即可
# 提取body标签
# print(soup.body)
# 提取title标签
# print(soup.title)
# 提取title标签内的文本
# print(soup.title.text)
# print(soup.title.string)
# 提取标签内的名字
# print(soup.title.name)
# 提取titlie副标签内的名字
# print(soup.title.parent.name)
# print(soup.a)

# 对象种类
# 如果要用lxml解析器的话
# pip install lxml

# 如果要用html5lib解析器的话
# pip install html5lib

# from bs4.element import NamespacedAttribute
# soup = BeautifulSoup(html_doc,'lxml')
# print(type(soup))          # <class 'bs4.BeautifulSoup'>
# print(type(soup.a))        # <class 'bs4.element.Tag'>
# print(type(soup.a.string)) # <class 'bs4.element.NavigableString'>
# print(type(soup.b.string)) # <class 'bs4.element.Comment'>


# 遍历文档数
# string  strings stripped_strings
# ● string获取标签里面的内容
# ● strings 返回是一个生成器对象用过来获取多个标签内容
# ● stripped_strings 和strings基本一致 但是它可以把多余的空格去掉
# print(soup.html.title.string)
# print(list(soup.html.strings))
# print(list(soup.html.stripped_strings))