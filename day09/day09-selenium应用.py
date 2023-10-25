from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#1.创建一个浏览器对象（打开一个浏览器）
bro = webdriver.Chrome()

#2.基于浏览器进行网络请求
bro.get('https://www.jd.com')
time.sleep(1)
#3.进行相关的标签定位
# search_box = bro.find_element_by_xpath('//*[@id="key"]')
search_box = bro.find_element(By.XPATH, '//*[@id="key"]')
search_box.send_keys('mac pro m1')
btn = bro.find_element(By.XPATH, '//*[@id="search"]/div/div[2]/button')
btn.click()
time.sleep(2)
#向下滑动滚轮：js
bro.execute_script('document.documentElement.scrollTo(0,2000)')
time.sleep(3)
bro.quit()