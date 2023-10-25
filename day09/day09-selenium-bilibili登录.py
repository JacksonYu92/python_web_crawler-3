from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep
import tujian
#1.创建浏览器对象
bro = webdriver.Chrome(executable_path='./chromedriver')
#2.发起请求
login_url = 'https://passport.bilibili.com/login?from_spm_id=333.851.top_bar.login_window'
bro.get(login_url)
sleep(1)
#3.定位到指定标签填充用户名和密码
user_box = bro.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/input')
user_box.send_keys('15027900535')
sleep(1)
pwd_box = bro.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[3]/div[2]/div[1]/div[3]/input')
pwd_box.send_keys('123456')
sleep(1)
login_btn = bro.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]')
login_btn.click()
sleep(10)
#4.定位完整的验证码对话框
#注意：在开发者工具中是可以定位到多个div表示验证码对话框的，因此将这几个div都定位到，以此去尝试
code_tag = bro.find_element_by_xpath('/html/body/div[4]/div[2]/div[6]/div/div')
sleep(1)
#5.识别验证码（使用打码平台进行验证码识别）
code_tag.screenshot('./code.png')#将验证码对话框截图保存
sleep(1)
#使用图鉴接口识别
result = tujian.getImgCodeText('./code.png',27)#获取了识别的结果
# result = '154,251|145,167'
# print(result)
result_list = result.split('|')
#result_list == ['154,251','145,167']
#6.根据识别出验证码的结果进行处理
for pos in result_list:
    x = int(pos.split(',')[0])
    y = int(pos.split(',')[1])
    ActionChains(bro).move_to_element_with_offset(code_tag,x,y).click().perform()
    sleep(0.5)
sleep(2)
#此处使用class属性进行确定标签定位
confirm_btn = bro.find_element_by_xpath('//a[@class="geetest_commit"]')
confirm_btn.click()
sleep(3)
bro.quit()