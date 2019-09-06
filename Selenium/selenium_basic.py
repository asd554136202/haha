# import time
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# url = 'https://www.baidu.com'
# driver.get(url)
# time.sleep(5)
# driver.quit()
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
url = 'https://www.baidu.com'
driver.get(url)
ele = driver.find_element_by_link_text('更多产品')
ActionChains(driver).move_to_element(ele).perform()
driver.find_element_by_xpath('//*[@id="head"]/div/div[4]/div/div[2]/div[1]/div/a[2]').click()




