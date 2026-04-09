"""
获取名字
获取链接
保存csv
"""
# import requests
# from lxml import etree
# import csv
# data_lst = []
#
# url = 'https://www.runoob.com/python/python-socket.html'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
# }
# response = requests.get(url, headers=headers)
# html = etree.HTML(response.content)
# res = html.xpath('//*[@id="leftcolumn"]/a')
# for r in res:
#     itm = {}
#     itm['名字'] = r.xpath('./@title')[0]
#     itm['链接'] ='https://www.runoob.com' +  r.xpath('./@href')[0]
#     print(itm)
#     data_lst.append(itm)

# with open("python学习.csv", "w", encoding="utf-8", newline='') as a:
#     dat = csv.DictWriter(a, ['名字', "链接"])
#     dat.writeheader()
#     dat.writerows(data_lst)

# print('Hello,', end='\n')
# print('world!')
# print("\n","*"*50,"\n   这是我的第一个程序","\n","*"*50)

# name = input("姓名：")
# age = input("年龄：")
# diz = input("地址：")
# print(name,age,diz)

# dj = int(input("输入商品单价："))
# sl = int(input("输入商品数量："))
# zh = dj*sl
# print("商品的总价：",zh)
# import math
# a = int(input("请输入三角形的第一条边："))
# b = int(input("请输入三角形的第二条边："))
# c = int(input("请输入三角形的第三条边："))
# s = 1/2*(a+b+c)
# area = math.sqrt(s*(s-a)*(s-b)*(s-c))
# print("三角形的面积为：",area)


# a = 1
# b = 2
# if a > b:
#     print(True)
# else:
#     print(False)

# a = 0.01
# b = 666
# c = "123"
# print("变量a的值是：",a,"类型是：",type(a))
# print("变量b的值是：",b,"类型是：",type(b))
# print("变量c的值是：",c,"类型是：",type(c))

# print("iahjk jaklsjcf \n hgzucba")
# print("\\你")
# print(r"\\你")

# x = 3
# y = 5
# z = 2
# print((x^2+y)/z)
# print(13&9)


# for x in range(1,10):
#     for y in range(1,x+1):
#         print(x,"*",y,"=",x*y,"",end=" ")
#     print("")
#
# for a in range(1,10):
#     for b in range(1,a+1):
#         print(f"{a}*{b}={a*b}",end=" ")
#     print()

yf1 = [5,6,7,8,9,10]
yf2 = [1,2,3,4,11,12]
a = int(input("输入购买机票的月份："))
if a in yf1:
    ck = int(input("输入你的存款："))
    if ck >= 1000:
        print("最终支付",ck*0.9,"(元)")
    elif ck >= 600:
        print("最终支付",ck*0.7,"(元)")
    else:
        print("你的存款不足以购买机票")
elif a in yf2:
    ck = int(input("输入你的存款："))
    if ck >= 1000:
        print("最终支付", ck * 0.5,"(元)")
    elif ck >= 600:
        print("最终支付", ck * 0.3,"(元)")
    else:
        print("你的存款不足以购买机票")
else:
    print("请输入正确的月份")




















