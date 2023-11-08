import base64

# print(base64.b64encode(b"you"))
data = "you"
print(base64.b64encode(data.encode()))
# print(ord("y"))
# print(ord("o"))
# print(ord("u"))
# print(bin(121))
# print(bin(111))
# print(bin(117))
#
# print(bin(97))
print(base64.b64encode(data.encode()).decode())

# base64编码
data = "i love you"
ret = base64.b64encode(data.encode()).decode()
print(ret)

# base64解码
s = "aSBsb3ZlIHlvdQ=="
ret = base64.b64decode(s).decode()
print(ret)

# 案例2:数据填充:base64解码的数据一定要是4的倍数
s = "aSBsb3ZlIHlvdSE"
# 手动填充
s += "=" * (4 - len(s) % 4)
print(s)
ret = base64.b64decode(s).decode()
print(ret)

# 案例3:base64的变种

data ="BkiKG8jzVGzbWOl4m8NXJEYglgtxhOB05MGmap8JSP97GzoewPBmDTs7c5iACUof3k/uJf0H88GygajVgBvkcbckJp7oO+Qj6VSUQYTOHhKN/VG2a8v+WzL34EO/S7BYoj2oOxIDAr8wDLxYxjBeXq/Be6Q1yBbnZcKaMkifhP8="
new_data = data.replace("+", "-").replace("/", "_")
print(new_data)

new_data = "BkiKG8jzVGzbWOl4m8NXJEYglgtxhOB05MGmap8JSP97GzoewPBmDTs7c5iACUof3k_uJf0H88GygajVgBvkcbckJp7oO-Qj6VSUQYTOHhKN_VG2a8v-WzL34EO_S7BYoj2oOxIDAr8wDLxYxjBeXq_Be6Q1yBbnZcKaMkifhP8="
data = new_data.replace("-", "+").replace("_", "/")
print(data)
print(base64.b64decode(data))