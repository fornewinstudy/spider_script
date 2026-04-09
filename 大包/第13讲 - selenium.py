# from selenium import webdriver
# import time  # 时间模块
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com/")
#
# # # driver.find_element_by_id("kw").send_keys("小姐姐")
# kw = driver.find_element(By.ID,"kw")
# kw.send_keys("小姐姐")
# kw.clear() # 删除send_keys("小姐姐")里面的内容
# kw.send_keys("小哥哥")   # 重新输入内容
#
# # # driver.find_element_by_id("su").click()
# driver.find_element(By.ID,"su").click()
#
# print(driver.current_url)
#
# time.sleep(3)
# driver.close() # 关闭当前网页
# driver.quit() # 关闭所有网页


# 鼠标行为链
# from selenium.webdriver import ActionChains
# from selenium import webdriver
# import time  # 时间模块
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com/")
# kw = driver.find_element_by_id("kw")
# su = driver.find_element_by_id("su")
# # 实例化鼠标行为链对象
# ac = ActionChains(driver)
# ac.move_to_element(kw) # move_to_element() 移动到
# ac.send_keys("小姐姐")  # send_keys() 输入
# ac.click(su)   # 点击
# # 注意一定要记得提交，不然不会执行
# ac.perform() # 提交
#
# time.sleep(3)
# driver.close() # 关闭当前网页
# driver.quit() # 关闭所有网页


# 滑块案例 - >>12306登入
# from selenium.webdriver import ActionChains
# from selenium import webdriver
# import time  # 时间模块
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get('https://kyfw.12306.cn/otn/resources/login.html')
# time.sleep(2)
# driver.find_element_by_id('J-userName').send_keys("123456")
# time.sleep(2)
# driver.find_element_by_id('J-password').send_keys("123456")
# time.sleep(1)
# driver.find_element_by_id('J-login').click()
# # 要等待滑块加载
# time.sleep(3)
#
# ac = ActionChains(driver)
# ac.click_and_hold(driver.find_element_by_id('nc_1_n1z'))
# ac.move_by_offset(400,0)  # 移到
# ac.release()  # 鼠标释放
# ac.perform()

# 页面等待
# 隐示等待
# from selenium import webdriver
# import time  # 时间模块
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com/")
# driver.find_element(By.ID,"kw").send_keys("小姐姐")
# driver.implicitly_wait(10)  # selenium自带的等待
# driver.find_element(By.ID,"su").click()
# print("执行完毕了")

# 显示等待
# from selenium import webdriver
# import time  # 时间模块
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com/")
# # 实例化等待对象
# # 方法一
# driver.find_element(By.ID,"kw").send_keys("小姐姐")
# wt = WebDriverWait(driver, 10)
# wt.until(
#     EC.presence_of_element_located((By.ID,'su')) # 表示某个元素已经加载完毕了，里面的定位是以一个元组来写的
# ) # 等待对象
# driver.find_element(By.ID,"su").click()
# print("执行完毕了")
# # 方法二
# driver.find_element(By.ID,"kw").send_keys("小姐姐")
# wt = WebDriverWait(driver, 10)
# until(
#  EC.presence_of_element_located((By.ID,'su'))
# )
# wt.click()
# print("执行完毕了")


# 获取cookie的操作
# from selenium.webdriver import ActionChains
# from selenium.webdriver.support.ui import Select
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import requests
# import time
# driver = webdriver.Chrome()
# driver.get("https://xui.ptlogin2.qq.com/cgi-bin/xlogin?proxy_url=https%3A//qzs.qq.com/qzone/v6/portal/proxy.html&daid=5&&hide_title_bar=1&low_login=0&qlogin_auto_login=1&no_verifyimg=1&link_target=blank&appid=549000912&style=22&target=self&s_url=https%3A%2F%2Fqzs.qzone.qq.com%2Fqzone%2Fv5%2Floginsucc.html%3Fpara%3Dizone&pt_qr_app=手机QQ空间&pt_qr_link=http%3A//z.qzone.com/download.html&self_regurl=https%3A//qzs.qq.com/qzone/v6/reg/index.html&pt_qr_help_link=http%3A//z.qzone.com/download.html&pt_no_auth=0")
# driver.implicitly_wait(60)
# driver.find_element_by_id('tab_menu_friend').click()
# time.sleep(3)
# cook = driver.get_cookies()
# # # print(cook)
# cook1 = ";".join([ i["name"]+ "=" +i["value"] for i in cook]) # 获取cookie
# headers = {
#     # 登入界面的ua
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
#     "cookie":cook1
# }
#                             # url 登入进去里面的url
# response = requests.get(url="https://user.qzone.qq.com/3351932344", headers=headers)
# with open("qq.html", "w",encoding="utf-8") as a:
#     a.write(response.content.decode("utf-8"))
#
#
# time.sleep(3)
# driver.close() # 关闭当前网页
# driver.quit() # 关闭所有网页

# 页面切换
# from selenium.webdriver import ActionChains
# from selenium.webdriver.support.ui import Select
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import requests
# import time
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com/')
# time.sleep(2)
# # driver.get("https://www.yuque.com/") 这样会覆盖
# driver.execute_script("window.open('https://www.yuque.com/')")
# driver.switch_to.window(driver.window_handles[1])
# print('操作')
# time.sleep(2)
# driver.close()
# driver.switch_to.window(driver.window_handles[0])
# time.sleep(2)
# driver.execute_script("window.open('https://www.sogou.com/')")
# time.sleep(3)
# # print(driver.current_url) # 查看当前网页的url
# # print(driver.page_source) # 查看当前网页的url
# # 获取到窗口对象
# win = driver.window_handles
# # print(win,type(win))
# driver.switch_to.window(win[1])
# time.sleep(3)
# print(driver.current_url)
# driver.close()
# driver.quit()


# 练习题
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
driver = webdriver.Chrome()
driver.get("https://nc.lianjia.com/ershoufang/")
a_tge_list = driver.find_element(By.XPATH,'//ul[@class="sellListContent"]/li/a')
while True:
    for a_tag in a_tge_list:
        time.sleep(2)
        # 元素被挡无法点击
        # 方法一 js
        # driver.execute_script('arguments[0].click()',a_tag)
        # 方法二 滑动元素至可见
        driver.execute_script('arguments[0].scrollIntoView()', a_tag)
        a_tag.click()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(2)
        print("获取数据")
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    try:
        driver.find_element_by_xpath('//a[text()="下一页"]').click()
    except:
        break
    driver.close()
    driver.quit()






























