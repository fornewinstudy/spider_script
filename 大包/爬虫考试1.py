"""
目标地址：https://finance.sina.com.cn/realstock/company/sh600835/nc.shtml

实时获取
上午9：00-11：30
下午13：00-15：00
每隔3秒获取一次
数据保存到csv文件内
"""
import time
import requests
from lxml import etree
import csv
import re

data_lst = []

class shanghai():
    def __init__(self):
        dact = round(time.time())
        self.url_lst = f"https://hq.sinajs.cn/etag.php?_={dact}&list=sh600835"
        self.url = 'https://finance.sina.com.cn/realstock/company/sh600835/nc.shtml'

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'Referer': 'https://finance.sina.com.cn/realstock/company/sh600835/nc.shtml',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"'
        }

    def mei(self):
        # 发送请求
        response = requests.get(url=self.url, headers = self.headers)
        html = etree.HTML(response.content.decode("gb2312"))
        response = requests.get(url=self.url_lst, headers=self.headers)
        # print(response.text)
        res = response.text.split("2022")[0]
        # print(res)
        res_lst = re.findall(r'(.*?),(.*?),', res)
        # print(res_lst)
        # res = response.text.split(',')
        # print(res, type(res))
        # print(html)
        # 获取该页面的代码
        li_tag_list = html.xpath('//*[@id="tabfive"]/tbody/tr/th/text()')
        before = li_tag_list[0:5]
        # print(li_tag_list[0:5])
        for index, li_take in enumerate(before):
            # print(index, li_take)
            itme = {}
            itme["买"] = li_take
            itme['价'] = round(float(res_lst[14-index][1]), 3)
            itme['量'] = res_lst[14-index][0][:-2]
            # print(itme)
            data_lst.append(itme)
        itme = {}
        # print(li_tag_list[5])
        itme['买'] = li_tag_list[5]
        itme['价'] = round(float(res_lst[3][0]), 3)
        itme['量'] = ''
        # print(itme)
        data_lst.append(itme)

        after = li_tag_list[6:11]
        # print(after)
        for index, li_take in enumerate(after):
            # print(index, li_take)
            itme = {}
            itme["买"] = li_take
            itme['价'] = round(float(res_lst[5 + index][1]), 3)
            itme['量'] = res_lst[5 + index][0][:-2]
            # print(itme)
            data_lst.append(itme)

            # exit()

            # # itme["价"] = res[11:30:2]
            # # itme["量"] = res[10:29:2]
            # print(itme)
            # return data_lst.append(itme)
        print(data_lst)
        return data_lst

    def baoc(self):
        with open("上海机电.csv", "w", encoding="utf-8", newline="") as a:
            wt = csv.DictWriter(a, ["买" , "价", "量"])
            wt.writeheader()
            wt.writerows(data_lst)

    def mian(self):
        while True:
            time.sleep(3)
            self.mei()
            self.baoc()

if __name__ == '__main__':
    tm = time.strftime('%H.%M',time.localtime())
    if 9 <= float(tm) <= 11.30:
        s = shanghai()
        s.mian()
    elif 13 <= float(tm) < 15:
        s = shanghai()
        s.mian()
    else:
        pass











