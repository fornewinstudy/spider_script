# 爬虫第一次作业
import urllib.request
import urllib.parse

word = input("输入你要找的内容：")
start = int(input("用户输入起始页："))
end = int(input("用户输入结束页："))
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.0.3161 SLBChan/30"
}
for i in range(start, end + 1):
    url = f"https://www.1ppt.com/moban/ppt_moban_{i}.html"
    res = urllib.request.Request(url, headers=headers)   # 实例化请求对象
    asd = (urllib.request.urlopen(res))              # 发送请求的方法
    with open(f"第{i}页.html", "w", encoding="gb2312") as a:
        a.write(asd.read().decode("gb2312"))
# import urllib.request
# import urllib.parse
# name=input("用户输入要查找的内容：")
# name1=urllib.parse.quote(name)
# qsy=int(input("输入起始页："))
# jsy=int(input("输入结束页："))
# qqt={
# "user-agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
# }
# for i in range(qsy, jsy+1):
#     url=f"https://search.bilibili.com/all?vt=55311890&keyword={name1}&from_source=webtop_search&spm_id_from=666.4&page=2&o={i}"
#     res=urllib.request.Request(url, headers=qqt)
#     asd=(urllib.request.urlopen(res))
#     with open(f"{name}的第{i}页.html", "w", encoding="utf-8") as a:
#         a.write(asd.read().decode("utf-8"))
# import urllib.request
# import urllib.parse
# url="https://img1.baidu.com/it/u=419005938,2732634053&fm=253&fmt=auto&app=138&f=JPEG?w=707&h=500"
# asd=urllib.request.urlopen(url)
# with open(f"python.png", "wb") as a:
#     a.write(asd.read())
# import urllib.request
# url = "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fi1.go2yd.com%2Fimage.php%3Furl%3D0Tfn9czQYj&refer=http%3A%2F%2Fi1.go2yd.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1652250976&t=8d59073c2be93a42a87815b9aafe5d61"
# asd = urllib.request.urlopen(url)
# with open("喜羊羊与灰太狼.png", "wb") as a:
#     a.write(asd.read())


# import urllib.request
# import urllib.parse
# name=input("请输入你要收索的内容：")
# name1=urllib.parse.quote(name)
# qsy=int(input("起始页："))
# jsy=int(input("结束页："))
# headers={
# "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
# }
# for i in range(qsy, jsy+1):
#     url=f"https://tieba.baidu.com/f?kw={name1}&ie=utf-8&pn={(i-1)*50}"
#     asd=urllib.request.Request(url, headers=headers)
#     res=urllib.request.urlopen(asd)
#     with open(f"{name}的第{i}页.html", "w", encoding="utf-8") as a:
#         a.write(res.read().decode("utf-8"))


# """
# 目标网站:https://www.1ppt.com/moban/
# 爬取要求:1，翻页爬取这个网页上面的源代码
# 2，并且保存到本地
# https://js.1ppt.com/logo.gif
# https://www.1ppt.com/moban/ppt_moban_2.html
# """
# import requests
# name=input("输入要收索的内容：")
# age=int(input("输入起始页："))
# aed=int(input("输入结束页："))
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
# }
# for i in range(age,aed+1):
#     url=f"https://www.1ppt.com/moban/ppt_moban_{i}.html"
#     # print(url)
#     response = requests.get(url,headers=headers)
#     with open(f""*"*50{name}的第{i}页.html","w",encoding="gb2312") as a:
#         a.write(response.content.decode("gb2312"))










