import requests
from toojs import get_js


url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
    'Cookie': 'OUTFOX_SEARCH_USER_ID=-1930825379@10.110.96.160; OUTFOX_SEARCH_USER_ID_NCOO=1871344231.4810517; fanyi-ad-id=306808; fanyi-ad-closed=1; ___rl__test__cookies=1655689231723',
    'Referer': 'https://fanyi.youdao.com/'
}
res = '爬虫'
# get_js 通过Python来执行js代码的 我们能够拿到逆向相关的四个参数
data = get_js('./youdao.js', 'youdao', res)
# print(data)
"""
i: 翻译
from: AUTO
to: AUTO
smartresult: dict
client: fanyideskweb
salt: 16556892317270
sign: f1cb00365562f8eeebbc3cf58cb31b0f
lts: 1655689231727
bv: 033a93960493d95e53be570a0117ca34
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_REALTlME
"""
data["i"] = res
data["from"] = 'AUTO'
data["to"] = 'AUTO'
data["smartresult"] = 'dict'
data["client"] = 'fanyideskweb'
data["doctype"] = 'json'
data["version"] = '2.1'
data["keyfrom"] = 'fanyi.web'
data["action"] = 'FY_BY_REALTlME'

das = requests.post(url, headers=headers, data=data)
# 不同的数据类型 后续的处理方式会不太一样
print(das.text,type(das.text)) #字符串
print(das.json(),type(das.json())) #字典






