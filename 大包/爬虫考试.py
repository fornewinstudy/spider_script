"""
抓取掘金文章：https://juejin.cn/backend/Python
抓取Python类名下面前300篇文章，并保存，抓取要求：
1.文章标题
2.文章作者
3.文章内容
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import re
from lxml import etree
import time
import random
import csv
data_list = []

driver = webdriver.Chrome()
driver.get("https://juejin.cn/backend/Python")
time.sleep(random.random()*2)
main_list = driver.find_elements(By.XPATH,'//div[@class="entry-list-wrap"]/div/li')
# print(main_list)
while True:
    for main in main_list:
        time.sleep(2)
        try:
            main.click()
        except:
            driver.execute_script('arguments[0].scrollIntoView()', main)
            main.click()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(2)
        html = etree.HTML(driver.page_source)
        for div in html.xpath('//div[@class="main-area article-area"]/article'):
            data = {}
            data['文章标题'] = div.xpath('./h1/text()'.strip())
            data['文章作者'] = div.xpath('./div/div[1]/a/span[1]/text()')
            data['文章内容'] = ''.join(div.xpath('./div[4]/div/p//text()'))
            data_list.append(data)

        time.sleep(3)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    driver.close() # 关闭当前网页
    driver.quit() # 关闭所有网页











