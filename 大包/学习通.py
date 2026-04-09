from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import re
from lxml import etree
import time
import random
import csv
data_list = []


# option = webdriver.ChromeOptions()
# option.add_experimental_option('excludeSwitches', ['enable-automation'])
# option.add_experimental_option("detach", True)
# 去掉window.navigator.webdriver的特性
# option.add_argument("disable-blink-features=AutomationControlled")
driver = webdriver.Chrome()
driver.get("https://passport2.chaoxing.com/login?newversion=true")
time.sleep(random.random()*2)





























