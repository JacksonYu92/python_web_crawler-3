import requests
import execjs #pip install PyExecJS
import json

# (1) 获取动态逆向值

with open("04 wangyiyun.js") as f:
    js_code = f.read()
# print(js_code)

js_compile = execjs.compile(js_code)
song_id = 2097278593
t = {"ids":f"[{song_id}]","level":"standard","encodeType":"aac","csrf_token":""}

x1 = json.dumps(t)
x2 = '010001'
x3 = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
x4 = '0CoJUm6Qyw8W8jud'

ret = js_compile.call("d", x1, x2, x3, x4)
print(ret)
data = {
    'params': ret['encText'],
    'encSecKey': ret['encSecKey']
}

# (2) 发起请求

my_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Referer': 'https://music.163.com/',
    'Cookie': 'NMTID=00OxNA3xlsr_ApDeUpLlO2mJP6hRv4AAAGLuNf-nQ; JSESSIONID-WYYY=t0VrjxCFqQZQPVutZEzF0%2Bk9aljo56WMlyt3U9HWtnz15BG5ma86h%2Fg432WNwtE0BwIjEWNFw6VFA2hhHjJwYXY3AJ3O8eqDltOpm5ZDB%2FRMAPDnO61cUA9BRnIHEMWdNhypW6jyRGNSMU37Kf4J0Ss8Sm6Vsm6UgkCybJUPV2mHBXlt%3A1699615045614; _iuqxldmzr_=32; _ntes_nnid=b1c11f74582a99c82fd21f4b530fa6bd,1699613245635; _ntes_nuid=b1c11f74582a99c82fd21f4b530fa6bd; WEVNSM=1.0.0; WNMCID=teriec.1699613246372.01.0; WM_TID=ffclSLdWa6xEQFAREEaAiFbAlq7kpzw4; WM_NI=h6DY5U%2FFa80PJGxyz6oR0MueOQ6pErc%2BI1Lo4r1hc%2B%2Bi%2FleTBbIOlIzZ2GgaVx2bypXvEKniDFkLq42B9UvKRdPvGVOiFy0wSBvNl4bdByXDqqveTNfmAYgHprl12M0DYWk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee87d86aaa8ffbacd474bb968ea2c14f839e8eb0d867b1e99a94bb4a92a900d3d82af0fea7c3b92aacea8cbab85fed9aafd9b35c8a99b89af93ead8e00aef86f8d8ffa91c87aa1f587d2cf65f8aeff89e221e9b7e18de86082be87b0ef43ba86fea8e66b96a8fe83fc7c9caa8baced63889aa5adf440f29ef7b6f54192bca097c65e8db78a9ab37d919ebaafef40a2bc8e9adb50b3afba86d746a6b38fbae644b4aea4d2b147f49c97b8ea37e2a3; ntes_utid=tid._.vVvpptIw%252FttBVlUUEBOU3ALUk76jJ5lF._.0; sDeviceId=YD-TOYk%2B5hjmtNEBlFBERfQnQPB07q3ZowI'
}
url = "https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token="
res = requests.post(url=url, data=data, headers=my_headers)
print(res.json())