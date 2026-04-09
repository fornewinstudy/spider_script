"""
url：http://shanzhi.spbeen.com/login/
xml⽂件的5：<map code="0x9476"name="glyph00006"/>
⽹⻚源码中的5：&#x9476;
真实数据：5
{"&#x9476;": '5', 'xxx':.....}
1.找到字体⽂件
2.结合⽹⻚源码和字体⽂件挖掘替换关系
  从⽹⻚源码中找到乱码的呈现形式
  打开字体⽂件的⽅式 要么通过在线的要么通过本地软件 看到真实的数字
                 还需要将字体⽂件保存成xml格式 晓得通过python咱们能够取出哪⼀些属性
3.拿着替换关系去⽹⻚源码中进⾏替换
 -在替换之前需要确保⽹⻚源码获取到了
 -如果是⽤替换字典进⾏⼀对⼀对的替换要注意及时更新字符串(重新赋值)
"""

from fontTools.ttLib import TTFont
import requests

# 加载字体文件
sz = TTFont('./szec.ttf')
# sz.saveXML('sz.xml')

# 提取内容
# print(sz.getBestCmap())

# 目标替换字典
replace_dict = {}

for k,v in sz.getBestCmap().items():
    # 想办法把0x替换成&#x 并且加上; 等到这个k衔接的就是源码
    # 想办法取出glyph00010最后两位 减1 得到的v衔接的就是数据
    # replace_dict = {'源码':'数据'}
    # hex 处理成对应的十六进制
    # print(hex(k),v)
    key = hex(k)
    new_key = key.replace('0x', '&#x') + ';'
    # print(new_key)

    # 处理value
    value = int(v[-2:]) - 1
    # print(value)

    # 放入替换字典中
    replace_dict[new_key] = str(value)
# print(value)

# 获取网页源码
url = 'http://shanzhi.spbeen.com/index/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
}
res = requests.get(url, headers=headers)
# print(res.text)
# html为网页源码
html = res.text

# 用目标替换字典去网页源码中进行替换
# 每一轮只会替换一对 替换完一对之后 要及时更新html
for k,v in replace_dict.items():
    # 变量的作用域
    html = html.replace(k,v)
print(html)










