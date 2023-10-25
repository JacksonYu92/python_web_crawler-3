from selenium import webdriver
import time
from lxml import etree
from selenium.webdriver.common.by import By

# 后面是你的浏览器驱动位置，记得前面加r'','r'是防止字符转义的
driver = webdriver.Chrome()
#2. 基于浏览器进行网络请求
driver.get("https://movie.douban.com/typerank?type_name=%E6%82%AC%E7%96%91&type=10&interval_id=100:90&action=")
time.sleep(1)
#获取当前页面的页面源码数据
page_text = driver.page_source

tree = etree.HTML(page_text)
ret = tree.xpath('//*[@id="content"]/div/div[1]/div[6]/div/div/div/div[1]/span[1]/a/text()')
print(ret)
driver.quit()