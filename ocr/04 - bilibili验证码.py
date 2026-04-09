from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from chaojiying import Chaojiying_Client
import time
import random
"""
https://passport.bilibili.com/login?from_id=333.1007.top_bar.l
"""
class Bilibili(object):
    def __init__(self):
        # 去除识别
        option = webdriver.ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        option.add_experimental_option("detach", True)
        # 去掉window.navigator.webdriver的特性
        option.add_argument("disable-blink-features=AutomationControlled")
        self.driver = webdriver.Chrome(options=option)
        self.driver.get('https://passport.bilibili.com/login?from_id=333.1007.top_bar.l')
    def deru(self):
        time.sleep(random.random() * 5)
        self.driver.find_element_by_id("login-username").send_keys("123456")
        time.sleep(random.random() * 5)
        self.driver.find_element_by_id("login-passwd").send_keys("123456")
        time.sleep(random.random() * 5)
        self.driver.find_element_by_class_name("btn-login").click()
        time.sleep(random.random() * 5)
        self.driver.implicitly_wait(10)  # 隐式等待

    def yzm(self):
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[6]/div/div').screenshot("bili.png") # 截图
        chaojiying = Chaojiying_Client('20201212', '153503', '933459')  # 用户中心>>软件ID 生成一个替换 96001
        im = open('bili.png', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
        pic_str = chaojiying.PostPic(im, 9004)["pic_str"]  # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
        print(pic_str)
        return pic_str

    def dianji(self,pic_str):
        ac = ActionChains(self.driver)
        for pic in pic_str.split("|"):
            x,y = pic.split(",")
            ac.pause(random.random() * 5)
            ac.move_to_element_with_offset(self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[6]/div/div'),int(x),int(y))
            ac.click()
        ac.pause(random.random() * 5)
        ac.click(self.driver.find_element_by_xpath('geetest_commit_tip'))
        ac.perform()

    def rou(self,):
        self.deru()
        pic_str = self.yzm()
        self.dianji(pic_str)


if __name__ == '__main__':
    bilibili = Bilibili()
    bilibili.rou()

























