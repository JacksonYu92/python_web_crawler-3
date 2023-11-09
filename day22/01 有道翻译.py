import requests
import time
import hashlib
import base64
from Crypto.Cipher import AES

def get_md5(val, is_hex=True):
    md5 = hashlib.md5()
    md5.update(val.encode())
    if is_hex:
        return md5.hexdigest()
    else:
        return md5.digest()

url = "https://dict.youdao.com/webtranslate"

# (1)构建逆向动态值
mysticTime = str(int(time.time() * 1000))
print(mysticTime)

d = 'fanyideskweb'
e = mysticTime
u = 'webfanyi'
t = 'fsdsogkndfokasodnaso'
s = f"client={d}&mysticTime={e}&product={u}&key={t}"
print("s:::", s)

sign = get_md5(s)

# (2)请求模拟
data = {
    'i': 'apple',
    'from': 'auto',
    'to': '',
    'domain': 0,
    'dictResult': 'true',
    'keyid': 'webfanyi',
    'sign': sign,
    'client': 'fanyideskweb',
    'product': 'webfanyi',
    'appVersion': '1.0.0',
    'vendor': 'web',
    'pointParam': 'client,mysticTime,product',
    'mysticTime': mysticTime,
    'keyfrom': 'fanyi.web',
    'mid': 1,
    'screen': 1,
    'model': 1,
    'network': 'wifi',
    'abtest': 0,
    'yduuid': 'abcdefg',
}
my_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Referer': 'https://fanyi.youdao.com/',
    'Cookie': 'OUTFOX_SEARCH_USER_ID_NCOO=1971488871.1180105; OUTFOX_SEARCH_USER_ID=-389359912@120.230.146.82; _ga=GA1.2.462881916.1693871168; UM_distinctid=18acca791fd600-056b015922fdc2-26031f51-144000-18acca791fec62; P_INFO=13426749358|1698376611|1|dict_logon|00&99|null&null&null#gud&null#10#0|&0||13426749358; DICT_PERS=v2|urs-phone-web||DICT||web||-1||1698376613029||120.239.89.174||urs-phoneyd.2cb2e560e8604c11a@163.com||k5PL6FkLYl0quOfPLRLwK0eS64k5n4qBRPyRLzEkMY50YmOfz5nHJ4RlWRHwz0LpBRwu0MwFnHqLRJFhLQFP4ey0; DICT_UT=urs-phoneyd.2cb2e560e8604c11a@163.com; DICT_SESS=v2|w7gGdEDxmWe46L64kfpFRPL0MwK64wB0zE6LUm6Mkm0OM6Me4h4Tz0PLOMwuh4z5RlYh4JFkMgBRwSO4kMhfzWRzYhLgLRLeuR; DICT_LOGIN=3||1699522675146'
}
res = requests.post(url=url, data=data, headers=my_headers)
# print(res.text)
res_encrypt_base64 = res.text.replace("-", "+").replace("_", "/")
print("res_encrypt_base64:::",res_encrypt_base64)
# (3) 解密和解密数据

# 解码
res_encrypt = base64.b64decode(res_encrypt_base64)
print(res_encrypt)

# 解密

# 密钥
o = 'ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl'
n = 'ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4'



key = get_md5(o, is_hex=False)
# 偏移量
iv = get_md5(n, is_hex=False)

#解密
# 构建aes算法对象
aes = AES.new(key, AES.MODE_CBC, iv)
source_data = aes.decrypt(res_encrypt).decode()
print("source_data:", source_data)