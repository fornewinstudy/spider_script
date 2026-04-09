"""
url = https://club.autohome.com.cn/bbs/thread/665330b6c7146767/80787515-1.html
1.找字体⽂件
  先找到有乱码的标签然后选中这个出现乱码的标签去右边的styles⾥⾯找font-family(需要进⾏简单的测试)
2.结合源码和字体⽂件挖掘映射关系
  如果浏览器⾥⾯不能够直观的看到替换⽬标(乱码的呈现形式)
  ⼀般我们会把⽹⻚源码先爬取下来 再解析
  有了替换⽬标之后结合打开的字体⽂件去找规律
  这⼀步可以借助⼀下 代码识别字体⽂件中的字体.py
  但是识别了之后最好⼈⼯校验⼀下
  校验完了之后 该替换的还是得统⼀进⾏替换
  eval()的使⽤:如果⾥⾯是⼀个可以计算的表达式那就会直接返回计算结果
              如果不是就会去掉⼀层引号
3.去⽹⻚源码(也可以是解析之后得数据)中进⾏替换
"""
from fontTools.ttLib import TTFont
from lxml import etree
import requests


# 获取网页源码
# 为了看清楚替换目标以及之后的替换
url = 'https://club.autohome.com.cn/bbs/thread/665330b6c7146767/80787515-1.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
}
res = requests.get(url, headers=headers)
# print(res.text)
text_str = res.text

# 解析页面数据
html = etree.HTML(text_str)
conten_lst = html.xpath('//div[@class="tz-paragraph"]//text()')
print(conten_lst)
# 从中发现替换目标：\uedb8 诸如此类的

# 加载字体文件
# car_font = TTFont('./qczj.ttf')
# # car_font.saveXML('car_font.xml')
# print(car_font.getGlyphOrder())

replace_dict = {'uniEC25': '多', 'uniEC27': '是', 'uniEC41': '矮', 'uniEC53': '短', 'uniEC5D': '右', 'uniEC6D': '三', 'uniEC6E': '和', 'uniEC77': '远', 'uniEC89': '呢', 'uniEC9A': '低', 'uniECA3': '了', 'uniECA4': '七', 'uniECBF': '八', 'uniECD0': '好', 'uniECD9': '五', 'uniECEA': '近', 'uniECF5': '的', 'uniED04': '十', 'uniED06': '上', 'uniED20': '九', 'uniED22': '下', 'uniED32': '二', 'uniED3C': '着', 'uniED4E': '小', 'uniED56': '更', 'uniED68': '长', 'uniED82': '不', 'uniED83': '得', 'uniED8C': '很', 'uniED9E': '坏', 'uniEDAF': '四', 'uniEDB8': '大', 'uniEDB9': '六', 'uniEDC9': '左', 'uniEDD4': '少', 'uniEDE5': '高', 'uniEDFF': '一', 'uniEE01': '地'}

# {'\uedb8': '大', '\ued06':'多' .......}

new_replave_dict = {}
for k,v in replace_dict.items():
    # r 防止被转义
    # \n
    key = r'"\u' + k[3:] + '"'
    # 先手动添加一层引号 然后用eval去掉一层
    new_key = eval(key)
    new_replave_dict[new_key] = v
print(new_replave_dict)

# 将列表内容拼接成完整的字符串
content_str = ''.join(conten_lst)

# 开始替换
for k,v in new_replave_dict.items():
    content_str = content_str.replace(k, v)
print(content_str)









