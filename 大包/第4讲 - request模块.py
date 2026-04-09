# import requests
# url = "https://www.baidu.com/"
# 向服务器发起请求的方法
# response = requests.get(url)
# print(response)
# print(type(response))

# 响应对象里面的方法
# 把数据以文本的形式提取出来
# response.encoding= response.apparent_encoding
# print(response.text)        # 这样也不会有乱码
# print(response.text)      # 这样提取会有很多乱码
# print(type(response.text))  #  str类型
# response.encoding = "utf-8"
# print(response.text)   # 在前面指定它的编码类型 —>> 不会有乱码
# print(response.encoding) #解码

# 把数据以字节的方式提取出来
# print(type(response.content))
# print(type(response.content.decode("utf-8")))

# print(response.apparent_encoding)  # 能看到编码形式

# 解释
# a = "枫"
# a1 = a.encode("utf-8")
# print(a1)
# 如果类型是bytes(字节流)的形式 ->> 用decode进行解码
# print(type(a1))  # 类型子节流
# a2 = a1.decode("utf-8")  # 解码

# 查看状态码
# print(response.status_code)       # 查看状态码
# print(type(response.status_code)) # 类型是int

# 查看url
# print(response.url)

# 查看请求头
# print(response.request.headers)
# print(type(response.request.headers))

# 查看响应头
# print(response.headers)



# 携带请求头
# import requests
# url="https://www.baidu.com/?tn=88093251_94_hao_pg"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
}
# # print(type(headers))   # 类型是集合(set)
# response=requests.get(url,headers=headers)
# # response.encoding=response.apparent_encoding
# # print(response.text)
# # response.encoding="utf-8"
# # print(response.text)
# print(response.content.decode("utf-8"))


# 百度贴吧案例
"""
1、分析网站
2、发送请求
3、提取数据
4、保存数据
"""
"""
https://tieba.baidu.com/f?kw=python
https://tieba.baidu.com/f?kw=python&ie=utf-8&pn=50
https://tieba.baidu.com/f?kw=python&ie=utf-8&pn=100
"""
import requests
name=input("输入要收索的内容：")
age=int(input("输入起始页："))
aed=int(input("输入结束页："))
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
}
for i in range(age,aed+1):
    url=f"https://tieba.baidu.com/f?ie=utf-8&kw={name}&fr={(i-1)*50}"
    # print(url)
    response = requests.get(url=url,headers=headers)
    with open(f"{name}的第{i}页.html","w",encoding="utf-8") as a:
        a.write(response.content.decode("utf-8"))
    # 查看发送请求的url
    print("实际上发送请求的url：",response.url)


# 搜狗翻译
import requests
import json
url="https://fanyi.sogou.com/reventondc/suggV3"
name = input("输入要翻译的内容：")
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
}
# 全部替换 ->> ctrl+r
# (.*?): (.*?)$
# "$1": "$2",
date={
    "from": "auto",
    "to": "zh-CHS",
    "client": "web",
    "text": name,
    "uuid": "3c594c6e-ecea-4397-ad13-d31aaa447339",
    "pid": "sogou-dict-vr",
    "addSugg": "on",
}
# 发送post请求
res = requests.post(url,headers=header,data=date)
# res_json=json.loads(res.text)
# print(type(res.json()))    # 类型为字典
res_json=res.json()
print(res_json["sugg"][0]["v"])   # 类型字典

# ua的构建
# 方法一 ->> 直接copy
# headers={
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
# }
# 方法2 ->> 随机的构建ua
# import random
# liset=[
#     "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
#     'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36',
#     'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36',
# ]
# headers={
#     "User-Agent":random.choice(liset)
# }
# print(headers)

# 方法三 ->> 第一次执行会报错 ->> 后面就不会
# pip install fake-useragent
# from fake_useragent import FakeUserAgent
# headers={
#     "User-Agent": FakeUserAgent().random
# }
# print(headers)

# cookie的使用
# import requests
# url = "https://www.baidu.com/?tn=88093251_94_hao_pg"
# headers = {
#     # 吉林了用户的账号信息
#     "Cookie": "PSTM=1649657583; BAIDUID=78ACD91C4EE6108976223C1679AC4022:FG=1; BD_UPN=12314453; BIDUPSID=349439FB312BD88CB31CB55AEC98BA48; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDSFRCVID_BFESS=TzAOJeC62w1LJu7DoYpWU9Tnug5MDc7TH6aoDqNVgMYvuu5jIr_qEG0POx8g0Ku-Nb29ogKKQgOTHRCF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=tR4t_K0-fC03fP36q45H24k0-qrtetJyaR3nXqjvWJ5TMCo6Dfvk5j-vhnrjLhL8QIot0K5z3n8bShPC-tnUKfCZbPck-JQtJCQAQf7h3l02Vh79e-t2ynQDXxKHq4RMW23I0h7mWUoTsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJIjj6jK4JKjHLetj5P; ab_sr=1.0.1_ZjZmNmE3MmEyZjBiODk0ZjI4ODliODA5ZjVlNTY3ODg5NDMzNGM5OGU0ODg5ODYxNjQxYjQ3Nzc2NmZmNTllZGYzNDcxNjk1ZGIzMjk4MjZmYzY4ZTMxMzc3YjkzNzA1MThhMWUxYzc1ODZlNTYwM2NiMGI0NjNhMWNlNzEzYTBlYjZiOTU3NTJkNGMyZDE3M2M5NWZkODhkMWJkZjExNQ==; H_PS_645EC=9a2418hwlLcdG4aKSMo2WoBb9QNd6w3qyBsu9mvyIQeXSno%2BV4NG6HbGz%2FNkOGYZ%2F8bwxYOOJQ9i; BAIDUID_BFESS=455804108CC1348FC5F020E58A09DED0:FG=1; COOKIE_SESSION=118_0_9_9_5_9_0_0_9_6_10_0_126_0_15_0_1650007428_0_1650007413%7C9%23200415_46_1649931979%7C9; BDRCVFR[8Wh8D9l_neY]=mk3SLVN4HKm; BD_HOME=1; H_PS_PSSID=31254_26350; BA_HECTOR=a58504ag0h8l840guv1h5i85p0r",
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
# }
# response = requests.get(url,headers=headers)
# print(response.content.decode("utf-8"))





















