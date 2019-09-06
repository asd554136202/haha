import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
url = 'D:\python\Selenium测试网页/multiple.html'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)
driver.maximize_window()
import os
driver.find_element_by_name('file').click()
time.sleep(3)
os.system('D:/ui自动化/uploadFile.exe')




# ele=driver.find_element_by_id('if')
# driver.switch_to.frame(ele)
# time.sleep(3)
# driver.find_element_by_id('kw').click()
# driver.find_element_by_id('kw').send_keys('我是你爸爸')
# driver.switch_to.default_content()
# driver.find_element_by_id('uid').send_keys('切换回来的操作')
# ele=driver.find_element_by_name('fn')
# driver.execute_script('arguments[0].removeAttribute("readonly");',ele)
# ele.send_keys('e://')

# ori_handle=driver.current_window_handle
# print(ori_handle)
# driver.find_element_by_link_text('百度').click()
# handles=driver.window_handles
# print(handles)
# for i in handles:
#     if i != ori_handle:
#         driver.switch_to.window(i)
#         driver.find_element_by_id('kw').click()
#         driver.find_element_by_id('kw').send_keys('我是你爸爸')
# driver.switch_to.window(ori_handle)
# driver.find_element_by_id('uid').send_keys('自动化测试')







# driver.find_element_by_name('b1').click()
# driver.switch_to.alert.accept()
# data=driver.switch_to.alert.text
# print(data)
# driver.switch_to.alert.send_keys('我是你爸爸')
# driver.switch_to.alert.accept()

# driver.switch_to_alert().send_keys('我是你爸爸')
# driver.switch_to_alert().accept()
from selenium.webdriver.support.ui import Select
# ele=driver.find_element_by_id('ShippingMethod')
# Select(ele).select_by_value('9.03')
# Select(ele).select_by_index(0)
# Select(ele).select_by_visible_text('UPS 3 Day Select ==> $10.69')



# driver.find_element_by_id('uid').send_keys('自动化测试')
# driver.find_element_by_id('uid').send_keys(Keys.BACK_SPACE)
# driver.find_element_by_name('pwd').click()
# driver.find_element_by_name('pwd').send_keys('这是输入到密码的内容')
# driver.find_element_by_xpath('//input[@id="uid"]').click()
# driver.find_element_by_xpath('//input[@id="uid"]').send_keys('自动化测试')
# driver.find_element_by_xpath('//*[@id="pwdid"]').click()
# driver.find_element_by_xpath('//*[@id="pwdid"]').send_keys('123456')
# driver.find_element_by_xpath('//*[@id="age"]').click()
# driver.find_element_by_xpath('//*[@id="age"]').send_keys('18')
# data=driver.find_elements_by_tag_name('a')
# print('type(data) is',type(data))
# print('长度是',len(data))
# print(data)
# data[4].click()

# data=driver.find_elements_by_class_name('control-group')
# print(type(data))
# print(len(data))
# print(data)
# driver.quit()
# ele=driver.find_element_by_id('div-id-5')
# print(ele)
# ele2=ele.find_element_by_link_text('百度').click()
# print(ele2)
# ele2.find_element_by_link_text().click()
# ele2.find_element_by_name('username').send_keys('admin')
# from selenium.webdriver.common.by import By
# username_ipt=(By.XPATH,'//*[@id="uid"]')
# driver.find_element(*username_ipt).click()
# driver.find_element(*username_ipt).send_keys('自动化测试')
#
# ele=driver.find_element_by_xpath()

# ele=driver.find_element_by_id('button_id_1')
# driver.execute_script('arguments[0].click()',ele)





