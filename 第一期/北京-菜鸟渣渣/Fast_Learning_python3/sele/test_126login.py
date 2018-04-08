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


class Test126login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://mail.126.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_126login(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.switch_to_frame('x-URS-iframe')
        driver.find_element_by_id("idInput").clear()
        driver.find_element_by_id("idInput").send_keys("zhzxweijing")
        driver.find_element_by_id("pwdInput").clear()
        driver.find_element_by_id("pwdInput").send_keys("13469619523weiye")
        driver.find_element_by_id("loginBtn").click()
        try:
            self.assertEqual("zhzxweijing@126.com", driver.find_element_by_id("spnUid").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        # ERROR: Caught exception [unknown command []]

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
    unittest.main()
