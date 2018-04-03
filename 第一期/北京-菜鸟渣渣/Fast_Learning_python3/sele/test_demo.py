#coding=utf-8

import logging

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Testdemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_demo(self):
        driver = self.driver
        driver.get(
            self.base_url + "/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E6%9B%B2%E7%BB%88%E4%BA%BA%E6%95%A3&oq=%25E6%259B%25B2%25E7%25BB%2588%25E4%25BA%25BA%25E6%2595%25A3&rsv_pq=b6d9724c00058d0b&rsv_t=4921zy8y6zG%2FLE1S4N6I1rNYbFBIFk8ur3bplcToTJc7J%2BMPQJcY1rzwpVY&rqlang=cn&rsv_enter=0&inputT=7&rsv_sug3=5&rsv_sug1=4&rsv_sug7=100&rsv_sug2=0&rsv_sug4=723&rsv_sug=1")
        driver.find_element_by_id("su").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'曲终人散歌词')])[2]").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    # unittest.main()
    pass