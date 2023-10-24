import asyncio
import time
import requests
from lxml import etree

import aiohttp

urls = ['http://127.0.0.1:5000/bobo', 'http://127.0.0.1:5000/jay', 'http://127.0.0.1:5000/tom']

start = time.time()
#在特殊函数内部不可以出现不支持异步的模块代码
async def get_requests(url):
    async with aiohttp.ClientSession() as req: #创建请求对象
        async with await req.get(url=url) as response: #返回一个响应对象
            page_text = await response.text() #json() read()
            return page_text

def parse(x):
    page_text = x.result()
    tree = etree.HTML(page_text)
    data = tree.xpath('//div[1]//text()')
    print(data)

tasks = [] # 存放所有的任务对象
for url in urls:
    c = get_requests(url) # 创建了3个协程对象
    task = asyncio.ensure_future(c)
    task.add_done_callback(parse)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

print('总耗时：', time.time()-start)