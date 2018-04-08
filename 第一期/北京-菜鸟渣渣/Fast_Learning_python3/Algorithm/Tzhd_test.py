import time
import os
from selenium import webdriver
# def TianjiahuodongTest():
driver = webdriver.Chrome()
driver.get('http://uat.haokeduo.com')
time.sleep(3)
driver.find_element_by_class_name('login_btn').click()
time.sleep(3)
driver.find_element_by_name('tel').send_keys('13450055555')
driver.find_element_by_name('pw').send_keys('w123456')
time.sleep(3)
driver.find_element_by_class_name('e_btn').click()
time.sleep(3)
driver.find_element_by_class_name('dis_inb').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[6]/div/div[3]').click()
time.sleep(3)
# 营销管理
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[3]/div[1]/ul/li[4]/a/span[1]').click()
time.sleep(1)
# 营销活动
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[3]/div[1]/ul/li[4]/ul/li/a').click()
time.sleep(1)
# 添加活动
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[4]/div/div/div/div[1]/div[1]/a').click()
time.sleep(2)
# 线上活动
# driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[4]/div/div/div/div[1]/div[3]/div[1]/div[2]/label[2]/span').click()
# 线下活动
driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/div[1]/div[4]/div/div/div/div[1]/div[3]/div[1]/div[2]/label[1]/span').click()
time.sleep(2)
'''
#限购  默认不限购
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[4]/div/div/div/div[1]/div[3]/div[2]/div[2]/label[2]/span').click()
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[4]/div/div/div/div[1]/div[3]/div[2]/div[3]/input').clear()
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[4]/div/div/div/div[1]/div[3]/div[2]/div[3]/input').send_keys('3')
time.sleep(2)
'''
# 活动分类
driver.find_element_by_class_name('tx_unbr').click()
time.sleep(1)
driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/div[1]/div[4]/div/div/div/div[1]/div[3]/div[3]/div[2]/div/a[5]').click()
time.sleep(1)
# 活动名称

driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/div[1]/div[4]/div/div/div/div[1]/div[3]/div[4]/input').send_keys('3')

driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/div[1]/div[4]/div/div/div/div[1]/div[3]/div[5]/div[2]/div/input[1]').send_keys('3')
driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/div[1]/div[4]/div/div/div/div[1]/div[3]/div[5]/div[2]/div/input[2]').send_keys('3')
driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/div[1]/div[4]/div/div/div/div[1]/div[3]/div[6]/input').send_keys('17316227114')

# # 单一规格 原价
# driver.find_element_by_xpath(
#     '/html/body/div[1]/div/div/div[1]/div[4]/div/div/div/div[1]/div[5]/div[1]/div[3]/table/tbody/tr/td[1]/input').send_keys(
#     '3')
# # 现价
# driver.find_element_by_xpath(
#     '/html/body/div[1]/div/div/div[1]/div[4]/div/div/div/div[1]/div[5]/div[1]/div[3]/table/tbody/tr/td[1]/input').send_keys(
#     '3')
# # 售卖价（元）
# driver.find_element_by_xpath(
#     '/html/body/div[1]/div/div/div[1]/div[4]/div/div/div/div[1]/div[5]/div[1]/div[3]/table/tbody/tr/td[2]/input').send_keys(
#     '3')
# # 库存
# driver.find_element_by_xpath(
#     '/html/body/div[1]/div/div/div[1]/div[4]/div/div/div/div[1]/div[5]/div[1]/div[3]/table/tbody/tr/td[3]/input').send_keys(
#     '3')
# time.sleep(2)
# 多规格 规格名称
target = driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/div[1]/div[4]/div/div/div/div[1]/div[5]/div[1]/div[2]/label[2]/span')
driver.execute_script("arguments[0].scrollIntoView();", target)

# js="var q=document.getElementById('id').scrollTop=0"
# driver.execute_script(js）

driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/div[1]/div[4]/div/div/div/div[1]/div[5]/div[1]/div[2]/label[2]/span').click()
time.sleep(3)
# 添加规格 @1
driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/div[1]/div[4]/div/div/div/div[1]/div[5]/div[1]/div[4]/table/tbody/tr/td[8]/a').click()
# 添加规格 @2
time.sleep(1)
driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/div[1]/div[4]/div/div/div/div[1]/div[5]/div[1]/div[4]/table/tbody/tr[1]/td[8]/a[1]').click()
time.sleep(1)
driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/div[1]/div[4]/div/div/div/div[1]/div[5]/div[1]/div[4]/table/tbody/tr/td[1]/input').send_keys(
    '3')

# 原价
driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/div[1]/div[4]/div/div/div/div[1]/div[5]/div[1]/div[4]/table/tbody/tr/td[2]/input').send_keys(
    '3')

# 售卖价（元）
driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/div[1]/div[4]/div/div/div/div[1]/div[5]/div[1]/div[4]/table/tbody/tr/td[3]/input').send_keys(
    '3')

# 库存
driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/div[1]/div[4]/div/div/div/div[1]/div[5]/div[1]/div[4]/table/tbody/tr/td[4]/input').send_keys(
    '3')

# # 删除规格@1
# driver.find_element_by_xpath(
#     '/html/body/div[1]/div/div/div[1]/div[4]/div/div/div/div[1]/div[5]/div[1]/div[4]/table/tbody/tr[1]/td[8]/a[2]').click()
# # 删除规格@2
# driver.find_element_by_xpath(
#     '/html/body/div[1]/div/div/div[1]/div[4]/div/div/div/div[1]/div[5]/div[1]/div[4]/table/tbody/tr[2]/td[8]/a[2]').click()

driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/div[1]/div[4]/div/div/div/div[1]/div[5]/div[1]/div[4]/table/tbody/tr[2]/td[1]/input').send_keys(
    '3')

driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/div[1]/div[4]/div/div/div/div[1]/div[5]/div[1]/div[4]/table/tbody/tr[2]/td[2]/input').send_keys(
    '3')

driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/div[1]/div[4]/div/div/div/div[1]/div[5]/div[1]/div[4]/table/tbody/tr[2]/td[3]/input').send_keys(
    '3')

driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/div[1]/div[4]/div/div/div/div[1]/div[5]/div[1]/div[4]/table/tbody/tr[2]/td[4]/input').send_keys(
    '3')

driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/div[1]/div[4]/div/div/div/div[1]/div[5]/div[1]/div[4]/table/tbody/tr[3]/td[1]/input').send_keys(
    '3')

driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/div[1]/div[4]/div/div/div/div[1]/div[5]/div[1]/div[4]/table/tbody/tr[3]/td[2]/input').send_keys(
    '3')

driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/div[1]/div[4]/div/div/div/div[1]/div[5]/div[1]/div[4]/table/tbody/tr[3]/td[3]/input').send_keys(
    '3')

driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/div[1]/div[4]/div/div/div/div[1]/div[5]/div[1]/div[4]/table/tbody/tr[3]/td[4]/input').send_keys(
    '3')

# 购买须知
target = driver.find_element_by_id(
    'edui1_iframeholder')
driver.execute_script("arguments[0].scrollIntoView();", target)
driver.find_element_by_id('edui1_iframeholder').click()
time.sleep(1)
driver.find_element_by_id('ueditor_1').send_keys('sajdhkjahdkjhakdjh')
time.sleep(1)
# 活动时间
# @11活动时间
js = "$('input[class=start_time]').attr('readonly',’ ‘)"
driver.find_element_by_class_name('start_time').clear()

driver.find_element_by_class_name('start_time').send_keys('2017-09-30')
time.sleep(3)
# @12活动结束时间
js = "$('input[class=end_time]').attr('readonly',’ ‘)"
driver.find_element_by_class_name('end_time').clear()

driver.find_element_by_class_name('end_time').send_keys('2018-09-30')
time.sleep(3)
# @13活动报名截止
js = "$('input[class=actclosing_date]').attr('readonly',’ ‘)"
driver.find_element_by_class_name('actclosing_date').clear()

driver.find_element_by_class_name('actclosing_date').send_keys('2018-09-29')
time.sleep(5)

# 活动封面图
driver.find_element_by_class_name('j_photos').click()
time.sleep(3)
driver.find_element_by_name("file").send_keys(r'C:\Users\bj0204\Pictures\wallpaper_5243735.jpg')
# driver.find_element_by_class_name('j_photos').send_key(r'E:\zp\01\wallpaper_5243735.jpg')
time.sleep(3)
driver.find_element_by_class_name('e_btn').click()
time.sleep(3)
# 活动详情
driver.find_element_by_id('ueditor_0').click()
time.sleep(1)
driver.find_element_by_id('ueditor_0').send_keys('dsdfkdfdskdshfhshdhfkhshdfkhdskdsfhkshfkfhdsdkfhshdfds')

# 点击保存
# driver.find_element_by_class_name('save').click()
driver.find_element_by_class_name('save_submit').click()
# driver.find_element_by_class_name('cancel').click()

# driver.close()
