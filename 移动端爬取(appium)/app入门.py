from appium import webdriver

caps = dict()
# 配置连接参数
# 测试的系统
caps['platformName'] = 'Android'
# 手机安卓的版本
caps['platformVersion'] = '5.1.1'
# 设备名字 不重要
caps['deviceName'] = 'Android'
# 包名
caps['appPackage'] = 'com.android.browser'
# 界面名
caps['appActivity'] = '.BrowserActivity'
# 如果有需要输入中文 设置为True
caps['unicodeKeyboard'] = True
# 恢复原来的输入法
caps['resetKeyboard'] = True
# 一般来说 不需要重置app状态 设置为True
caps['noReset'] = True


# 加载驱动
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)

driver.get('https://www.baidu.com/')

