# 安装pip install selenium
# 指定坂本 pip install selenium == 3.*
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time  # 时间模块
# 实例化浏览器
# 指定驱动路径executable_path="D://"
service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)
# 打开一个页面(网站)
driver.maximize_window()
driver.get("https://www.baidu.com")
time.sleep(2)
# driver.get("https://www.sogou.com/")

# 窗口最大化
# driver.maximize_window()
# time.sleep(2)

# 窗口最小化
# driver.minimize_window()
# time.sleep(2)

# 窗口后退
# time.sleep(2)
# driver.back()

# 窗口前进
# time.sleep(3)
# driver.forward()

# 拿到元素面板上面的html
# print(driver.page_source)

# 截图
# driver.save_screenshot("bd.png")

# 关闭浏览器
# driver.close() # 关闭当前网页
# driver.quit() # 关闭所有网页

# 练习
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com/")
# 通过id定位元素
# 输内容send_keys()
# # 点击click()
# driver.find_element_by_id("kw").send_keys("小姐姐")
# driver.find_element_by_id("su").click()
