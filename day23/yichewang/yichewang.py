import requests
import json
import time
import urllib.parse
import hashlib

mysticTime = str(int(time.time() * 1000))
print(mysticTime)


param = {"cityId": "521", "serialId": "1661"}
params = {
'cid': 508,
'param': '{"cityId":"521","serialId":"1661"}',
}
s1 = json.dumps(param, separators=(",", ":"))
print(s1)
o = '19DDD1FBDFF065D3A4DA777D2D7A81EC'
s2 = f'cid=508&param={s1}19DDD1FBDFF065D3A4DA777D2D7A81EC{mysticTime}'
print(urllib.parse.urlencode(param))

md5_object = hashlib.md5()
# 摘要函数
md5_object.update(s2.encode())
# 获取摘要结果
print(md5_object.hexdigest())
sign = md5_object.hexdigest()

my_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Referer': 'https://car.yiche.com/siyucivic/peizhi/',
    'Cookie': 'CIGUID=dd19d78574320c243f7a88b8c7b1c075; auto_id=b241b4bf0ed23ad9aa7a8eff760859ef; UserGuid=dd19d78574320c243f7a88b8c7b1c075; selectcity=440700; selectcityid=521; selectcityName=%E6%B1%9F%E9%97%A8; locatecity=440700; bitauto_ipregion=120.230.167.118%3A%E5%B9%BF%E4%B8%9C%E7%9C%81%E6%B1%9F%E9%97%A8%E5%B8%82%3B521%2C%E6%B1%9F%E9%97%A8%E5%B8%82%2Cjiangmen; Hm_lvt_610fee5a506c80c9e1a46aa9a2de2e44=1698028850,1699628030; isWebP=true; Hm_lpvt_610fee5a506c80c9e1a46aa9a2de2e44=1699683506',
    'X-City-Id': '521',
    'X-Ip-Address': '120.230.167.118',
    'X-Platform': 'pc',
    'X-Sign': sign,
    'X-Timestamp': mysticTime,
    'X-User-Guid': 'dd19d78574320c243f7a88b8c7b1c075',
}


url = 'https://mapi.yiche.com/web_api/car_model_api/api/v1/car/config_new_param?'

res = requests.get(url=url, params=params, headers=my_headers)
print(res.json())
