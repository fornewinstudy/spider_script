"""
https://tieba.baidu.com/f?kw=python&ie=utf-8&pn=0
https://tieba.baidu.com/f?kw=python&ie=utf-8&pn=50
https://tieba.baidu.com/f?kw=python&ie=utf-8&pn=100
"""
import urllib.request
import urllib.parse
import requests
word=input("用户输入要收索的内容：")
word1=urllib.parse.quote(word)
start=int(input("用户输入起始页："))
end=int(input("用户输入结束页："))
header={
"User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
}
for i in range(start, end+1):
     url=f"https://tieba.baidu.com/f?kw={word1}&ie=utf-8&pn={(i-1)*50}"
     print(url)
     # 构建请求头
     url=urllib.parse.quote(url)
     res=urllib.request.Request(url,headers=header)
     # 发送请求
     asd=(urllib.request.urlopen(res))
     with open(f"{word}的第{i}页.html", "w", encoding="utf-8") as a:
          a.write(asd.read().decode("utf-8"))

# 函数方法
# import urllib.request
# import urllib.parse
#
#
# # 输入内容的功能
# # 选择多个内容一起缩进-按住shift+tab 回到开头 ->> 缩进多个选择按住tab
# def name():
#     word = input("用户输入要收索的内容：")
#     start = int(input("用户输入起始页："))
#     end = int(input("用户输入结束页："))
#     return word,start,end
#
#
# # 发送请求的功能
# def get(url):
#     qqt = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
#     }
#     res = urllib.request.Request(url, headers=qqt)
#     # 发送请求
#     asd = (urllib.request.urlopen(res))
#     return asd
#
#
# # 保存数据的功能
# def save(word,i,asd):
#     with open(f"{word}的第{i}页.html", "w", encoding="utf-8") as a:
#         a.write(asd.read().decode("utf-8"))
#
#
# def res():
#     word,start,end=name()
#     for i in range(start, end + 1):
#         # 转成urlencode编码->>urllib.parse.quote(word)
#         url=f"https://tieba.baidu.com/f?kw={urllib.parse.quote(word)}&ie=utf-8&pn={(i-1)*50}"
#         # print(url)
#         # 调用发送请求的方法，把返回值保存到变量里面
#         asd=get(url)
#         # 调用保存数据
#         save(word,i,asd)
# res()

# 面向对象
# import urllib.request
# import urllib.parse
#
# class name(object):
#     def __init__(self):
#         self.qqt = {
#                 "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
#         }
#         # 同时给多个值修改 —>> 按住alt,选择多个值输入要增删的东西即可
#         self.word = input("用户输入要收索的内容：")
#         self.start = int(input("用户输入起始页："))
#         self.end = int(input("用户输入结束页："))
#
#     # 发送请求的一个方法
#     def get(self,url):
#         res = urllib.request.Request(url, headers=self.qqt)
#         # 发送请求
#         asd = (urllib.request.urlopen(res))
#         return asd
#
#     # 保存数据的方法
#     def abd(self,i,asd):
#         with open(f"{self.word}的第{i}页.html", "w", encoding="utf-8") as a:
#             a.write(asd.read().decode("utf-8"))
#
#     # 组函数
#     def res(self):
#         for i in range(self.start, self.end + 1):
#             # 转成urlencode编码->>urllib.parse.quote(word)
#             url=f"https://tieba.baidu.com/f?kw={urllib.parse.quote(self.word)}&ie=utf-8&pn={(i-1)*50}"
#             print(url)
#             # asd=self.get(url)
#             # self.abd(i,asd)
#
# tb=name()
# tb.res()


# __name__在本文件中打印输出的是 __main__
# __name__在其他文件中打印输出的是文件名和文件里的内容
# print("我已经被倒入了")
# print(__name__)

# json模块的使用
# json中加s是对内容的操作
# import json
# with open("fy.json", encoding="utf-8") as f:
#     s = f.read()
#     # print(type(s))
#     # 把json数据转成字典
#     s1=json.loads(s)
#     # print(type(s1))
#     # 把字典转成json数据
#     s2=json.dumps(s1)
#     print(type(s2))

# json中没有加s是对文件的操作
# import json
# with open("fy.json", encoding="utf-8") as f:
#     # 读取json文件，并且直接转成字典
#     # s1=json.load(f)
#     # print(type(s1))

# import json
# s='{"zly":"zly","message":"success","code":0,"uuid":"400676c8-0343-48e5-a6b7-b2f9223d5525","sugg":[{"k":"蚂蚁","v":"n.ant"},{"k":"蚂蚁上树","v":"vermicelli with spicy pork powder"},{"k":"蚂蚁啃骨头","v":"ants gnawing/nibbling at a bone—attack a big job bit by bit; plod/plug away at a big job bit by bit"},{"k":"蚂蚁搬泰山","v":"ants removing Mount Tai—the united efforts of the masses can accomplish mighty projects"}],"direction":"zh-CHS#en"}'
# with open("fy1.json","w", encoding="utf-8") as f:
#     # 可以直接写入json文件
#     json.dump(s,f)


"""
用代码实现翻译功能
1、分析
2、发送请求，拿到响应内容
3、对数据进行解析、提取
4、对数据进行保存
"""
import urllib.request
import urllib.parse
import json
text=input("请你输入要翻译的内容：")
url="https://fanyi.sogou.com/reventondc/suggV3"
headers= {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
}
dat={
    'from': 'auto',
    'to': 'en',
    'client': 'web',
    'text': text,
    'uuid': '400676c8-0343-48e5-a6b7-b2f9223d5525',
    'pid': 'sogou-dict-vr',
    'addSugg': 'on',
}
dat=urllib.parse.urlencode(dat)
dat=bytes(dat, encoding="utf-8")
rea=urllib.request.Request(url, headers=headers,data=dat)
res=urllib.request.urlopen(rea)
asd=res.read().decode()
# with open("fy.json","w",encoding="utf-8") as a:
#     a.write(res.read().decode())
rea=json.loads(asd)
print('你翻译的内容是：'+rea["sugg"][0]["v"])



# 安装模块
# win+r  输入cmd  输入 pip install requests
# 指定环境 where python
import requests





