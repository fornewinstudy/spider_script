# from bs4 import BeautifulSoup
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
# find() 方法
# 特性：只能提取到一个标签
# soup = BeautifulSoup(html_doc, "lxml")
# print(soup.find("a", attrs={"class":"sister"}))
# print(soup.find(["a", "p" ,"title"]))   # 通过列表可以写多个标签，如果有多个标签，find方法只能默认提取在前面的标签。
# print(soup.find(["a", "p"],attrs={"class":"sister"} ))
# print(soup.a)  # 这种只能提取第一个
# print(soup.find("a", id="link3"))
# print(soup.find(["a", "p"],attrs={"class":"sister", "id":"link2"}))
# print(soup.find(["a", "p"],attrs={"class":"sister", "id":"asd"})) # 如果没有提取到内容泽返回None
# print(soup.find("a", id="link3",class_="sister"))

# find_all()方法
# 特性:能提取多个标签
# print(soup.find_all("a")) # 提取多个标签，放在一个列里面
# print(soup.find_all("a", id="asxd"))  # 用find_all方法没有提取到内容，则返回一个[]
# print(soup.find_all(["a","p"],attrs={"class":"sister"}))
# print(soup.find_all(["a","p"],class_="sister"))

# select()方法
# .代表class
# print(soup.select(".sister"))
# #代表id
# print(soup.select("#link3"))
# 选择副标签
# print(soup.select("p>b"))

# 案例练习
html = """
<table class="tablelist" cellpadding="0" cellspacing="0">
    <tbody>
        <tr class="h">
            <td class="l" width="374">职位名称</td>
            <td>职位类别</td>
            <td>人数</td>
            <td>地点</td>
            <td>发布时间</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=33824&keywords=python&tid=87&lid=2218">22989-金融云区块链高级研发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-25</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a target="_blank" href="position_detail.php?id=29938&keywords=python&tid=87&lid=2218">22989-金融云高级后台开发</a></td>
            <td>技术类</td>
            <td>2</td>
            <td>深圳</td>
            <td>2017-11-25</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=31236&keywords=python&tid=87&lid=2218">SNG16-腾讯音乐运营开发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>2</td>
            <td>深圳</td>
            <td>2017-11-25</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a target="_blank" href="position_detail.php?id=31235&keywords=python&tid=87&lid=2218">SNG16-腾讯音乐业务运维工程师（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-25</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=34531&keywords=python&tid=87&lid=2218">TEG03-高级研发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a target="_blank" href="position_detail.php?id=34532&keywords=python&tid=87&lid=2218">TEG03-高级图像算法研发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=31648&keywords=python&tid=87&lid=2218">TEG11-高级AI开发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>4</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a target="_blank" href="position_detail.php?id=32218&keywords=python&tid=87&lid=2218">15851-后台开发工程师</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=32217&keywords=python&tid=87&lid=2218">15851-后台开发工程师</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a id="test" class="test" target='_blank' href="position_detail.php?id=34511&keywords=python&tid=87&lid=2218">SNG11-高级业务运维工程师（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
    </tbody>
</table>
"""
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, "lxml")
# 需求1、获取所有的tr标签
# print(soup.find_all("tr"))
# 需求2、获取第2个tr标签
# print(soup.find_all("tr")[1])
# 需求3、获取class属性等于even的tr标签,里面的职位名称
# for i in soup.find_all("tr",class_="even"):
    # print(i.find("td").find("a").string)
    # print(i.td.a.string)
# 只提取第一个
# print(soup.find("tr",class_="even").td.a.string)
# 提取第2个
# print(soup.find_all("tr",class_="even")[1].td.a.string)
# 需求4、提取所有的a标签，class为test，id为test
# print(soup.find_all("a", class_="test", id="test"))
# 需求5、提取所有的a标签里面的href属性
# for a in soup.find_all("a"):
    # print(a.get("href"))
    # print(a["href"])

# 天气预报案例
"""
找class="conMidtab"第2个div
找class="conMidtab2"的div
提取所有的tr标签
td标签就是我们要的数据了
"""
# import requests
# import csv
# from bs4 import BeautifulSoup
# data_list = []
# url_list = ["http://www.weather.com.cn/textFC/hb.shtml",
#            "http://www.weather.com.cn/textFC/db.shtml",
#             "http://www.weather.com.cn/textFC/hd.shtml",
#             "http://www.weather.com.cn/textFC/hz.shtml",
#             "http://www.weather.com.cn/textFC/hn.shtml",
#             "http://www.weather.com.cn/textFC/xb.shtml",
#             "http://www.weather.com.cn/textFC/xn.shtml"
#             ]
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
# }
# for url in url_list:
#     response = requests.get(url,headers=headers)
#     htmlse = response.content.decode("utf-8")
#     soup = BeautifulSoup(htmlse,"lxml")
#     div_tak = soup.find_all("div",class_="conMidtab")[1] # 这个索引是调整第几天的天数
#     # print(div_tak)
#     for div in div_tak.find_all("div", class_="conMidtab2"):
#         tr_tag_list = div.find_all("tr")[2:]
#         # print(tr_tag_list)
#         # break
#         for tr_tag in tr_tag_list:
#             itme = {}
#             td_list = tr_tag.find_all("td")
#             print(td_list)
    #         itme["城市"] = td_list[-8].a.string
    #         itme["天气"] = td_list[-7].string+"转"+td_list[-4].string
    #         # print(td_list[-7].string+"转"+td_list[-4].string)
    #         itme ["气温"]= td_list[-2].string+"到"+td_list[-5].string
    #         print(itme)
    #         data_list.append(itme)
    # with open("天气预报.csv","w",encoding="utf-8",newline="") as a:
    #     wt = csv.DictWriter(a,["城市", "天气", "气温" ])
    #     wt.writeheader()
    #     wt.writerows(data_list)

















