# """
# (选做题2)目标网站：https://top.baidu.com/board?tab=movie
# 需求：
# 1、爬取页面源代码
# 2、用正则解析数据，获取到整个榜单的电影名，电影类型和演员
# 3、把数据保存到csv问答题 0.0分
# """
# import requests
# import re
# import csv
# asd = []
# url = "https://top.baidu.com/board?tab=movie"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
# }
# response = requests.get(url,headers=headers)
# # with open("百度热收.html","w",encoding="utf-8") as a:
# #     a.write(response.content.decode("utf-8"))
# html = response.content.decode("utf-8")
# est = re.findall('.*?<div class="c-single-text-ellipsis">(.*?)</div>(.*?)</a> <!--s-frag--> <div class="intro_1l0wp">(.*?)</div><div class="intro_1l0wp">(.*?)</div>.*?',html,re.S)
# print(est)
# for i in est:
#     res = {}
#     res["影片"] = i[0]
#     res["类型"] = i[2]
#     res["演员"] = i[3]
#     asd.append(res)
# with open("百度热搜.csv","w",encoding="utf-8",newline="") as a:
#     dat = csv.DictWriter(a,["影片", "类型", "演员"])
#     dat.writeheader()
#     dat.writerows(asd)
#
# # """
# # (选做题1)目标网站：https://music.163.com/#/discover/toplist
# # 需求：
# # 1、爬取页面源代码
# # 2、用正则解析数据，获取到整个页面的歌名和歌手名
# # 3、把数据保存到csv问答题 0.0分
# # """
# import requests
# import re
# import csv
# import json
# dta_list = []
# url = "https://music.163.com/discover/toplist"
# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
# }
# response = requests.get(url, headers=headers)
# print(response)
# html = response.content.decode("utf-8")
# print(html)
# est = re.search('<textarea id="song-list-pre-data" style="display:none;">(.*?)</textarea>', html,re.S)
# print(est)
# res_json = est.group(1)
# res_json = json.loads(res_json)
# for data in res_json:
#     intes = {}
#     intes["歌曲"] = data["name"]
#     intes["歌手"] = ''.join([i["name"] for i in data['artists']])
#     print(intes)
#     dta_list.append(intes)
# with open("网易云音乐.csv","w",encoding="utf-8",newline="") as a:
#     dat = csv.DictWriter(a,["歌曲", "歌手"])
#     dat.writeheader()
#     dat.writerows(dta_list)










