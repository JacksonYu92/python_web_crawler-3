import requests
import execjs
from urllib.parse import urlencode
from Crypto.Cipher import AES
import base64

with open("03 birdreport.js") as f:
    js_code = f.read()

js_compile = execjs.compile(js_code)

data = {
    "city": "",
    "ctime": "",
    "district": "",
    "endTime": "",
    "limit": "20",
    "mode": "0",
    "outside_type": "0",
    "page": "4",
    "pointname": "",
    "province": "新疆",
    "serial_id": "",
    "startTime": "",
    "state": "",
    "taxonid": "",
    "taxonname": "",
    "username": "",
}
# print(urlencode(data))
data = js_compile.call("get_data", urlencode(data))
# print(data)
headers = data.get("headers")
encrypt_data = data.get("encrypt_data")

session = requests.session()
url = "https://api.birdreport.cn/front/record/activity/search"
session.headers.update(
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        "Referer": "http://birdreport.cn/",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
)
session.headers.update(headers)
print("session.headers:::", session.headers)
res = session.post(url, data=encrypt_data, )
# print(res.json().get("data"))
base64_enc_data = res.json().get("data")

# 解码并解密：
key = '3583ec0257e2f4c8195eec7410ff1619'.encode()
iv = 'd93c0d5ec6352f20'.encode()

aes = AES.new(key, AES.MODE_CBC, iv)
enc_data = base64.b64decode(base64_enc_data)
# print(ret)
data = aes.decrypt(enc_data).decode()
print(data)