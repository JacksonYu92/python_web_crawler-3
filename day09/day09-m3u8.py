import requests
from urllib.parse import urljoin
import re
import os
dirName = 'tsLib'
if not os.path.exists(dirName):
    os.mkdir(dirName)

headers  = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}
#一级m3u8地址
m1_url = "https://c2.monidai.com/20230415/7Z6l3a9h/index.m3u8"
m1_page_text = requests.get(url=m1_url,headers=headers).text
#从一级m3u8文件中解析出二级m3u8地址
m1_page_text = m1_page_text.strip()#取出收尾的回车
#二级m3u8地址
m2_url = ''
for line in m1_page_text.split('\n'):
    if not line.startswith('#'):
        m2_url = line
        #补充m2_url:缺少域名
        m2_url = 'https://h0.rzisytn.cn/'+m2_url
        #至此就获取到了完整的二级文件地址
#请求二级文件地址内容
m2_page_text = requests.get(url=m2_url,headers=headers).text
m2_page_text = m2_page_text.strip()

#解析出每一个ts切片的地址
ts_url_list = []
for line in m2_page_text.split('\n'):
    if not line.startswith('#'):
        ts_url = line
        #不同ts下载地址
        ts_url = 'https://h0.rzisytn.cn'+ts_url
        ts_url_list.append(ts_url)

#请求到每一个ts切片的数据
for url in ts_url_list:
    #获取ts片段的数据
    ts_data = requests.get(url=url,headers=headers).content
    ts_name = url.split('/')[-1]
    ts_path = dirName+'/'+ts_name
    with open(ts_path,'wb') as fp:
        #需要将解密后的数据写入文件进行保存
        fp.write(ts_data)
    print(ts_name,'下载保存成功！')

# ts文件的合并，最好网上找专业的工具进行合并，自己手动合并会经常出问题