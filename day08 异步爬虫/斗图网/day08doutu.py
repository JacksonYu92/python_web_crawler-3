import requests
from lxml import etree

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
    img_path = 
    requests.get(url=a, headers=headers).content





