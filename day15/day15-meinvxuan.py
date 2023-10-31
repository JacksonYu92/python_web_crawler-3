import requests
import re
import urllib3
import json
from lxml import etree

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 MicroMessenger/6.8.0(0x16080000) NetType/WIFI MiniProgramEnv/Mac MacWechat/WMPF XWEB/30817',
}
# url = 'https://mmbiz.qpic.cn/mmbiz_jpg/NRCMWxXBYcl0gU1Wr0RX9pkHbj82phAtmTNibBonVrPOaZiaiaCNb5dYXvFOq3CYXXQoSMBES6a8NV5BB25BzpZ8g/300?wxtype=jpeg&wxfrom=401'
url = 'https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=Mzg3Nzc2OTQzOA==&uin=MTM1ODMyODkwNQ%3D%3D&key=16ff41fc38234ef85714c38b97b06d4054d7aaad452dcdaf5581c33d2104f5e1630ff6ee48da46b153f323af36a90b5e59a7129b6b28fb1c791f4a59a12ee787ad2ca7cf19ee565396f08b773ac694d06ea340cbe0d62d386a153ecfcdd84eaf742b071f75c5a234dc5d31204a1b4854d1930225947bebe72cc59476490e0e22&devicetype=iMac+MacBookPro17%2C1+OSX+OSX+13.5+build(22G74)&version=13080310&lang=zh_CN&nettype=WIFI&a8scene=0&fontScale=100&acctmode=0&pass_ticket=km2622VtVeH2MRYrt4EbChPo59EMr4MvwCDuSRJa%2F3w8GTlBsbamxA475CNyQt3m'
page_text = requests.get(url, headers=headers, verify=False).text

# with open('meinv.html', 'w') as fp:
#     fp.write(page_text)

#替换&quot;为空串
ret = re.findall("var msgList = '(.*?)'", page_text)[0]
# 将&quot;转换成引号
import html

ret = html.unescape(ret)
ret = json.loads(ret)

for dic in ret['list']:
    title = dic['app_msg_ext_info']['multi_app_msg_item_list'][0]['title']
    detail_url = dic['app_msg_ext_info']['multi_app_msg_item_list'][0]['content_url']
    detail_page_text = requests.get(detail_url, headers=headers, verify=False).text

    # 图片链接保存在img标签的data-src属性值中
    tree = etree.HTML(detail_page_text)
    img_list = tree.xpath('//img/@data-src')
    print(img_list)
    break