import requests
import csv
from lxml import etree
data_list = []
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}
url = "http://www.daomubiji.com/"
response = requests.get(url, headers=headers)
html = etree.HTML(response.content)
res = html.xpath("//article[@class='article-content']/a")
# print(res)
for tr in res:
    itme = {}
    itme["名字"] = tr.xpath('./div/h2/text()')
    data_list.append(itme)

with open("电影.csv", "w", encoding="utf-8", newline='') as a:
    dat = csv.DictWriter(a,["名字"])
    dat.writeheader()
    dat.writerows(data_list)