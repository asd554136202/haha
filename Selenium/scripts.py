from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'http://localhost/admin.php'
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(10)
driver.maximize_window()
driver.find_element_by_id('username').click()
driver.find_element_by_id('username').send_keys('admin')
driver.find_element_by_id('password').click()
driver.find_element_by_id('password').send_keys('admin')
driver.find_element_by_xpath('//*[@id="loginFrm"]/input').click()
driver.find_element_by_xpath('//*[@id="header"]/ul/li[3]/a').click()
# driver.find_element_by_xpath('/html/body/div[2]/h3/a[2]/span').click()

driver.find_element_by_xpath('//*[@id="side-menu"]/div[3]/ul/li[2]/a').click()
# 转到iframe内
ele = driver.find_element_by_id('mainframe')
driver.switch_to.frame(ele)

driver.find_element_by_xpath('/html/body/div[2]/h3/a[2]/span').click()
driver.find_element_by_name('username').click()
driver.find_element_by_name('username').send_keys('18806643211')
driver.find_element_by_name('realname').click()
driver.find_element_by_name('realname').send_keys('admin')
driver.find_element_by_name('password').click()
driver.find_element_by_name('password').send_keys('123456')
from selenium.webdriver.support.ui import Select

ele = driver.find_element_by_name('roleid')

Select(ele).select_by_index(3)
ele1 = driver.find_element_by_name('orid1')
Select(ele1).select_by_index(2)
driver.find_element_by_id('email').click()
driver.find_element_by_id('email').send_keys('554136202@qq.com')
driver.find_element_by_id('phone').click()
driver.find_element_by_id('phone').send_keys('18806643211')
driver.find_element_by_xpath('//*[@id="btn_sub"]/span').click()
time.sleep(5)
# 弹出确认成功框
driver.switch_to.alert.accept()
# 返回列表确认是否添加成功
driver.find_element_by_xpath('/html/body/div[2]/h3/a/span').click()
# 获取标签的文本值
data = driver.find_element_by_xpath('//*[@id="recordList"]/tr[1]/td[2]/div/a').text
if data == '13800000003':
    print('测试成功')
    driver.quit()
else:
    print('测试失败')



