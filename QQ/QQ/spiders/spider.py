import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['qq.com']
    start_urls = ['https://user.qzone.qq.com/3351932344/main']

    # 携带cookie
    def start_requests(self):
        cookie = 'x-stgw-ssl-info=165aced6aabd17a74ce76ab00b6e4fee|0.112|-|85|.|I|TLSv1.2|ECDHE-RSA-AES128-GCM-SHA256|40500|h2|0; pgv_pvid=5695147234; RK=IhetDZO16M; ptcz=46b3c5a03776f07fb10c92c795e566cad33c4253a27e2b0b43684ff28e39e922; qz_screen=1536x864; QZ_FE_WEBP_SUPPORT=1; cpu_performance_v8=0; __Q_w_s__QZN_TodoMsgCnt=1; _qpsvr_localtk=0.44005771522865644; pgv_info=ssid=s8160380330; uin=o3351932344; skey=@THfGILpEV; p_uin=o3351932344; pt4_token=wdQSoQS6EAjHdHq*sVdbjY*Q4mTQb6sKm2dIOpbK5BM_; p_skey=deg*pAMAIY80Sv0VLqZShyKv5YNrcFpE06-PU14eKQo_; Loading=Yes; x-stgw-ssl-info=e32f7842e78418ec1856ac3d6c2063f9|0.140|-|1|.|Y|TLSv1.2|ECDHE-RSA-AES128-GCM-SHA256|60000|h2|0; 3351932344_todaycount=0; 3351932344_totalcount=1224; __Q_w_s_hat_seed=1; v6uin=3351932344|qzone_player'
        cookies = {i.split('=')[0]:i.split("=")[1]for i in cookie.split(';')}
        yield scrapy.Request(
            url=self.start_urls[0],
            callback=self.parse,
            cookies=cookies
        )


    def parse(self, response):
        with open('qq.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
