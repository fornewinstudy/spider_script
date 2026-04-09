# cookie和Session
# import requests
# url= "https://i.chaoxing.com/base?t=1650173116274"
# headers = {
#     "Cookie": "lv=2; fid=30766; _uid=157125969; uf=94ffe74515793f36d90bbacee9fca287be426f6af487028482c8afe249601c68d95d3e405e0cc04d709c958a11e0595a2a80cd29a298e70788b83130e7eb4704399c98527e5336171c02e4163ea748924129e2925200b376692f0a635621fa61fbab748716933757e7fafd565af53bf2; _d=1650101686378; UID=157125969; vc=43DD92318A41DC2C7D84EBBF1C639FFD; vc2=86218C5601D82C654C3B4220264A8917; vc3=KmZncJ4BxeGZFhy1588KulW6%2BQ4CZ1ialtXjjmydxHMdvojkPIH1t%2F6Whxu6DdFzAUGbcplqy1UEFWasu01cY8Kj94DcGOqu48JjivcLAjGpi2vNLWABwUHdAVoe%2BJ5g5d4skQv8LhV5pbcS03oJq6ByUWhW6rSAW5RBGpHpenI%3D1ae299779b9c7c09fe07b92936490184; xxtenc=1d549fe355945001f79268c359a1436e; DSSTASH_LOG=C_38-UN_29222-US_157125969-T_1650101686379; JSESSIONID=70B2302A9BE8CA1114CF165766C70C83; source=""; spaceFid=30766; spaceRoleId=""",
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
# }
# response = requests.get(url,headers=headers)
# print(response.content.decode("utf-8"))

# import requests
# # Session()作用是把俩个请求都执行
# session = requests.Session()
# url = "https://passport2.chaoxing.com/getauthstatus"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
# }
# data={
#     "enc": "adb816700921e25080a289c8d7307e4e",
#     "uuid": "330832b6b35e4491811762c23e64401c",
# }
# session.post(url,headers=headers,data=data)
# response=session.get("https://notice.chaoxing.com/pc/notice/myNotice?s=8b71a604a92a2bd004d066f1c761a912",headers=headers)
# print(response.content.decode("utf-8"))

# cookie反爬
# import requests
# import json
# """
# 3 这次
# 23 软卧 一等卧
# """
# url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2022-04-18&leftTicketDTO.from_station=CSQ&leftTicketDTO.to_station=GZQ&purpose_codes=ADULT"
# headers = {
#     "Cookie": "_uab_collina=165017584405693706229486; JSESSIONID=39E3D9AE822E6196602C6440077E7BB9; route=c5c62a339e7744272a54643b3be5bf64; BIGipServerotn=1156579850.50210.0000; _jc_save_fromStation=%u957F%u6C99%2CCSQ; _jc_save_toStation=%u5E7F%u5DDE%2CGZQ; _jc_save_fromDate=2022-04-18; _jc_save_toDate=2022-04-17; _jc_save_wfdc_flag=dc",
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
# }
# response = requests.get(url,headers=headers)
# res_json = json.loads(response.text)
# for i in res_json["data"]["result"]:
#     # for n, dt in enumerate(i.split("|")):
#     #     print(n,dt)
#     # break
#     data_cc = i.split("|")
#     print(f"车次：{data_cc[3]} 软卧一等卧：{data_cc[23]}")

# referer反爬
"""
https://video.pearvideo.com/mp4/short/20220416/cont-1749827-15862840-hd.mp4
https://video.pearvideo.com/mp4/short/20220416/1650178813736-15862840-hd.mp4

"""
"""
思路：
用户要输入url
把url后面一部分提取出来
读xhr里面的一个url发送请求，拿到视频的url
对url进行替换
"""
# import requests
# work = input("请输入你要下载的梨视频url：")
# # work = "https://www.pearvideo.com/video_1749827"
# c_id = work.split("_")[-1]  # split 从左到右进行分割  rsplit 从又到左进行分割
# headers = {
#     "Referer": f"https://www.pearvideo.com/video_{c_id}",
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
# }
# url = f"https://www.pearvideo.com/videoStatus.jsp?contId={c_id}&mrd=0.17117958158658708"
# # print(url)
# response = requests.get(url,headers=headers)
# mp4_url = response.json()["videoInfo"]["videos"]["srcUrl"]
# m2_url = mp4_url.replace(mp4_url.rsplit("/",1)[-1].split("-",1)[0],f"cont-{c_id}")
# # print(m2_url)
# with open(f"sp.mp4","wb") as a:
#     a.write(requests.get(m2_url).content)

# 代理ip

# 代理ip的分类
# 匿名度
# 透明的 服务器知道你用了代理ip，也知道你真实的ip
# 匿名的 服务器知道你用了代理ip，不知道你真实的ip
# 高匿的 服务器不知道你用了代理ip，也不知道你真实的ip

# 查看ip的方法
# 1、直接在百度上收索
# 2、http://httpbin.org/ip
# 3、cmd ipconfig
# import requests
# url = "http://httpbin.org/ip"
# pox = {
#     "http":"http://200.125.168.132:999",
#     "https":"http://200.125.168.132:999"
# }
# res = requests.get(url,proxies=pox)
# print(res)




