"""
8.(必做题2)目标网站：https://music.163.com/#/song?id=399354373
需求：
1、翻页爬取此音乐对应的评论信息
2、保存到csv(名字和评论要对应)
"""
"""
当我们在获取滚动位置时，常常使用document.documentElement.scrollTop来获取垂直滚动的偏移值，
document.documentElement.scrollLeft来获取水平滚动的偏移值。
document.documentElement.clientHeight => 就是网页在浏览器中可见高度，不包括浏览器自身的状态栏，随着浏览器大小变化；
"""

from selenium import webdriver
from lxml import etree
import time
import csv
import random
# 用来保存数据的
data_list = []
# 去除识别
option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option("detach", True)
# 去掉window.navigator.webdriver的特性
option.add_argument("disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=option)
driver.get("https://music.163.com/#/song?id=399354373")
time.sleep(random.random()*2)
# switch_to.frame()可以通过三种属性来定位(name、索引、xpath)
# 切换iframe标签
driver.switch_to.frame('contentFrame')
for i in range(5):
    # 滑动到最底下
    while True:
        h1 = driver.execute_script('return document.body.scrollHeight;')
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(2)
        h2 = driver.execute_script('return document.body.scrollHeight;')
        if h1 == h2:
            break
    time.sleep(2)
    html = etree.HTML(driver.page_source)
    for div in html.xpath('//div[@class="itm"]'):
        data_list.append(dict(name = div.xpath('.//div[@class="cnt f-brk"]/a/text()')[0],
                              comm = div.xpath('.//div[@class="cnt f-brk"]/text()')[0]))
    driver.find_element_by_xpath('//a[text()="下一页"]').click()

with open('网易云评论.csv', 'w', encoding='utf-8', newline='') as f:
    wt = csv.DictWriter(f, ['name', 'comm'])
    wt.writeheader()
    wt.writerows(data_list)



# """
# 7.(必做题1)目标网站：http://www.51job.com
# 需求：
# 1、点击高级搜索
# 2、输入关键字 python
# 3、地区选择 广州
# 4、职能类别选择 计算机 -> 后端开发 -> python开发工程师
# 5、工作年限选择 1-3年
# 6、抓取到所有的岗位标题和里面的职位信息（职位信息可不做）
# 7、保存到csv
# """
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import time
import random
import csv
# 用来保存数据的
data_list = []
# 去除识别
option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option("detach", True)
# 去掉window.navigator.webdriver的特性
option.add_argument("disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=option)
driver.get('http://www.51job.com')
time.sleep(random.random()*3)
# 点击高级搜索
driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/a').click()
time.sleep(random.random()*3)
# 输入关键字 python
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/p[1]/input').send_keys('python')
time.sleep(random.random()*3)
# 地区选择 广州
driver.find_element_by_xpath('//*[@id="work_position_click"]/em').click()
time.sleep(random.random()*3)
driver.find_element_by_xpath('//div[@id="work_position_click_multiple_selected"]/span[1]').click()
time.sleep(random.random()*3)
driver.find_element_by_xpath('//em[text()="广州"]').click()
time.sleep(random.random()*3)
driver.find_element_by_id('work_position_click_bottom_save').click()
time.sleep(random.random()*3)
# 职能类别选择 计算机 -> 后端开发 -> python开发工程师
# arguments这个就相当于*args - def fn(*args):
driver.execute_script('arguments[0].click()',driver.find_element_by_id('funtype_click'))
time.sleep(random.random()*3)
driver.find_element_by_xpath('//em[text()="后端开发"]').click()
time.sleep(random.random()*3)
driver.find_element_by_xpath('//em[text()="Python开发工程师"]').click()
time.sleep(random.random()*3)
driver.find_element_by_id('funtype_click_bottom_save').click()
time.sleep(random.random()*3)
# 工作年限选择 1-3年
driver.find_element_by_xpath('//div[@id="workyear_list"]/span').click()
time.sleep(random.random()*3)
driver.find_element_by_xpath('//span[text()="1-3年"]').click()
time.sleep(random.random()*3)
# 点击搜索
div = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[10]/span').click()
time.sleep(random.random()*3)
# 提取数据
while True:
    time.sleep(random.random() * 3)
    for span in driver.find_elements_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div[4]/div[1]/div/a/p[1]/span[1]'):
        data_list.append(dict(name=span.text))
    try:
        driver.find_element_by_xpath('//li[@class="next"]/a').click()
        time.sleep(random.random() * 3)
    except:
        break
print(data_list)
driver.close()
driver.quit()
with open('zp.csv', 'w', encoding='utf-8', newline='') as f:
    wt = csv.DictWriter(f, ['name'])
    wt.writeheader()
    wt.writerows(data_list)








































