"""
目标网站https://www.sogou.com/
要求：
1. 用户输入要搜索的内容、起始页和终止页
2. 根据用户输入的内容爬取相关页面的源码
3. 把获取下来的数据保存到本地

"""
"""
https://www.sogou.com/web?query=python
https://www.sogou.com/web?query=python&page=2
https://www.sogou.com/web?query=python&page=3
"""
import requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
}
url = "http://www.daomubiji.com/"
response = requests.get(url,headers=headers)
with open("盗墓.html","w",encoding="utf-8") as a:
    a.write(response.content.decode("utf-8"))


# urllib模块自带的保存图片的方法是urlretrieve()


"""
选做题2)目标网站：https://fanyi.so.com/
要求：
1、让用户选择翻译成英语还是翻译成中文
2、根据用户输入的内容，实现翻译
3、把翻译出来的内容打印到控制台
"""
"""
中文翻译成英文
eng: 0
validate: 
ignore_trans: 0
query: 明天

英文翻译成中文
eng: 1
validate: 
ignore_trans: 0
query: Tomorrow

"""
# import requests
# ent = input("你要翻译成中文还是英文（中文:1 英文:0）：")
# query = input("输入你要翻译的内容：")
# headers = {
#     "pro": "fanyi",
#     "user-agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
# }
# data = {
#     "eng": ent,
#     "ignore_trans": 0,
#     "query": query,
# }
# url = "https://fanyi.so.com/index/search?"
# response = requests.post(url,headers=headers,data=data)
# print(response.json()["data"]["fanyi"])









