"""
1.获取两张验证码图⽚
 -打开知乎⽬标⽹站
 -切换到密码登录的模式
 -分别输⼊账号和密码
 -点击登录按钮
 -找到两个img标签 获取到⾥⾯的src属性 也就是验证码图⽚的url 通过url将验证码图⽚保存到本地
2.识别缺⼝位置
 -通过openCV的⽅式对两张图⽚进⾏缺⼝识别 获取到缺⼝位置 也就是咱们需要滑动的距离
3.滑动
 -滑动滑块实现登录

  如果程序在滑动⽐较精准的情况下没有登录成功(或者返回的是其他的乱七⼋糟的反馈)
  这种情况下很有可能是该⽹站对你的某种⾏为做了检测⼀种是selenium另⼀种是滑动轨迹

⽤端⼝号打开浏览器能够最⼤程度的减少被识别出来的⻛险(确保之前打开的浏览器都关闭了)
-先在cmd中输⼊：chrome.exe --remote-debugging-port=9222(要么cd进⼊到chrome安装⽬录下要么把chrome的安装⽬录加⼊到环境变量中)
-然后在加载驱动的时候连接上打开的浏览器
self.chrome_options = Options()
self.chrome_options.add_experimental_option("debuggerAddress","127.0.0.1:9222")
#加载驱动
self.driver = webdriver.Chrome(options=self.chrome_options)
"""

import time
import random

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pyautogui
from urllib import request
import cv2


class ZhiHu():
    def __init__(self, username, password):
        # 目标url
        self.url = 'https://www.zhihu.com/signin?next=%2F'
        # 账号和密码
        self.username = username
        self.password = password

        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        # 加载驱动
        self.driver = webdriver.Chrome(options=self.chrome_options)

        # 窗口最大化处理
        try:
            self.driver.maximize_window()
        except:
            pass
        # 显示等待
        self.wait = WebDriverWait(self.driver, 100)

        # 有缺口的背景图片的保存位置
        self.back_file = 'back.jpg'
        # 缺口小图片的保存位置
        self.tp_file = 'tp.png'


    # 获取两张验证码图片 方便之后的识别
    def get_captche(self):
        # 1.1 打开知乎目标网站
        self.driver.get(self.url)

        # 1.2 切换登录模式
        # element_to_be_clickable 是有返回值的 如果等待到了 会将定位到的元素返回
        model = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//div[@class="SignFlow-tabs"]/div[@class="SignFlow-tab"][1]'))
        )
        model.click()

        # self.driver.find_element(By.XPATH, '//div[@class="SignFlow-tabs"]/div[@class="SignFlow-tab"][1]').click()

        # 输入账号密码
        username_input = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//input[@name="username"]'))
        )
        username_input.send_keys(self.username)

        password_input = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//input[@name="password"]'))
        )
        password_input.send_keys(self.password)

        # 输入完表单内容 进行下一步操作执勤 先强制一会会
        time.sleep(1)

        # 1.4 点击登录按钮
        btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
        )
        btn.click()

        # 1.5 找到并且保存验证码图片

        # 先确保验证码图片加载出来否
        self.wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.yidun_tips__text.yidun-fallback__tip'), '向右拖动滑块填充拼图')
        )
        # 最好结合一点儿强制等待使用
        time.sleep(1)
        # self.driver.save_screenshot('验证.png')
        """
        驱动·里面的xpath语句跟之前解析模块里面的xpath语句有点儿区别 主要是属性值的获取
        解析模块里面的xpath：//img[@class="yidun_bgimg"]/@src
        驱动里面的xpath：先定位到img 定位到了之后 在.get_attribute()获取属性值
        """
        # 找到图片的url
        back_url = self.driver.find_element(By.CLASS_NAME, 'yidun_bg-img').get_attribute('src')
        tp_url = self.driver.find_element(By.CLASS_NAME, 'yidun_jigsaw').get_attribute('src')
        print(back_url, tp_url)

        # 通过图片url将图片保存到本地
        request.urlretrieve(back_url, self.back_file)
        request.urlretrieve(tp_url, self.tp_file)


    # 识别缺口位置
    def identify_gap(selif, bg_image, tp_image, out="new_image.png"):
        """
        通过cv2计算缺口位置
        :param bg_image: 有缺口的背景图片文件
        :param tp_image: 缺口小图文件图片文件
        :param out: 绘制缺口边框之后的图片
        :return: 返回缺口位置 也就是咱们需要滑动的距离
        """
        # 读取背景图片和缺口图片
        bg_img = cv2.imread(bg_image)  # 背景图片
        tp_img = cv2.imread(tp_image)  # 缺口图片

        # 识别图片边缘
        # 因为验证码图片里面的目标缺口通常是有比较明显的边缘 所以可以借助边缘检测算法结合调整阈值来识别缺口
        # 目前应用比较广泛的边缘检测算法是Canny John F.Canny在1986年所开发的一个多级边缘检测算法 效果挺好的
        bg_edge = cv2.Canny(bg_img, 100, 200)
        tp_edge = cv2.Canny(tp_img, 100, 200)

        # 转换图片格式
        # 得到了图片边缘的灰度图，进一步将其图片格式转为RGB格式
        bg_pic = cv2.cvtColor(bg_edge, cv2.COLOR_GRAY2RGB)
        tp_pic = cv2.cvtColor(tp_edge, cv2.COLOR_GRAY2RGB)

        # 缺口匹配
        # 一幅图像中找与另一幅图像最匹配(相似)部分 算法：cv2.TM_CCOEFF_NORMED
        # 在背景图片中搜索对应的缺口
        res = cv2.matchTemplate(bg_pic, tp_pic, cv2.TM_CCOEFF_NORMED)
        # res为每个位置的匹配结果，代表了匹配的概率，选出其中「概率最高」的点，即为缺口匹配的位置
        # 从中获取min_val，max_val，min_loc，max_loc分别为匹配的最小值、匹配的最大值、最小值的位置、最大值的位置
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 寻找最优匹配

        # 绘制方框(人为校验)
        th, tw = tp_pic.shape[:2]
        tl = max_loc  # 左上角点的坐标
        br = (tl[0] + tw, tl[1] + th)  # 右下角点的坐标
        cv2.rectangle(bg_img, tl, br, (0, 0, 255), 2)  # 绘制矩形
        cv2.imwrite(out, bg_img)  # 保存在本地

        # 返回缺口的X坐标
        return tl[0]

    # 移动函数
    def move_slide(self, offset_x, offset_y, left):
        """
        :param offset_x: 滑块的x轴坐标
        :param offset_y: 滑块的y轴坐标
        :param left: 需要移动的距离
        :return:
        """
        # pip install pyautogui -i https://pypi.tuna.tsinghua.edu.cn/simple
        # pyautogui库操作鼠标指针
        # 移动到滑块的位置
        # duration为持续时间
        # random.uniform(参数1，参数2) 返回参数1和参数2之间的任意值
        pyautogui.moveTo(offset_x, offset_y,
                         duration=0.1 + random.uniform(0, 0.1 + random.randint(1, 100) / 100))

        # 按下鼠标 准备开始滑动
        pyautogui.mouseDown()
        # random.randint(参数1, 参数2) 函数返回参数1和参数2之间的任意整数
        offset_y += random.randint(9, 19)
        pyautogui.moveTo(offset_x + int(left * random.randint(15, 25) / 20), offset_y, duration=0.28)
        offset_y += random.randint(-9, 0)
        pyautogui.moveTo(offset_x + int(left * random.randint(18, 22) / 20), offset_y,
                         duration=random.randint(19, 31) / 100)
        offset_y += random.randint(0, 8)
        pyautogui.moveTo(offset_x + int(left * random.randint(19, 21) / 20), offset_y,
                         duration=random.randint(20, 40) / 100)
        offset_y += random.randint(-3, 3)
        pyautogui.moveTo(left + offset_x + random.randint(-3, 3), offset_y,
                         duration=0.5 + random.randint(-10, 10) / 100)
        offset_y += random.randint(-2, 2)
        pyautogui.moveTo(left + offset_x + random.randint(-2, 2), offset_y,
                         duration=0.5 + random.randint(-3, 3) / 100)
        # 释放鼠标
        pyautogui.mouseUp()
        time.sleep(3)

    # 主函数
    def login(self):
        # 获取验证码
        self.get_captche()

        # left 接收缺口位置 也就是待滑动的距离
        left = self.identify_gap(self.back_file, self.tp_file)
        print(left)

        left += 8

        # 定位滑块图标
        icon = self.driver.find_element(By.CLASS_NAME, "yidun_slider__icon")
        # location 用于获取定位好的元素的坐标
        location = icon.location
        print(location)

        # 从location里面提取出坐标位置
        x_offset = location.get('x')
        y_offset = location.get('y')

        self.move_slide(x_offset, y_offset, left)


if __name__ == '__main__':
    zh = ZhiHu('xxx', '123')
    zh.login()










