import time
from selenium import webdriver
from selenium.webdriver.common.by import By  # 按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait  # 等待页面加载某些元素
import cv2 #pip install opencv-python

from urllib import request
from selenium.webdriver.common.action_chains import ActionChains


#获取要滑动的距离
def get_distance():
    #滑动验证码的整体背景图片
    background = cv2.imread("background.png", 0)
    #缺口图片
    gap = cv2.imread("gap.png", 0)

    res = cv2.matchTemplate(background, gap, cv2.TM_CCOEFF_NORMED)
    value = cv2.minMaxLoc(res)[2][0]
    print(value)
    #单位换算
    return value * 248 / 360


def main():
    chrome = webdriver.Chrome()
    chrome.implicitly_wait(5)

    chrome.get('https://passport.jd.com/new/login.aspx?')

    # login = chrome.find_element(By.CLASS_NAME, 'login-tab-r')
    # login.click()

    loginname = chrome.find_element(By.ID, 'loginname')
    loginname.send_keys("123@qq.com")

    nloginpwd = chrome.find_element(By.ID, 'nloginpwd')
    nloginpwd.send_keys("987654321")

    loginBtn = chrome.find_element(By.CLASS_NAME, 'login-btn')
    loginBtn.click()
		#带缺口的大图
    img_src = chrome.find_element(By.XPATH, '//*[@class="JDJRV-bigimg"]/img').get_attribute("src")
    #缺口图片
    temp_src = chrome.find_element(By.XPATH, '//*[@class="JDJRV-smallimg"]/img').get_attribute("src")
    #两张图片保存起来
    request.urlretrieve(img_src, "background.png")
    request.urlretrieve(temp_src, "gap.png")

    distance = int(get_distance())
    print("distance:", distance)

    print('第一步,点击滑动按钮')
    element = chrome.find_element(By.CLASS_NAME, 'JDJRV-slide-btn')
    ActionChains(chrome).click_and_hold(on_element=element).perform()  # 点击鼠标左键，按住不放

    ActionChains(chrome).move_by_offset(xoffset=distance, yoffset=0).perform()
    ActionChains(chrome).release(on_element=element).perform()

    time.sleep(2)
if __name__ == '__main__':
    main()
