# 贪婪模式和非贪恋
# 贪婪模式
# 正则表达式在重复匹配里面默认是一种贪贪婪模式(贪婪模式匹配最多个)
# 非贪婪模式
# 在重复匹配的后面加个?(非贪婪模式匹配最少个)

# 正则的基本使用
# import re
# # match ->> str
# s = " python and java"
# reslt = re.match("python",s)
# reslt = re.match("java",s)   # 报错
# print(reslt)       # None  ->> 如同 ^java
# print(reslt.group())
# print(type(reslt.group()))
# .group把对象里面的内容以字符串的形式提取出来
# match特性：从头开始匹配，如果开头没有则返回一个空值

# search —>> str
# s = "python and java and java"
# reslt = re.search("java",s)
# print(reslt.group())
# search特性：只会匹配成功一次

# findall ->> list
# s = "python and java and java"
# reslt = re.findall("java",s)
# print(reslt)
# print(type(reslt))
# findall特性：返回列表
#
# finditer
# s = "python and java and java"
# reslt = re.finditer("java",s)
# # print(reslt)
# # print(type(reslt))  # <class 'callable_iterator'> ->> 可迭代
# for i in reslt:
#     print(i.group())

# 正则表达式 ->> 替换
# sub
# s = "python and java and java"
# s2 = re.sub("java","php",s)
# print(s2)
# sub特性：默认全部替换，如果要替换几次则爱后面加上参数n

# 正则表达式 ->> 分割 ->> list
# s = "python and java and java"
# s2 = re.split("\s", s)
# print(s2)
# print(type(s2))
# split特性：将字符串分割，如果要分割几次则在后面加上参数n

# 预定义
# compile
# reslt = re.compile("python")
# print(reslt)
# print(type(reslt))
# s = "python and java and java"
# s2 = reslt.match(s)
# print(s2.group())

# re.S匹配模式 —>> 使 . 能够匹配\n
# s = "python and java and java\n"
# reslt = re.findall("java.",s,re.S)
# print(reslt)

# re.I匹配模式 —>> 是你的正则表达式不区分大小写
# s = "python JAVA and java and java\n"
# reslt = re.findall("java",s,re.I)
# print(reslt)

# 练习
# import re
# html = """
# <div class="panel panel-default">
#    <!-- Default panel contents -->
# <div class="panel-heading">本周热点</div>
# <div class="panel-body"></div>
# <!-- List group -->
# <ul class="list-group">
#   <li class="list-group-item">三门峡市陕州区一中餐厅管理工作...</li>
#   <li class="list-group-item">鹤壁七中多措并举助推"六城联创...</li>
#   <li class="list-group-item">沙溪中学开展"扫黑除恶"专项宣...</li>
#   <li class="list-group-item">中牟县晨阳路学校："点缀生活 ...</li>
#   <li class="list-group-item">上饶市第二保育院开展预防手足口...</li>
# </ul>
# """
# # relst = re.match('\n<div class="(panel panel-default)">',html,re.S)
# relst = re.match('.*?<ul class="list-group">(.*?)</ul>.*?',html,re.S)
# # () 相当于分组的作用,如果超过分组范围则报错
# s2 = relst.group(1)
# s3 = re.findall('<li class="list-group-item">(.*?)</li>',s2)
# # print(s3)
# for i in s3:
#     print(i)


# 酷我案例
# http://www.kuwo.cn/play_detail/167610995
"""
<a title="美人画卷(片段)" href="/play_detail/167610995" class="name" data-v-1344465b>美人画卷(片段)</a>
<a title="月老掉线(片段)" href="/play_detail/210951079" class="name" data-v-1344465b>月老掉线(片段)</a>
<a title="(.*?)" href="(.*?)" class="name" data-v-1344465b>.*?</a>
"""
# import requests
# import re
# import json
# dat = []
# url = "http://www.kuwo.cn/playlist_detail/3331622979"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
# }
# response = requests.get(url,headers=headers)
# html = response.content.decode("utf-8")
# result = re.findall('<a title="(.*?)" href="(.*?)" class="name" data-v-1344465b>.*?</a> ',html,re.S)
# # print(result)
# for i in result:
#     # 定义一个字典用来保存数据的
#     item = {}
#     # print(i)
#     item["name"] = i[0]
#     item["url"] = "http://www.kuwo.cn" + i[1]
#     # print(item)
#     dat.append(item)
#
# # print(dat)
# with open("kw.txt","w",encoding="utf-8") as a:
#     for d in dat:
#         a.write(json.dumps(d,ensure_ascii=False))

# import re
# s = r"你好\n,name"
# asd = re.match("你好\\\\n,name",s)
# print(asd.group())



