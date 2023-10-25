import asyncio
from pyppeteer import launch
from lxml import etree

async def requests_page():
    #创建一个浏览器对象
    bro = await launch(headless=False)
    #创建一个page
    page = await bro.newPage()
    #可以专门设置打开page的像素宽度和高度
    await page.setViewport({'width':1366, 'height':768})
    #发起请求
    await page.goto('https://www.taobao.com')

    await asyncio.sleep(3)
    await page.evaluate('window.scrollTo(0,document.body.scrollHeight)')
    await asyncio.sleep(3)
    await bro.close()

c = requests_page()
loop = asyncio.get_event_loop()
loop.run_until_complete(c)