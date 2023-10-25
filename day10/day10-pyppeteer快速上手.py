import asyncio
from pyppeteer import launch
from lxml import etree

#第一次运行程序，会给你安装Chromium这个浏览器，因此运行时间会比较久
async def main():
    browser = await launch(headless=False, devtools=True, args=['--disable-infobars'])
    page = await browser.newPage()
    await page.goto('http://quotes.toscrape.com/js/')
    page_text = await page.content()
    tree = etree.HTML(page_text)
    div_list = tree.xpath('//div[@class="quote"]')
    print(len(div_list))
    await asyncio.sleep(3)
    await browser.close()

c = main()
loop = asyncio.get_event_loop()
loop.run_until_complete(c)