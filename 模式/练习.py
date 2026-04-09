from queue import Queue
import threading
import requests
from lxml import etree
import hashlib
import urllib.request
import time

# 单线程
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
# }
#
# for i in range(5):
#     url = f"https://www.fabiaoqing.com/biaoqing/lists/page/{i+1}.html"
#     response = requests.get(url, headers=headers)
#     html = etree.HTML(response.content)
#     for div in html.xpath('//*[@id="bqb"]/div[1]/div'):
#         img_url = div.xpath('./a/img/@data-original')[0]
#         # rspalt 从右边开始分割
#         name ='image/'+hashlib.md5(img_url.encode("utf-8")).hexdigest() + '.' + img_url.rsplit('.',1)[-1]
#         urllib.request.urlretrieve(img_url, name)

# 多线程
def produer(url_q,img_q):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
    }
    while True:
        if url_q.empty():
            break
        response = requests.get(url_q.get(),headers=headers)
        html = etree.HTML(response.content)
        for div in html.xpath('//*[@id="bqb"]/div[1]/div'):
            img_url = div.xpath('./a/img/@data-original')[0]
            img_q.put(img_url)


def consumer(img_q):
    while True:
        if img_q.empty():
            break
        img_url = img_q.get(i)
        name ='image2/'+hashlib.md5(img_url.encode("utf-8")).hexdigest() + '.' + img_url.rsplit('.',1)[-1]
        urllib.request.urlretrieve(img_url, name)


if __name__ == '__main__':
    url_q = Queue()
    img_q = Queue()
    for i in range(5):
        url = f"https://www.fabiaoqing.com/biaoqing/lists/page/{i + 1}.html"
        url_q.put(url)

    # 生产者
    p_list = []
    for i in range(1):
        t = threading.Thread(target=produer, args=(url_q, img_q))
        t.start()
        p_list.append(t)
    for t in p_list:
        t.join()
    print("已经打印完毕了")

    # 消费者
    c_list = []
    for i in range(10):
        t = threading.Thread(target=consumer, args=(img_q,))
        t.start()
        c_list.append(t)
    for t in p_list:
        t.join()





















