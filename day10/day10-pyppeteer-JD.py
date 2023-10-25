import random
from pyppeteer import launch
import asyncio
import cv2
from urllib import request


async def get_track():
    background = cv2.imread("background.png", 0)
    gap = cv2.imread("gap.png", 0)

    res = cv2.matchTemplate(background, gap, cv2.TM_CCOEFF_NORMED)
    value = cv2.minMaxLoc(res)[2][0]
    print(value)
    return value * 270 / 360


async def main():
    browser = await launch({
        # headless指定浏览器是否以无头模式运行，默认是True。
        "headless": False,
        # 设置窗口大小
        "args": ['--window-size=1366,768'],
    })
    # 打开新的标签页
    page = await browser.newPage()
    # 设置页面大小一致
    await page.setViewport({"width": 1366, "height": 768})
    # 访问主页
    await page.goto("https://passport.jd.com/new/login.aspx?")

    # 单击事件
    # await page.click('div.login-tab-r')
    # 模拟输入用户名和密码,输入每个字符的间隔时间delay ms
    await page.type("#loginname", '324534534@qq.com', {
        "delay": random.randint(30, 60)
    })
    await page.type("#nloginpwd", '345653332', {
        "delay": random.randint(30, 60)
    })

    # page.waitFor 通用等待方式，如果是数字，则表示等待具体时间（毫秒）: 等待2秒
    await page.waitFor(2000)
    await page.click("div.login-btn")
    await page.waitFor(2000)
    # page.jeval（selector，pageFunction）#定位元素，并调用js函数去执行
    # =>表示js的箭头函数：el = function(el){return el.src}
    img_src = await page.Jeval(".JDJRV-bigimg > img", "el=>el.src")
    temp_src = await page.Jeval(".JDJRV-smallimg > img", "el=>el.src")

    request.urlretrieve(img_src, "background.png")
    request.urlretrieve(temp_src, "gap.png")

    # 获取gap的距离
    distance = await get_track()
    """
        # Pyppeteer 三种解析方式
        Page.querySelector()  # 选择器
        Page.querySelectorAll()
        Page.xpath()  # xpath  表达式
        # 简写方式为：
        Page.J(), Page.JJ(), and Page.Jx()
        """
    # 定位到滑动按钮标签
    el = await page.J("div.JDJRV-slide-btn")

    # 获取元素的边界框，包含x,y坐标
    box = await el.boundingBox()
    # box={'x': 86, 'y': 34, 'width': 55.0, 'height': 55.0}
    # 将鼠标悬停/一定到指定标签位置
    await page.hover("div.JDJRV-slide-btn")
    # 按下鼠标
    await page.mouse.down()
    # 模拟人的行为进行滑动
    # steps 是指分成几步来完成，steps越大，滑动速度越慢
    # move(x,y)表示将鼠标移动到xy坐标位置
    #random.uniform生成一个在指定范围内的随机浮点数
    await page.mouse.move(box["x"] + distance + random.uniform(10, 30),
                          box["y"], {"steps": 100})
    await page.waitFor(1000)

    await page.mouse.up()
    await page.waitFor(2000)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
