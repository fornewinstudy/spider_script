#  com.android.settings/.Settings

import time

from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.extensions.android.nativekey import AndroidKey

caps = dict()
# 配置连接参数
# 测试的系统
caps['platformName'] = 'Android'
# 手机安卓的版本
caps['platformVersion'] = '5.1.1'
# 设备名字 不重要
caps['deviceName'] = 'Android'
# 包名
caps['appPackage'] = 'com.android.settings'
# 界面名
caps['appActivity'] = '.Settings'
# 如果有需要输入中文 设置为True
caps['unicodeKeyboard'] = True
# 恢复原来的输入法
caps['resetKeyboard'] = True
# 一般来说 不需要重置app状态 设置为True
caps['noReset'] = True


# 加载驱动(打开浏览器)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)

# 定位到WLAN
WLAN = driver.find_element(By.XPATH, '//*[@text="WLAN"]')
# WLAN.click()

# 定位到应用
yy = driver.find_element(By.XPATH, '//*[@text="应用"]')

# 滑动 从某一个元素滑动到另一个元素
# 从注意滑动方向 从应用到WLAN
# drag_and_drop速度慢 精准 没有惯性
# driver.drag_and_drop(yy, WLAN)

# 滑动 从某一个元素滑动到另一个元素
# 从注意滑动方向 从应用到WLAN
# scroll速度快 不是很精准 有惯性
driver.scroll(yy, WLAN)




















