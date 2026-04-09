# 过识别
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
# 去除识别
option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option("detach", True)
# 去掉window.navigator.webdriver的特性
option.add_argument("disable-blink-features=AutomationControlled")
# 设置无头 -->> 看不到网页打开
option.add_argument('--headless')

driver = webdriver.Chrome(options=option)
driver.get('https://www.baidu.com/')
print(driver.current_url)
# time.sleep(2)
# driver.close()
# driver.quit()