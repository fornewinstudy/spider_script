# 导入模块
# 方法一：import urllib.request
# 方法二：from urllib import request
# import urllib.request
# urllib.request.方法
# from urllib import request
# request.方法
# import urllib.request
# res=urllib.request.urlopen(" https://www.baidu.com/")
# # print(res)
# # print(type(res))
# # print(type(res.read()))
# # print(res.read().decode("utf-8"))
# print(res.getcode())
# print(res.geturl())
# print(res.read())

import urllib.request
url="https://www.baidu.com/"
asd={
"User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
}
res=urllib.request.urlopen(url)
print(res.read().decode("utf-8"))

# import urllib.request
# url="https://www.baidu.com/"
# asd={
# "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
# }
# # res=urllib.request.urlopen(url)
# # print(res.read().decode("utf-8"))
# res=urllib.request.Request(url,headers=asd)
# # print(type(res))
# abc=urllib.request.urlopen(res)
# print(abc.read().decode("utf-8"))



# import urllib.request
# url="https://www.baidu.com/"
# asd={
# "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
# }
# qwe= urllib.request.Request(url,headers=asd)
# res=urllib.request.urlopen(qwe)
# d=res.read()
# print(d.decode("utf-8"))
# # 保存数据
# # 方法一：
# a=open("baidu.html","w",encoding="utf-8")
# a.write(d.decode("utf-8"))
# a.close()
# # read(): 只能读取响应内容的一次数据
# # 方法二：
# with open("baidu1.html","w",encoding="utf-8") as a:
#     a.write(d.decode("utf-8"))


# import urllib.request
# # urllib自带的保存数据的方法
# urllib.request.urlretrieve("https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fnimg.ws.126.net%2F%3Furl%3Dhttp%3A%2F%2Fdingyue.ws.126.net%2F2021%2F0720%2F32825dbbp00qwj04x009gc000t800idm.png%26thumbnail%3D650x2147483647%26quality%3D80%26type%3Djpg&refer=http%3A%2F%2Fnimg.ws.126.net&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1652154454&t=b1d27a88f070665295f20c95e7c8c990","吴京.png")


# import urllib.request
# url="https://ss1.baidu.com/9vo3dSag_xI4khGko9WTAnF6hhy/imgad/pic/item/242dd42a2834349bf6920c8ec1ea15ce36d3be21.jpg"
# c=urllib.request.urlopen(url)
# with open("许嵩.png","wb") as a:
#      a.write(c.read())


"""
https://tieba.baidu.com/f?kw=python&ie=utf-8&pn=0
https://tieba.baidu.com/f?kw=python&ie=utf-8&pn=50
https://tieba.baidu.com/f?kw=python&ie=utf-8&pn=100
"""
# import urllib.request
# import urllib.parse
# word=input("用户输入要收索的内容：")
# word1=urllib.parse.quote(word)
# start=int(input("用户输入起始页："))
# end=int(input("用户输入结束页："))
# qqt={
# "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
# }
# for i in range(start, end+1):
#      url=f"https://tieba.baidu.com/f?kw={word1}&ie=utf-8&pn={(i-1)*50}"
     # print(url)
     # 构建请求头
     # url=urllib.parse.quote(url)
     # res=urllib.request.Request(url,headers=qqt)
     # 发送请求
     # asd=(urllib.request.urlopen(res))
     # with open(f"{word}的第{i}页.html", "w", encoding="utf-8") as a:
     #      a.write(asd.read().decode("utf-8"))


# import urllib.parse
# 方法一：
# kw={
# 'ie': 'utf-8',
# 'kw': '周杰伦',
# 'fr': 'search',
# }
# asd=urllib.parse.urlencode(kw)
# print(asd)

# 方法二：
# asd=urllib.parse.quote("周杰伦")
# print(asd)

# 将编码转为中文：
# print(urllib.parse.unquote("%E5%91%A8%E6%9D%B0%E4%BC%A6"))

# urllib自带的保存图片的方法urlretrieve()














