import urllib.parse

# url编码
# 案例1:值的url编码
data = "&s"
print(urllib.parse.quote(data))

# 案例2:整体数据url编码
params = {'name': '张三', 'age': 20, 'address': '北京市海淀区'}

print(urllib.parse.urlencode(params))

#url解码

source = "name=%E5%BC%A0%E4%B8%89&age=20&address=%E5%8C%97%E4%BA%AC%E5%B8%82%E6%B5%B7%E6%B7%80%E5%8C%BA"
print(urllib.parse.parse_qs(source))