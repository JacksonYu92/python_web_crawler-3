from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# 后面是你的浏览器驱动位置，记得前面加r'','r'是防止字符转义的
driver = webdriver.Chrome()
# 用get打开百度页面
driver.get("http://www.baidu.com")

# 查找页面的“设置”选项，并进行点击
# driver.find_element_by_xpath('//*[@id="s-usersetting-top"]').click()
driver.find_element(By.XPATH,'//*[@id="s-usersetting-top"]').click()


sleep(1)
# # 打开设置后找到“搜索设置”选项，设置为每页显示50条
# driver.find_elements_by_link_text('搜索设置')[0].click()
driver.find_element(By.LINK_TEXT,'搜索设置').click()
sleep(1)

# 选中每页显示50条
m = driver.find_element_by_xpath('//*[@id="nr_3"]').click()
sleep(1)

# 点击保存设置
driver.find_element_by_xpath('//*[@id="se-setting-7"]/a[2]').click()
sleep(1)

# 处理弹出的警告页面   确定accept() 和 取消dismiss()
driver.switch_to.alert.accept()
sleep(1)
# 找到百度的输入框，并输入 美女
driver.find_element_by_id('kw').send_keys('美女')
sleep(1)
# 点击搜索按钮
driver.find_element_by_id('su').click()
sleep(1)
driver.find_element_by_xpath('//*[@id="1"]/div/h3/a').click()
sleep(3)

# 关闭浏览器
driver.quit()