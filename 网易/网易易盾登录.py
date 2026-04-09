"""
- 1. 打开目标网站
- 2. 切换验证模式
- 3. 直接点击完整验证(就不强制要求输入账号密码了)
- 4. 获取到验证码图片
- 5. 识别缺口位置
- 6. 滑动(要求滑动成功)
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



class WanYe():
    def __init__(self):
        # 目标url
        self.url = 'https://dun.163.com/trial/sense'

        # self.chrome_options = Options()
        # self.chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        # # options=self.chrome_options
        # 加载驱动
        self.driver = webdriver.Chrome()

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

    # 获取到验证码图片
    def get_captche(self):
        # 打开网站
        self.driver.get(self.url)

        # 切换登录模式
        model = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//li[@captcha-type="jigsaw"]'))
        )
        model.click()
        # 点击完成验证
        btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//span[@class="yidun_intelli-text"]'))
        )
        btn.click()
        time.sleep(2)

        # 找到图片的url
        back_url = self.driver.find_element(By.CLASS_NAME, 'yidun_bg-img').get_attribute('src')
        tp_url = self.driver.find_element(By.CLASS_NAME, 'yidun_jigsaw').get_attribute('src')
        # print(back_url, tp_url)

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


    def login(self):
        self.get_captche()

        # left 接收缺口位置 也就是待滑动的距离
        left = self.identify_gap(self.back_file, self.tp_file)
        print(left)

        left -= 4

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
    wy = WanYe()
    wy.login()








