import requests

res = requests.get("http://m701.music.126.net/20231110193131/ade00e60eda241df8ce5872dd39b29b1/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/31356911284/7e5a/7159/4ce7/0d177e2e030311ec8f4eddae23723224.m4a")
with open("折自磨.m4a", "wb") as f:
    f.write(res.content)