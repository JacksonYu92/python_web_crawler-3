import asyncio
from pyppeteer import launch
from lxml import etree

urls = ['https://news.163.com/domestic/',
        'https://news.163.com/world/',
        'https://war.163.com/']

async def get_data(url):
    browser = await launch(
        headless=False,
        # chrome://version/
        executablePath='C:\Program Files\Google\Chrome\Application\chrome.exe'
    )
    page = await browser.newPage()

    await page.goto(url)
    # await asyncio.sleep(3)
    await page.waitFor(2000)
    page_text = await page.content()
    await browser.close()

    return page_text

def parse(task):
    page_text = task.result()
    tree = etree.HTML(page_text)
    div_list = tree.xpath('//div[@class="data_row news_article clearfix "]')
    for div in div_list:
        title = div.xpath('.//div[@class="news_title"]/h3/a/text()')[0]
        print(title)

tasks = []
for url in urls:
    c = get_data(url)
    task = asyncio.ensure_future(c)
    task.add_done_callback(parse)
    tasks.append(task)

asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))