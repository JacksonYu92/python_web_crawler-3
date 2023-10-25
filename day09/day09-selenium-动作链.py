from selenium.webdriver import ActionChains
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
bro = webdriver.Chrome()
bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
sleep(1)
#注意：如果定位的标签是存在于iframe表示的子页面中，则常规的标签定位报错
#处理：使用如下指定操作
bro.switch_to.frame('iframeResult')
div_tag = bro.find_element(By.ID,'draggable')

#实例化一个动作链对象且将该对象绑定到指定的浏览器中
action = ActionChains(bro)
action.click_and_hold(div_tag) #对指定标签实现点击且长按操作
for i in range(5):
    action.move_by_offset(10,10).perform() #perform让动作链立即执行
    sleep(0.5)
sleep(3)
bro.quit()