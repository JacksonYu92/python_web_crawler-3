import requests
from lxml import etree
import os
import aiohttp
import asyncio

dirName = 'imgLibs'
if not os.path.exists(dirName):
    os.mkdir(dirName)

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

# 爬取多页的图片链接，将其存储起来，然后准备后面的异步图片爬取
def get_img_msg():
    img_msg = [] #存储图片相关信息

    url = 'https://www.pkdoutu.com/'
    page_text = requests.get(url,headers=headers).text
    tree = etree.HTML(page_text)
    a_alist = tree.xpath('//*[@id="home"]/div/div[2]/div[2]/ul/li/div[2]/div/a')
    for a in a_alist:
        #图片是滑动滚轮后单独加载出来的（图片懒加载）
        img_src = a.xpath('./img/@data-original')[0]
        img_title = img_src.split('/')[-1]
        dic = {}
        dic['img_url'] = img_src
        dic['img_title'] = img_title
        img_msg.append(dic)
    return img_msg

async def get_request(dic):
    async with aiohttp.ClientSession() as sess:
        async with await sess.get(url=dic['img_url']) as response:
            img_data = await response.read()
            dic['img_data'] = img_data
            return dic

#任务对象回调函数：用来进行图片的持久化存储
def saveImg(task):
    dic = task.result()
    img_path = dirName+'/'+dic['img_title']
    with open(img_path, 'wb') as fp:
        fp.write(dic['img_data'])
    print(dic['img_title'], '：爬取保存成功！')


if __name__ == '__main__':
    img_msg = get_img_msg()
    tasks = []
    for dic in img_msg:
        c = get_request(dic)
        task = asyncio.ensure_future(c)
        task.add_done_callback(saveImg)
        tasks.append(task)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))