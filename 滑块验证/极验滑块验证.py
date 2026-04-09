"""
1.获取到两张图⽚ ⼀张是由缺⼝的背景图⽚ ⼀张是没有缺⼝的背景图⽚
先找到所有的canvas标签
如何通过python修改elements⾥⾯的源代码(如何实时操作修改elements⾥⾯的源码)：
我们是可以通过driver执⾏js代码的
-把第⼆个的style从"opacity: 1; display: block;"改为"opacity: 1; display:none;"得到有缺⼝的背景图⽚
-把第三个style从"display: none; opacity: 0;"修改为""得到没有缺⼝的背景图⽚
-如何把修改好样式的图⽚保存到本地
2.通过像素对⽐两张图⽚从⽽获取到缺⼝位置
3.⽤selenium进⾏滑动
"""

import time
import random

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# <class 'selenium.webdriver.remote.webelement.WebElement'>
from selenium.webdriver.remote.webelement import WebElement
from PIL import Image
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui


class Slide():
    def __init__(self):
        # 加载驱动
        self.driver = webdriver.Chrome()
        try:
            # 窗口最大化
            self.driver.maximize_window()
        except:
            pass
        # 显示等待
        self.wait = WebDriverWait(self.driver, 100)

        # 目标url
        self.url = 'https://www.geetest.com/demo/slide-float.html'

        # 有缺口的背景图片保存图片位置
        self.gap_img = 'gap.png'
        # 完整图片的保存位置
        self.intact_img = 'intact.png'

    # 获取验证码图片(并且保存到本地)
    def get_captche(self):
        self.driver.get(self.url)

        # 有时候 显示等待返回的是定位好的元素 有时候是布尔值
        # 点击按钮 加载验证码
        self.wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME,'geetest_radar_tip_content'), "点击按钮进行验证")
        )
        self.driver.find_element(By.CLASS_NAME,'geetest_radar_tip_content').click()

        # 确定滑块加载出来之后 在进行后续的操做
        self.wait.until(
            # 如果是用的class属性进行的定位 就用.
            # 如果是用的id属性进行的定位 就用#
            EC.text_to_be_present_in_element((By.CSS_SELECTOR,'.geetest_slider_tip.geetest_fade'), '拖动滑块完成拼图')
        )
        time.sleep(1)

        # 滑块加载完成之后 截图(在处理滑块的时候 需要特别注意自己电脑设置里面的屏幕中的缩放布局)
        # page_source = seli.driver.page_sourse
        # 通过driver执行js代码 execute_script
        # 如果不确定下标索引从零开始的 还是从一开始的 可以测试一下：从0开始
        self.driver.execute_script('document.querySelectorAll("canvas")[1].style="opacity: 1; display:none;"')

        # 截图 screenshot
        captcha_tag = self.driver.find_element(By.CLASS_NAME, "geetest_window")
        # 获取有缺口的
        captcha_tag.screenshot(self.gap_img)

        # 先修改css样式 得到完整图片
        self.driver.execute_script('document.querySelectorAll("canvas")[2].style=""')
        captcha_tag.screenshot(self.intact_img)

    # 进行识别
    #获取缺⼝偏移量
    def get_gap(self,image1, image2):
        """
        :param image1:
        :param image2:
        :return:返回偏移量
        """
        #打开图⽚
        image1_img=Image.open(image1)
        image2_img=Image.open(image2)

        # print(image1_img.size)  # (260, 160)
        # exit()
        #遍历图⽚的每个坐标点
        # image1_img和image2_img的⻓宽是⼀样的所以在遍历的时候⽤其中⼀张就⾏
        for i in range(image1_img.size[0]):
            for j in range(image1_img.size[1]):
                if not self.is_pixel_equal(image1_img, image2_img, i, j):
                    return i

    #判断这个坐标点像素是否相同
    def is_pixel_equal(self,image1, image2, x, y):
        """
        :param image1:图⽚⼀
        :param image2:图⽚⼆
        :param x:需要对⽐的坐标(x)
        :param y:需要对⽐的坐标(y)
        :return:像素是否相同 相同返回True 不同返回False
        """
        #获取两个图⽚的像素点
        pixel1=image1.load()[x, y]
        pixel2=image2.load()[x, y]

        # 阈值
        threshold=60
        # 获取到两张图⽚对应像素点的RGB数据
        # 如果差距在⼀定范围之类 就代表两个像素相同 继续对⽐下⼀个像素点
        # 如果差距超过⼀定范围 则表示像素点不同 即为缺⼝位置
        if abs(pixel1[0] - pixel2[0]) < threshold and abs(pixel1[1] - pixel2[1]) < threshold and abs(
                pixel1[2] - pixel2[2]) < threshold:
            return True
        return False

    # 生成移动轨迹
    def get_track(self, distance):
        # 移动轨迹
        track = []
        # 当前位置
        current = 0
        """
        如果是匀速运动 极验很有可能会识别出它是程序的操作 因为人是没有办法做到完全匀速拖动的
        需要用到物理学里面的两个公式
        通过这两个公式可以构造轨迹移动算法 计算出先加速后减速的运动轨迹
        """
        # 减速阈值(大概到3/4的位置 开始减速)
        mid = distance * 3 / 4
        # 计算间隔
        t = 0.1
        # 初速度
        v = 0
        while current < distance:
            if current < mid:
                a = random.randint(2, 3)
            else:
                a = -random.randint(7, 8)
            # 初速度
            v0 = v
            # 当前速度
            v = v0 + a * t
            # 移动距离
            move = v0 * t + 0.5 * a * t * t
            # round：https://www.runoob.com/python/func-number-round.html
            track.append(round(move))  # 把计算得到的新的移动距离放入移动轨迹列表中
            current += move  # 更新当前位置
        return track

    # 进行滑动
    # 移动函数
    def move_slide(self, offset_x, offset_y, left):
        """
        :param offset_x: 滑块的x轴坐标
        :param offset_y: 滑块的y轴坐标
        :param left: 需要移动的举例
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

    # 调用
    def main(self):
        # 1. 获取到两张验证码图片
        self.get_captche()
        # 2. 识别
        left = self.get_gap(self.gap_img, self.intact_img)
        # print(left)

        # 实际滑动距离需要做细微的调整
        left -= 5

        # 3. 滑动
        # 3.1 先生成移动的轨迹列表 track
        # track = self.get_track(left)
        # print(track)
        # # 定位到滑动按钮
        # btn = self.driver.find_element(By.CLASS_NAME, "geetest_slider_button")
        #
        # # 移动到滑块位置 并且摁住 准备滑动
        # ActionChains(self.driver).click_and_hold(btn).perform()
        # for x in track:
        #     ActionChains(self.driver).move_by_offset(xoffset=x, yoffset=0).perform()
        # time.sleep(0.5)
        # # 释放
        # ActionChains(self.driver).release().perform()

        # 936, 465 滑块的坐标位置需要调整
        self.move_slide(936, 465, left)

if __name__ == '__main__':
    s = Slide()
    s.main()

    """
    1.获取到两张图⽚ ⼀张是由缺⼝的背景图⽚ ⼀张是没有缺⼝的背景图⽚
    先确保验证码图⽚加载出来(显示+强制)
    修改样式 才能出现我们需要的图⽚
    先找到所有的canvas标签
    如何通过python修改elements⾥⾯的源代码(如果实时操作修改elements⾥⾯的源码)：
    我们是可以通过driver执⾏js代码的 execute_script
    document.querySelectorAll("canvas")下标索引是从0开始的
    -把第⼆个的style从"opacity: 1; display: block;"改为"opacity: 1; display:none;"得到有缺⼝的背景图⽚
    -把第三个style从"display: none; opacity: 0;"修改为""得到没有缺⼝的背景图⽚
    -如何把修改好样式的图⽚保存到本地
    2.通过像素对⽐两张图⽚ 从⽽获取到缺⼝位置
    3.进⾏滑动
    """