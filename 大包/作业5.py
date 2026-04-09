"""
7.(选做题1)目标网站：https://www.iyingku.cn/IMDB250
需求：
1、爬取页面所有电影名及评分
2、保持到cs
"""
# import requests
# import csv
# import re
# asd = []
# url_list = ["https://www.iyingku.cn/IMDB250"]
# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
# }
# for url in url_list:
#     response = requests.get(url, headers=headers)
#     html = response.content.decode("utf-8")
#     res = re.findall('<a href="(.*?)" title=(.*?) target="_blank"> (.*?) <span>(.*?)</span></a></td>.*?<td class="rl_grade_IMDB"><i class="iconfont">&#xe615;</i><span>(.*?)</span></td>.*?', html, re.S)
#     # print(res)
#     for i in res:
#         dst = {}
#         dst["电影名"] = i[2]
#         dst["评分"] = i[4]
#         asd.append(dst)
# with open("全球电影排行榜前250名.csv","w",encoding="utf-8",newline="") as a:
#     dat = csv.DictWriter(a,["电影名", "评分"])
#     dat.writeheader()
#     dat.writerows(asd)

# """
# 8.(选做题2)目标网站：https://www.9ku.com/music/t_new.htm
# 需求：
# 1、爬取到榜单页面使有的歌曲名、歌曲地址
# 2、保存到cs
# """
import requests
import re
import csv
asd = []
url = "https://www.9ku.com/music/t_new.htm"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}
response = requests.get(url, headers=headers)
html = response.content.decode("utf-8")
res = re.findall('<a target="_1" href="(.*?)" class="songName ">(.*?) </a>', html, re.S)
# print(res)
for data in res:
    dat = {}
    dat["url"] = data[0]
    dat["歌名"] = data[1]
    asd.append(dat)
with open("九酷音乐.csv","w",encoding="utf-8",newline="") as a:
    dat = csv.DictWriter(a,["url", "歌名"])
    dat.writeheader()
    dat.writerows(asd)

# """
# 7.(选做题1)目标网站：https://www.iyingku.cn/IMDB250
# 需求：
# 1、爬取页面所有电影名及评分
# 2、保持到cs
# """
import requests
import csv
from bs4 import BeautifulSoup
from lxml import etree
data_list = []
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}
url = f"https://www.iyingku.cn/IMDB250"
response = requests.get(url, headers=headers)
html = etree.HTML(response.content)
res = html.xpath("//tbody/tr")
for tr in res:
    itme = {}
    itme["电影名"] = tr.xpath('./td[@class="rl_name"]/a/text')[0]
    itme["链接"] = "https://www.iyingku.cn"+tr.xpath('./td[@class="rl_name"]/a/@href')[0]
    itme["评分"] = tr.xpath('./ta[@class="rl_grade_IMDB"]/span/text()')[0]
    data_list.append(itme)

with open("电影.csv", "w", encoding="utf-8", newline='') as a:
    dat = csv.DictWriter(a, ["电影名", "评分", "链接"])
    dat.writeheader()
    dat.writerows(data_list)

"""
8.(选做题2)目标网站：https://www.9ku.com/music/t_new.htm
需求：
1、爬取到榜单页面使有的歌曲名、歌曲地址
2、保存到cs
//div[@id="body"]/div/ol/li
"""
import requests
import csv
from lxml import etree
data_list = []
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}
url = "https://www.9ku.com/music/t_new.htm"
response = requests.get(url, headers=headers)
html = etree.HTML(response.content)
res = html.xpath('//div[@id="body"]/div/ol/li')
print(res)
# for li in res:
#     itme = {}
#     itme["歌曲名"] = li.xpath('./a/text()')[0]
#     itme["链接"] = "https://www.9ku.com" + li.xpath('./a/@href')[0]
#     data_list.append(itme)
#
# with open("音乐.csv", "w", encoding="utf-8", newline='') as a:
#     dat = csv.DictWriter(a, ["歌曲名", "链接"])
#     dat.writeheader()
#     dat.writerows(data_list)







