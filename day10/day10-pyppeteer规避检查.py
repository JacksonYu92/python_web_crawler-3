import asyncio
from pyppeteer import launch

width, height = 1366,768

async def main():
    #创建一个浏览器对象
    browser = await launch(headless=False, args=['--disable-infobars'])
    #创建一个page
    page = await browser.newPage()
    #可以专门设置打开page的像素宽度和高度
    await page.setViewport({'width':width, 'height':height})
    #发起请求
    await page.goto('https://login.taobao.com/member/login.jhtml?redirectURL=https://www.taobao.com/')
    #规避检测
    await page.evaluate('''() => { Object.defineProperties(navigator, { webdriver:{ get: () => false } }) }''')
    await asyncio.sleep(20)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())