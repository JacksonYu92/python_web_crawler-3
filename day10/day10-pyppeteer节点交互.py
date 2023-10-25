import asyncio
from pyppeteer import launch


async def main():
    # headless参数设为False，则变成有头模式
    browser = await launch(
        headless=False,
        #chrome://version/
        executablePath='C:\Program Files\Google\Chrome\Application\chrome.exe'
    )
    page = await browser.newPage()
    # 设置页面视图大小
    await page.setViewport(viewport={'width': 1280, 'height': 800})

    await page.goto('https://www.baidu.com/')

    await page.type('#kw', 'Jay', {'delay':2000})

    await page.click('#su')
    await asyncio.sleep(2)

    #单独进行标签定位
    tag_list = await page.querySelectorAll('.s_tab_inner > a')
    tag = tag_list[0]
    await tag.click()
    await asyncio.sleep(2)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())