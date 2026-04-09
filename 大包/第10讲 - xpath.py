# # xpath 所针对的标签是元素面板里面的源代码
# # /  从根节点选取
# # // 从匹配选择当前节点选择文档中的节点，而不考虑它们的位置
# # .  选择当前节点
# # .. 选择当前节点的父节点
# # @  选择属性   //head[@id="su"]
# # last()在xpath中提取最后一个
# # last()-1在xpath中提取倒数第二个
# # last()-2在xpath中提取倒数第三个
# # (position()<4)说明就代表你前面几个
#
#
# # xpath练习
# wb_data = """
#         <div>
#             <ul>
#                  <li class="item-0"><a href="link1.html">first item</a></li>
#                  <li class="item-1"><a href="link2.html">second item</a></li>
#                  <li class="item-inactive"><a href="link3.html">third item</a></li>
#                  <li class="item-1"><a href="link4.html">fourth item</a></li>
#                  <li class="item-0"><a href="link5.html">fifth item</a>
#              </ul>
#          </div>
# """
# from lxml import etree
# html = etree.HTML(wb_data)
# # print(html.xpath("/htnl"))
# # print(html.xpath("/div"))  # 如果没有提取到内容则返回一个空的列表
# # print(html.xpath("/div")[0]) # 如果没有提取到内容去加索引则报错
# # print(html.xpath("/html")) # 如果你使用xpath里面的lxml可以自动的去修改你的html的代码
# # s = html.xpath("/html")[0]
# # print(etree.tounicode(s))  # tounicode() 转成字符串
#
# # 提取文本text()
# # print(html.xpath("//li/a/text()"))
# #提取熟属性href
# print(html.xpath("//li/a/@href"))
# print(html.xpath("//li/a[@href]"))


# 豆瓣250案例
"""
//ol[@class="grid_view"]/li
"""
# import requests
# from lxml import etree
# import csv
# data_list = []
# for start in range(0,250,25):
#     url =f"https://movie.douban.com/top250?start={start}&filter="
#     # print(url)
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
#     }
#     response = requests.get(url, headers=headers)
#     html = etree.HTML(response.content.decode("utf-8"))
#     # html = etree.HTML(response.content)
#     # print(etree.tounicode(html))
#     # break
#     li_tag_list = html.xpath('//ol[@class="grid_view"]/li')
#     for li_take in li_tag_list:
#         itme = {}
#         itme["电影名"] = li_take.xpath('.//div[@class="hd"]/a/span[1]/text()')[0] # 只能写./ —>> 不能写//不然你当期提取的//ol[@class="grid_view"]/li就无效果
#         itme["演员"] = "".join([ i.strip() for i in li_take.xpath('.//div[@class="bd"]/p/text()')]).replace("\xa0",'')
#         itme["评分"] = li_take.xpath('.//div[@class="star"]/span[2]/text()')[0]
#         yp = li_take.xpath('.//div[@class="bd"]/p[@class="quote"]/span/text()')
#         if yp:
#             itme["影评"] = yp[0]
#         else:
#             itme["影评"] = "没有影评"
#         data_list.append(itme)
#         # print(itme)
#         # break
# with open("豆瓣250.csv","w",encoding="utf-8",newline="") as a:
#         wt = csv.DictWriter(a,["电影名", "演员", "评分", "影评"])
#         wt.writeheader()
#         wt.writerows(data_list)














