import execjs
import requests

f = open("01 qimai.js", mode='r', encoding="utf-8")
js_code = f.read()
f.close()

js = execjs.compile(js_code)

url = "https://api.qimai.cn/rank/index"

params = {
"brand": "free",
"device": "iphone",
"country": "cn",
"genre": "36",
"date": "2023-11-12",
"page": 1,
"is_rank_index": 1,
}

analysis = js.call("get_analysis", url, params)
print("analysis:::", analysis)
params['analysis'] = analysis

resp = requests.get(url, params, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
})

print(resp.json())