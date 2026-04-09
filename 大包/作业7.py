"""
(必做题1)目标网站：https://www.1ppt.com/moban/
需求：
1、用多线程爬取前10页模板名字和模板下载链接
2、把模板保存到moban文件夹里面
"""
# from queue import Queue
# import threading
# import csv
# from lxml import etree
# import requests
#
# # 生产者
# def produer(url_q, img_q):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
#     }
#     while True:
#         if url_q.empty():
#             break
#         response = requests.get(url_q.get(), headers=headers)
#         # 方法一
#         # response.encoding = 'gb2312'
#         # 方法二
#         data = response.content.decode('gb2312')
#         img_q.put(data)
#         # print(img_q)
#
#
# # 消费者
# def consumer(img_q):
#     data_list = []
#     while True:
#         if img_q.empty():
#             break
#         img_url = img_q.get(i)
#         img_url = etree.HTML(img_url)
#         a =img_url.xpath('/html/body/div[5]/dl/dd/ul/li')
#         for img in a:
#             data = {}
#             name = img.xpath('./h2/a/text()')[0]
#             list = 'https://www.1ppt.com' + img.xpath('./h2/a/@href')[0]
#             data['name'] = name
#             data['list'] = list
#             data_list.append(data)
#     with open("模板.csv", "w", encoding="utf-8",newline='') as a:
#         dat = csv.DictWriter(a,["name", 'list'])
#         dat.writeheader()
#         dat.writerows(data_list)
#
# # 程序的主入口__name__ == '__main__':
# if __name__ == '__main__':
#     url_q = Queue()
#     img_q = Queue()
#     for i in range(1, 11):
#         url = f"https://www.1ppt.com/moban/ppt_moban_{i}.html"
#         url_q.put(url)
#     # 生产者
#     p_list = []
#     for i in range(3):
#         t = threading.Thread(target=produer, args=(url_q, img_q))
#         t.start()
#         p_list.append(t)
#     for a in p_list:
#         a.join()
#
#     # 消费者
#     c_list = []
#     for i in range(3):
#         t = threading.Thread(target=consumer, args=(img_q,))
#         t.start()
#         c_list.append(t)
#     for b in p_list:
#         b.join()




"""
(必做题2)目标网站：https://sc.chinaz.com/tupian/ 
需求： 1、用多线程爬取前10页图片链接和图片名 
      2、把图片保存到tupian文件夹里面
"""

from queue import Queue
import threading
import csv
from lxml import etree
import requests

# 生产者
def produer(url_q, img_q):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
    }
    while True:
        if url_q.empty():
            break
        response = requests.get(url_q.get(), headers=headers)
        # 方法一
        # response.encoding = 'gb2312'
        # 方法二
        data = response.content.decode('utf-8')
        img_q.put(data)
        # print(img_q)


# 消费者
def consumer(img_q):
    data_list = []
    while True:
        if img_q.empty():
            break
        img_url = img_q.get(i)
        img_url = etree.HTML(img_url)
        a =img_url.xpath('//*[@id="container"]/div')
        for img in a:
            data = {}
            name = img.xpath('.//a/@alt')[0]
            list = 'https:' + img.xpath('.//a/img/@src2')[0]
            data['name'] = name
            data['list'] = list
            data_list.append(data)
    with open("tupian.csv", "w", encoding="utf-8",newline='') as a:
        dat = csv.DictWriter(a,["name", 'list'])
        dat.writeheader()
        dat.writerows(data_list)

# 程序的主入口__name__ == '__main__':
if __name__ == '__main__':
    url_q = Queue()
    img_q = Queue()
    for i in range(1, 5):
        if i == 1:
            url = 'https://sc.chinaz.com/tupian/index.html'
        else:
            url = f"https://sc.chinaz.com/tupian/index_{i}.html"
        url_q.put(url)
    # 生产者
    p_list = []
    for i in range(3):
        t = threading.Thread(target=produer, args=(url_q, img_q))
        t.start()
        p_list.append(t)
    for a in p_list:
        a.join()

    # 消费者
    c_list = []
    for i in range(3):
        t = threading.Thread(target=consumer, args=(img_q,))
        t.start()
        c_list.append(t)
    for b in c_list:
        b.join()




















