"""
-打开苏宁app（通过点击苏宁app来打开该app 避免出现闪退的情况）
-点击搜索框
-往搜索框⾥⾯输⼊搜索关键字
-点击搜索按钮
-解析-滑动-解析-滑动......(由于appium只能处理当前屏幕所呈现出来的数据 所以要边解析边滑动)

暂时不解析⼴告数据

在滑动进⾏解析的时候
- appium只能处理当前屏幕呈现出来的数据 也就是说我们看不到的数据是获取不到(⽤异常处理)
-滑动之后获取数据 会出现重复的情况 使⽤集合做去重处理
 将数据放⼊集合⾥⾯之前 需要转数据类型(如果是使⽤json转的 ⼩⼼中⽂)
"""


import time
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json


class Suning():
    def __init__(self, keyword):
        caps = dict()
        # 配置连接参数
        # 测试的系统
        caps['platformName'] = 'Android'
        # 手机安卓的版本
        caps['platformVersion'] = '5.1.1'
        # 设备名字 不重要
        caps['deviceName'] = 'Android'
        # 包名
        # caps['appPackage'] = 'com.android.browser'
        # 界面名
        # caps['appActivity'] = '.BrowserActivity'
        # 如果有需要输入中文 设置为True
        caps['unicodeKeyboard'] = True
        # 恢复原来的输入法
        caps['resetKeyboard'] = True
        # 一般来说 不需要重置app状态 设置为True
        caps['noReset'] = True

        # 加载驱动(连接到模拟器)
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)

        # 搜索关键字
        self.keyword = keyword

        # 显示等待
        self.wait = WebDriverWait(self.driver, 100)

        # 获取屏幕高度 方便滑动
        window_size = self.driver.get_window_size()
        self.height, self.width = window_size.get('height'), window_size.get('width')

        # 存储数据 用来给商品去重的
        self.info_set = set()

    # 搜索指定商品
    def search_product(self):
        # # 点击跳过
        # down_tag = self.wait.until(
        #     EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.TextView"))
        # )
        # down_tag.click()
        # print('点击跳过')

        # 定位搜索框
        search_tag = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'com.suning.mobile.ebuy:id/home_fragment_search_view_flipper'))
        )
        search_tag.click()
        print('定位搜索框')

        # 定位输入搜索框
        seach_input = self.wait.until(
            EC.presence_of_element_located((By.ID, 'com.suning.mobile.ebuy:id/et_search_input'))
        )
        seach_input.send_keys(self.keyword)

        time.sleep(0.5)

        # 点击搜索按钮
        self.driver.find_element(By.ID, 'com.suning.mobile.ebuy:id/tv_search_input_btn').click()
        print('点击搜索按钮')

        # 开始解析数据
        print('开始解析数据')
        self.parse_product()

    # 解析商品数据
    def parse_product(self):
       #  获取当前页面所有的商品信息 通对比 一个android.view.View存放的是一个商品的数据
       product_lst = self.wait.until(
           EC.presence_of_all_elements_located((By.XPATH, '//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout/android.view.View'))
       )
       for product in product_lst:
           '''
           碰到异常的两种情况：
           1. 广告
           2. 这个商品信息在当前屏幕并不完整
           '''
           try:
               item = {}
               # 获取商品名字 text获取定位到的元素文本
               item['title'] = product.find_element(By.ID,'com.suning.mobile.ebuy:id/tv_search_product_samll_name').text

               # 获取属性值
               item['attr'] = ''
               attr_lst = product.find_elements(By.XPATH,'//android.view.View[@resource-id="com.suning.mobile.ebuy:id/flow_view_product_attr_small"]//android.widget.TextView')
               for attr in attr_lst:
                   item['attr'] = item['attr'] + ' ' + attr.text

               # 其他属性
               other_attrs = product.find_elements(By.XPATH,"//android.widget.LinearLayout[@resource-id='com.suning.mobile.ebuy:id/flow_view_product_attr_center_small']/android.widget.LinearLayout")
               for other_attr in other_attrs:
                   # 属性值
                   content = other_attr.find_element(By.ID, 'com.suning.mobile.ebuy:id/tv_search_attr_item').text
                   # 属性名
                   name = other_attr.find_element(By.ID, 'com.suning.mobile.ebuy:id/tv_search_attr_item_name').text
                   item[name] = content

                   # 获取价格
                   item['price'] = product.find_element(By.ID, "com.suning.mobile.ebuy:id/tv_search_common_price").text
                   # 获取店铺名字
                   item['shopname'] = product.find_element(By.ID, "com.suning.mobile.ebuy:id/tv_shopname").text
                   print(item)
                   # json.dumps 将字典转为字符串 如果有中文 需要设置ensure_ascii
                   # 放集合中 做去重的处理
                   self.info_set.add(json.dumps(item, ensure_ascii=False))
           except:
               pass

           # 往下滑动 加载更多数据
           # 持续时间是以毫秒为单位的
           # 限定爬取数据的条数 来设置滑动的条件
           if len(self.info_set) < 10:
               self.driver.swipe(self.width * 0.5, self.height * 0.7, self.width * 0.5, self.height * 0.2, 1000)
               print('滑动成功')

               # 滑动完之后 继续解析
               self.parse_product()
           else:
               # 顺序跟咱爬取的顺序不太一样
               print(self.info_set)

    def main(self):
        # 关闭已经打开的苏宁
        try:
            self.driver.terminate_app('com.suning.mobile.ebuy')
        except:
            pass

        # 打开苏宁APP
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@content-desc="苏宁易购"]').click()
        time.sleep(2)
        self.search_product()

if __name__ == '__main__':
    s = Suning('手机')
    s.main()






















