import requests
import time
import execjs
from Crypto.Cipher import AES
import base64

# t = str(int(time.time() * 1000))
# print(t)

with open("guanniao.js") as f:
    JS_code = f.read()
JS_compile = execjs.compile(JS_code)
ret = JS_compile.call("get_headers")
print(ret)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Referer': 'http://birdreport.cn/',
    'Requestid': ret['requestId'],
    'Sec-Ch-Ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': "Windows",
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'Sign': ret['sign'],
    'Timestamp': ret['timestamp'],

}
data = {

}
url = "https://api.birdreport.cn/front/activity/search"

res = requests.post(url=url, data=data, headers=headers)
res_json = res.json()
base64_enc_data = res.json().get("data")

# 解码并解密：
key = '3583ec0257e2f4c8195eec7410ff1619'.encode()
iv = 'd93c0d5ec6352f20'.encode()

aes = AES.new(key, AES.MODE_CBC, iv)
enc_data = base64.b64decode(base64_enc_data)
# print(ret)
data = aes.decrypt(enc_data).decode()
print(data)