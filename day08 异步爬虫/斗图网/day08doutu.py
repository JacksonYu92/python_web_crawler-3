import requests
from lxml import etree
import os
import time

dirName = 'imgLibs'
if not os.path.exists(dirName):
    os.mkdir(dirName)
start = time.time()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}
url = 'https://www.pkdoutu.com/'

page_text = requests.get(url=url, headers=headers).text

tree = etree.HTML(page_text)
# tree.xpath('//*[@id="home"]/div/div[2]/div[2]')
a_list = tree.xpath('//*[@id="home"]/div/div[2]/div[2]/ul/li/div[2]/div/a')
for a in a_list:
    img_src = a.xpath('./img[2]/@data-original')[0]
    img_title = img_src.split('/')[-1]
    img_path = dirName+'/'+img_title
    img_data = requests.get(url=img_src, headers=headers).content
    with open(img_path, 'wb') as fp:
        fp.write(img_data)
    print(img_title, ':爬取保存成功！')

print('总耗时：', time.time()-start)


