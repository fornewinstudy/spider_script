# 定位元素
# from selenium import webdriver
# import time  # 时间模块
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com/")
# # 通过id定位元素
# # 输内容send_keys()
# # 点击click()
# # driver.find_element_by_id("kw").send_keys("小姐姐")
# driver.find_element(By.ID,"kw").send_keys("小姐姐")
# # driver.find_element_by_id("su").click()
# driver.find_element(By.ID,"su").click()
# driver.close() # 关闭当前网页
# driver.quit() # 关闭所有网页


# 定位元素
# """
# <input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off">
# """
# from selenium import webdriver
# # import time  # 时间模块
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.find_elements()  # 加了一个s可以提取多个，并且返回一个列表
#
# # find_element_by_id：根据id来查找个元素某(要求掌握)
# driver.find_element_by_id('kw')  # 没有s则返回一个标签对象
# driver.find_element(By.ID,'kw')
#
#
# # find_element_by_class_name：根据类名查找元素  ->> 通过class来查找(要求掌握)
# driver.find_element_by_class_name('s_ipt')
# driver.find_element(By.CLASS_NAME,'s_ipt')
#
# # find_element_by_name：根据name属性的值来查找元素
# driver.find_element_by_name('wd')
# driver.find_element(By.NAME,'wd')
#
# # find_element_by_tag_name：根据标签名来查找元素
# driver.find_element_by_tag_name('input')
# driver.find_element(By.TAG_NAME,'input')
#
# # find_element_by_xpath：根据xpath语法来获取元素
# driver.find_element_by_xpath('//*[@id="kw"]')
# driver.find_element(By.XPATH,'//*[@id="kw"]')
#
# #find_element_by_css_selector: 根据css语法来获取元素
# driver.find_element_by_css_selector("#kw")
# driver.find_element(By.CSS_SELECTOR("#kw"))

# 练习
# from selenium import webdriver
# import time  # 时间模块
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com/")
# print(driver.find_elements(By.ID,"kw"))
# time.sleep(3)
# driver.close() # 关闭当前网页
# driver.quit() # 关闭所有网页
#

# 获取元素
# from selenium import webdriver
# import time  # 时间模块
# from selenium.webdriver.common.by import By
# from lxml import etree
# driver = webdriver.Chrome()
# driver.get("https://movie.douban.com/top250")
# 只能提取标签，不支持text()语法,否则报错
# span = driver.find_elements(By.XPATH,'//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]')
# # print(span)
# for i in span:
#     # 提取文本
#     print(i.text)
#     break

# a_tag = driver.find_elements(By.XPATH,'//div[@class="article"]/ol/li/div/div[2]/div[1]/a')
# for i in a_tag:
#     print(i.get_attribute("href"))
#     break
# 获取源代码
# print(driver.page_source)
# time.sleep(3)
# driver.close() # 关闭当前网页
# driver.quit() # 关闭所有网页

# 执行js
from selenium import webdriver
import time  # 时间模块
from selenium.webdriver.common.by import By
from lxml import etree
driver = webdriver.Chrome()
driver.get("https://bj.lianjia.com/zufang")
for i in range(2):
    # 解析数据
    # etree.HTML(driver.page_source).xpath('')
    while True:
        # document.body.scrollHeight 获取高度
        h1 = driver.execute_script('return document.body.scrollHeight;')
        # 滑倒window.scrollTo(0.6857)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        #js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight'
        # print(he)
        time.sleep(2)
        h2 = driver.execute_script('return document.body.scrollHeight;')
        if h1 == h2:
            break
    driver.find_element_by_xpath('//a[text()="下一页"]').click()
time.sleep(3)
driver.close() # 关闭当前网页
driver.quit() # 关闭所有网页

# 操作表单元素
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time  # 时间模块
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.17sucai.com/pins/demo-show?id=5926")
driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="iframe"]'))  #  切换
st = driver.find_element(By.XPATH,'/html/body/div[2]/form/fieldset[1]/div[1]/span[1]/select')
time.sleep(2)
select = Select(st)
print(select)
# select.select_by_value("JP")
# select.select_by_index(4)
# select.select_by_visible_text("Japan")
# time.sleep(3)
# driver.close() # 关闭当前网页
# driver.quit() # 关闭所有网页








