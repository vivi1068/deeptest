#coding=utf-8

import logging

from selenium.webdriver.common.by import By

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")

import  time
from selenium import webdriver
import os

if __name__ != '__main__':

    #引入chromedriver.exe
    chromedriver = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    browser = webdriver.Chrome()

    #设置浏览器需要打开的url
    url = "http://www.baidu.com"
    browser.get(url)

    #在百度搜索框中输入关键字"python"
    browser.find_element_by_id("kw").send_keys("python")
    #单击搜索按钮
    browser.find_element_by_id("su").click()

    #关闭浏览器
    #browser.quit()

class Account(object):
    def __init__(self,username="",password=""):

        self.username=username
        self.password=password
def do_login_as(user_info):

    print(user_info.username)
    print(user_info.password)

admin=Account(username="zhansan",password="123455")
do_login_as(admin)



if __name__ == '__main__':
    pass
    # driver=webdriver.Chrome()
    # driver.get("http://www.baidu.com")
    # driver.find_element(By.ID,"kw").send_keys("Selenium2")
    # driver.find_element_by_id('su').click()
    # time.sleep(1000)
    # driver.quit()