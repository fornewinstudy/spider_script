import requests
from pprint import pprint

# 目标url
# keyword 指向关键字
# page 用来实现翻页的

url = 'http://mapi7.dangdang.com/index.php?page_version=new2&access-token=&time_code=e75a9de5092e25738f270e619d92667c&img_size=e&client_version=10.12.4&pageSize=10&union_id=537-100998&timestamp=1657178413&province_id=111&permanent_id=20220707151927745580104551719123089&a=all-search&global_province_id=111&page_action=search&c=search&sort_type=default_0&keyword=%E7%88%AC%E8%99%AB&udid=6dfdfd3043cd1c00f77c6ebe0b0cb7d6&user_client=android&page=1'

"""
GET http://mapi7.dangdang.com/index.php?page_version=new2&access-token=&time_code=e75a9de5092e25738f270e619d92667c&img_size=e&client_version=10.12.4&pageSize=10&union_id=537-100998&timestamp=1657178413&province_id=111&permanent_id=20220707151927745580104551719123089&a=all-search&global_province_id=111&page_action=search&c=search&sort_type=default_0&keyword=%E7%88%AC%E8%99%AB&udid=6dfdfd3043cd1c00f77c6ebe0b0cb7d6&user_client=android&page=1 HTTP/1.1
Content-type: application/json
User-Agent: Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G973N Build/PPR1.190810.011)
Host: mapi7.dangdang.com
Connection: Keep-Alive
Accept-Encoding: gzip


HTTP/1.1 200 OK
Server: DD-Engine/3.9
Date: Thu, 07 Jul 2022 07:20:14 GMT
Content-Type: application/json; charset=utf-8
Connection: keep-alive
Vary: Accept-Encoding
Vary: Accept-Encoding
Access-Control-Allow-Origin: *
X-DD-Gateway-Upstream-Latency: 169
X-DD-Gateway-Proxy-Latency: 0
Content-Length: 27366

"""
# 请求头
headers = {
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G973N Build/PPR1.190810.011)'
}

# 发送请求
res = requests.get(url, headers=headers)
# text 先用text获取 确定是json格式的数据之后 在用json()
# print(res.text)
# print(res.json())
# pprint 对控制台的输出结果做了格式化处理 方便后续的分析
# pprint(res.json()['data']['product'])

# 当前页面所有的图书的数据放在一个列表里面 列表里面的每一个元素对应的是一本图书的数据
pro_lst = res.json()['data']['product']
for pro in pro_lst:
    # pprint(pro)
    item = {}

    #图书的名字
    item['productName'] = pro.get('productName')
    # 作者
    item['author'] = pro.get('author')
    # 出版社
    item['publisher'] = pro.get('publisher')
    # 好评率
    item['goodCommentRate'] = pro.get('goodCommentRate')
    # 价格
    item['price'] = pro.get('price')
    print(item)


















