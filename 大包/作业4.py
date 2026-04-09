"""
(选做题2)目标网站：https://sc.chinaz.com/yinxiao/
需求：
1、翻页爬网页上的音乐名字，音乐链接
2、保存到csv问答题 0.0分
"""
import requests
import csv
from bs4 import BeautifulSoup
data_list = []
for i in range(10):
    url = f"https://sc.chinaz.com/yinxiao/index_{i+1}.html"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content.decode("utf-8"), 'lxml')
    res = soup.find('div', id="AudioList").find('div', class_="container").find_all("div", class_="audio-item")
    for i in res:
        dat = {}
        dat["音效名"] =list(i.find("div", class_="right-head").p.stripped_strings)[0]
        dat["音效"] = "https:"+i.audio.get("src")
        data_list.append(dat)
with open("站长素材.csv", "w", encoding="utf-8", newline='') as a:
    dat = csv.DictWriter(a, ["音效名", "音效"])
    dat.writeheader()
    dat.writerows(data_list)

"""
7.(选做题1)目标网站：https://sc.chinaz.com/tupian/
需求：
1、翻页爬网页上的图片名字，图片链接
2、保存到csv
https://sc.chinaz.com/tupian/index_2.html
"""
# requests 安alt+回车直接导入库
# import requests
# from bs4 import BeautifulSoup
# import csv
# data_list = []
# for i in range(10):
#     url = f'https://sc.chinaz.com/tupian/index_{i+1}.html'
#     if i == 0:
#         url = "https://sc.chinaz.com/tupian/"
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
#     }
#     response = requests.get(url, headers=headers)
#     soup = BeautifulSoup(response.content.decode("utf-8"), 'lxml')
#     res = soup.find('div', id="container").find_all('div', class_="box picblock col3")
#     # print(res)
#     # break
#     for i in res:
#         dat = {}
#         dat["url"] = "https:"+i.div.a.img.get("src2")
#         dat["图片名"] = i.div.a.get("alt")
#         data_list.append(dat)
# with open("图片素材.csv", "w", encoding="utf-8", newline='') as a:
#     dat = csv.DictWriter(a,["url", "图片名"])
#     dat.writeheader()
#     dat.writerows(data_list)









