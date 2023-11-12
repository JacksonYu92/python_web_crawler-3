import requests
import execjs
import json


# 打码平台：tujian
# 3: 数字和英文混合
def base64_api(img_base64, typeid):
    data = {"username": "yuan0316", "password": "yuan0316", "typeid": typeid, "image": img_base64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        # ！！！！！！！注意：返回 人工不足等 错误情况 请加逻辑处理防止脚本卡死 继续重新 识别
        return result["message"]
    return ""


session = requests.session()
session.headers[
    "User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"

# (1) 加载JS代码

with open("01 ypwk.js") as f:
    JS_code = f.read()

JS_compile = execjs.compile(JS_code)

# (2) 获取验证码
data = {}

headers = JS_compile.call("get_headers", data)
session.headers.update(headers)

res = session.get("https://www.epwk.com/api/epwk/v1/captcha/show?channel=common_channel&base64=1")
base64_img = res.json().get("data").get("base64")

code = base64_api(base64_img, 3)
print(code)
# (3) 模拟登录请求
data = {
    "username": "yuan",
    "password": "yuan1234",
    "code": code,
    "hdn_refer": "https://www.epwk.com/"
}

headers = JS_compile.call("get_headers", data)
print(headers)
session.headers.update(headers)

res = session.post("https://www.epwk.com/api/epwk/v1/user/login", data=data)
print(res.text)