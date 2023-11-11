import requests
import time
import hashlib
import json

t = str(int(time.time()*1000))




url = "https://mapi.yiche.com/web_api/car_model_api/api/v1/car/config_new_param?"

s1 = {"cityId": "521", "serialId": "1729"}

params={
'cid': '508',
'param': '{"cityId":"521","serialId":"1729"}',
}
s1 = json.dumps(s1,separators=(',', ':'))
print("s1,", s1)
s2 = f'cid=508&param={s1}19DDD1FBDFF065D3A4DA777D2D7A81EC{t}'
print("s2",s2)
md5 = hashlib.md5()
md5.update(s2.encode())
sign = md5.hexdigest()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Referer': 'https://car.yiche.com/baoma3xi/peizhi/',
    'Cookie': 'CIGUID=63a495e2b2b524525739ff5af6017327; isWebP=true; locatecity=440700; bitauto_ipregion=120.230.167.118%3A%E5%B9%BF%E4%B8%9C%E7%9C%81%E6%B1%9F%E9%97%A8%E5%B8%82%3B521%2C%E6%B1%9F%E9%97%A8%E5%B8%82%2Cjiangmen; auto_id=93ef4b2fb67130e29280084af06b007e; UserGuid=63a495e2b2b524525739ff5af6017327; Hm_lvt_610fee5a506c80c9e1a46aa9a2de2e44=1699682081; selectcity=440700; selectcityid=521; selectcityName=%E6%B1%9F%E9%97%A8; Hm_lpvt_610fee5a506c80c9e1a46aa9a2de2e44=1699682091',
    'X-City-Id': '521',
    'X-Ip-Address': '120.230.167.118',
    'X-Platform': 'pc',
    'X-Sign': sign,
    'X-Timestamp': t,
    'X-User-Guid': 'dd19d78574320c243f7a88b8c7b1c075',
}
res = requests.get(url=url, params=params, headers=headers)
print(res.url)
print(res.text)