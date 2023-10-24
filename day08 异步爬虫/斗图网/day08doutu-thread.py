import requests
from lxml import etree
from threading import Thread #线程模块
import os
import time

dirName = 'imgLibs'

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

#对一张图片数据进行下载
def get_img_data(url, title):
    print('正在请求：',title)
    img_data = requests.get(url=url, headers=headers).content
    img_path = dirName+'/'+title
    with open(img_path, 'wb') as fp:
        fp.write(img_data)


if __name__ == '__main__':
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

        #图片下载可以基于多线程来实现
        thread = Thread(target=get_img_data, args=(img_src, img_title))
        thread.start()


    print('总耗时：', time.time()-start)


