import asyncio

import requests
from lxml import etree
from threading import Thread #线程模块
import os
import time
import aiohttp

dirName = 'imgLibs'

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }



async def get_img_data(dic):
    img_src = dic['img_src']
    title = dic['img_title']
    async with aiohttp.ClientSession() as req:
        async with await req.get(img_src, headers=headers) as response:
            img_data = await response.read()
            return [img_data, title]

def saveImgData(x):
    data_list = x.result()
    img_data = data_list[0]
    title = data_list[1]
    img_path = dirName +'/' + title
    with open(img_path, 'wb') as fp:
        fp.write(img_data)
    print(title, ': 下载保存成功！')

if __name__ == '__main__':
    all_img_data = []
    url = 'https://www.pkdoutu.com/'
    start = time.time()
    if not os.path.exists(dirName):
        os.mkdir(dirName)

    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    a_list = tree.xpath('//*[@id="home"]/div/div[2]/div[2]/ul/li/div[2]/div/a')
    for a in a_list:
        img_src = a.xpath('./img/@data-original')[0]
        img_title = img_src.split('/')[-1]
        dic = {
            'img_src':img_src,
            'img_title': img_title,
        }
        all_img_data.append(dic)
        #对图片数据进行网络请求（协程）
    tasks = []
    for dic in all_img_data:
        c = get_img_data(dic)
        task = asyncio.ensure_future(c)
        task.add_done_callback(saveImgData)
        tasks.append(task)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))

    print('总耗时：', time.time()-start)


