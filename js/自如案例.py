"""
第⼀个数字：0
第⼆个数字：21.4
第三个数字：42.8
第四个数字：64.2
从0开始的 以21.4为增量
我们就可以先准备⼀个替换字典(映射关系)
{'-0px':'7','-21.4px':'4'......}
x_list = ['-0px','-21.4px','-42.8px', '-64.2px', '-85.6px', '-107px','-128.4px', '-149.8px','-171.2px','-192.6px']
num_list = [6, 2, 9, 1, 0, .....]
识别图⽚中数字的⽅法：
1.超级鹰
2. tesseract(3.05左右的)
#讲两个列表合并成⼀个字典
zip(x_list, num_list)
通过简单的对⽐ 我们发现每次请求获得到数字图⽚是会变化的
那就意味着 我们需要⽤本次请求获取的图⽚去解析该次请求获得的源码
实现步骤：
1.获取到源码的同时拿到数字图⽚(url)
  -静态加载出来的⽹⻚直接就能够拿到⽬标url
  -发送请求获取源码
  -⽤正则去源码⾥⾯匹配图⽚url
  -通过url将图⽚保存到本地
2.根据数字图⽚得到数字列表(如何识别图⽚中的数字) 然后将数字列表跟偏移量列表合并成⼀个字典(映射关系)
  -识别图⽚中的数字通过正则去得到数字列表(findall)
  -将数字列表和偏移量列表合并成映射关系
3.拿着映射关系去源码中做替换(解析数据：先解析数据再⽤映射关系替换替换)
  -先解析数据分析⻚⾯结构根据⻚⾯结构的分析结果写xpath语句
  -通过xpath得到标题和偏移量(拿到span⾥⾯的style属性值通过切⽚得到偏移量)
  -⽤偏移量去映射关系⾥⾯找真实数据
  -拼接真实数据(两种：字符串的拼接和数字)
"""
import requests
from urllib import request
# pip install pytesseracet
import pytesseract
# pip install pillow
from PIL import Image
from lxml import etree
import re


class ZiRoom():
    def __init__(self):
        # 目标url
        self.url = 'https://www.ziroom.com/z/'
        # 请求头
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
        }
        # 数字图片
        self.back_num = 'back_num.png'

    # 获取网页源码以及图片
    def get_html(self):
        # 发送请求
        response = requests.get(self.url, headers = self.headers)
        # 从响应对象里面获取网页源码
        # print(response.text)
        html_str = response.text

        # 从网页源码里面拿到数字图片url
        # re.S 能够实现换行匹配的标志位
        result = re.search(r'background-image: url\((.*?)\)', html_str,re.S)
        # print(result.group(1))
        #       //static8.ziroom.com/phoenix/pc/images/price/new-list/377327c0373f87395ab1908cd1607c1.png
        # https://static8.ziroom.com/phoenix/pc/images/price/new-list/2e120609b7f35a9ebec0c72c4b7502b.png
        num_url = 'https:' + result.group(1)
        # print(num_url)

        # 根据图片url将图片进行保存到本地
        request.urlretrieve(num_url, self.back_num)
        return html_str


    # 解析数据
    def parse_html(self, html_str, replace_dict):
        # 每一套房屋对应的是一个class="item"的小div标签 这些div标签都放在一个class="Z_list-box"的大div标签
        html = etree.HTML(html_str)
        div_list = html.xpath('//div[@class="Z_list-box"]/div[@class="item"]')
        for div in div_list:
            # 获取标题
            # contains(@class, "title") 模糊匹配
            # title = div.xpath('.//h5[contains(@class, "title")]/a/text()')
            title = div.xpath('.//h5/a/text()')[0]
            print(title)

            # 获取偏移量
            span_list = div.xpath('.//span[@class="num"]')
            # print(span_list)
            price = ""
            for span in span_list:
                style = span.xpath('./@style')[0]
                pisition = style.split(': ')[-1]
                # print(pisition, replace_dict[pisition])
                price += replace_dict[pisition]
                print(price)
            print(title, price)


    def main(self):
        # 接收网页源码：html_str
        html_str = self.get_html()

        # 识别数字图片
        im = Image.open(self.back_num)
        res = pytesseract.image_to_string(im)
        # <class 'str'> 5471380629
        # print(type(res),res)
        # print(list(res))

        # 在正则里面有啥返回的是列表的数据类型
        # 得到数字列表
        num_list = re.findall(r'\d',res)
        # print(num_list)

        # 偏移量列表
        x_list = ['-0px', '-21.4px', '-42.8px', '-64.2px', '-85.6px', '-107px', '-128.4px', '-149.8px',                 '-171.2px', '-192.6px']

        # 将数字列表和偏移量列表合并成字典
        replace_dict = dict(zip(x_list, num_list))
        # print(replace_dict)

        # 解析数据
        self.parse_html(html_str,replace_dict)


if __name__ == '__main__':
    zr = ZiRoom()
    zr.main()




















