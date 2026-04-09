from fontTools.ttLib import TTFont
from lxml import etree
import requests

# 加载字体文件
sz = TTFont('./szec.ttf')
# sz.saveXML('sz.xml')

replace_dict = {}
for k,v in sz.getBestCmap().items():
    key = hex(k)
    new_key = key.replace('0x', '&#x') + ';'
    value = int(v[-2:]) - 1
    # print(value)
    # 放入替换字典中
    replace_dict[new_key] = str(value)

url = 'http://shanzhi.spbeen.com/detail/?id=1988'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
    'Cookie': 'shanzhi_kmer=szua6wl5txyhcjnv8oa4oqdn8airk1l7; csrftoken=HwFjwGzcyRMMJrAJ94NIwBOsdqOdA2wGMtlYZcF2lCX2XNGYZ5fMiUqyF5lKcF1M'
}
res = requests.get(url, headers=headers)
html = res.text
for k,v in replace_dict.items():
    # 变量的作用域
    html = html.replace(k,v)
# print(html)
# 解析页面数据
html = etree.HTML(html)
conten_lst = html.xpath('//div[@class="jumbotron bg-white"]//text()')[1]
contena_lst = html.xpath('//div[@class="jumbotron bg-white"]//text()')[2]
contenb_lst = html.xpath('//div[@class="jumbotron bg-white"]//text()')[8]
# print(conten_lst)0
content_str = ''.join(conten_lst)
contenta_str = ''.join(contena_lst)
contentb_str = ''.join(contenb_lst)
# print(content_str)
cont = content_str.strip()
con = contenta_str.strip()
co = contentb_str.strip()
print(cont, con, co)

