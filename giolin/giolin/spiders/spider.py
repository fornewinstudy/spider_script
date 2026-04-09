import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/session']

    # def start_requests(self):
        # value = "4tZxtIQqzqV5-edJteA1QjKnHF8DQ2_tg8Yj0OKQLSDrdF4UvxNx3pQt6XF_NrbquMOUM4eNIq8Frul36DqCIQ"
        # value1 = "1654763402838"
        # data = {
        #     "commit":" Sign in",
        #     "authenticity_token":value,
        #     "login":"xmsjn",
        #     "password":"154862155",
        #     "webauthn - support":" supported",
        #     "webauthn - iuvpaa - support":"supported",
        #     "return_to: https":"// github.com / login",
        #     "timestamp":value1,
        #     "timestamp_secret":"e75f99a61780ad4c55a4d4fc2a4a6183d9e7288f0e20d4bd789b3fc790aec45d",
        # }
        # yield scrapy.FormRequest(self.start_urls[0],cookies=self.parse,formdata=data)


    def parse(self, response):
        authenticity_token = response.xpath('//input = [@name="authenticity_token"]/@value').get()
        timestamp = response.xpath('//input = [@name="timestamp"]/@value').get()
        timestamp_secret = response.xpath('//input = [@name="timestamp_secret"]/@value').get()

        data = {
            "commit":" Sign in",
            "authenticity_token":authenticity_token,
            "login":"xmsjn",
            "password":"154862155",
            "webauthn - support":" supported",
            "webauthn - iuvpaa - support":"supported",
            "return_to: https":"// github.com / login",
            "timestamp":timestamp,
            "timestamp_secret":timestamp_secret,
        }

        yield scrapy.FormRequest(url='https://github.com/session',cookies=self.after_login,formdata=data)


    def after_login(self,response):
        with open('github.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
