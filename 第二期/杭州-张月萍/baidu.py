# -*- coding: utf-8 -*-
# __author__ = 'Carina'


from selenium import webdriver
from selenium.webdriver import phantomjs
from selenium.webdriver.common.keys import Keys
import time

# 获取浏览器对象
driver = webdriver.PhantomJS("G:/Program Files (x86)/Python/Scripts/phantomjs-2.1.1-windows/bin/phantomjs.exe")

# 发送数据请求
url = "http://www.baidu.com"
driver.get(url)
time.sleep(1)
# 截屏获取浏览器页面
driver.save_screenshot("baidu.png")
driver.get("http://www.youku.com")
driver.save_screenshot("youku.png")
driver.back()
driver.save_screenshot("baidu2.png")
driver.forward()
driver.save_screenshot("youku2.png")

# 打印网页代码
#print(driver.page_source)

# 获取百度输入框
# 源码<input type="text" class="s_ipt" name="wd" id="kw" maxlength="100" autocomplete="off">
# 通过id定位
inputid = driver.find_element_by_id("kw")
# 通过name属性定位
iuputname = driver.find_element_by_name("wd")
# 通过class属性定位
inputclass = driver.find_element_by_class_name("s_ipt")
# 通过标签属性定位
inputtagname = driver.find_element_by_tag_name("input")
# 通过css方式定位
inputcss = driver.find_element_by_css_selector("#kw")
# 通过xpath方式定位
inputxpath = driver.find_element_by_xpath("//*[@id='kw']")
# 获取标签的类型
print(inputid.tag_name)

driver.save_screenshot("baidu2.png")

# 输入关键字
inputid.send_keys("python")
# 通过回车进行查询操作
inputid.send_keys(Keys.RETURN)
inputid.send_keys(Keys.ENTER)
# 暂停2秒，获取数据
#time.sleep(2)
#driver.set_page_load_timeout(2)
driver.save_screenshot("baidu3.png")
# 全选输入框内容
inputid.send_keys(Keys.CONTROL, "a")
driver.save_screenshot("baidu4.png")
# 剪切输入框内容
inputid.send_keys(Keys.CONTROL, "x")
driver.save_screenshot("baidu5.png")

# 获取查询按钮
button = driver.find_element_by_id("su")
# 点击按钮
button.click()
time.sleep(1)
# 截屏查看数据
driver.save_screenshot("baidu.png")

# 获取cookie
print(driver.get_cookie())
# 获取当前访问的URL
print(driver.current_url)
# 获取网页标题
print(driver.title)

# 关闭页面
driver.close()
# 关闭浏览器
driver.quit()