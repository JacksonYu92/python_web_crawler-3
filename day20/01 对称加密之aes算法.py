from Crypto.Cipher import AES
import base64

# AES-128模式: key: 16 iv: 16位 明文是16的倍数
# 明文
# data = "Alex is ugly!"
data = '{"name":"alex","msg":"ugly"}'

while len(data) % 16 != 0:
    data += "\0"

print(data, len(data))

# 密钥
key = "1234567890123456".encode()
# 偏移量
iv = "aaaabbbbccccdddd".encode()

# (1) 加密,发生在客户端

# 构建aes算法对象
aes = AES.new(key, AES.MODE_CBC, iv)

encrypt_data = aes.encrypt(data.encode())
print(f"加密数据{encrypt_data}")
# b'\x93\x1e\xdca\xbd\x08\xb1\xed\xef\xdbc\xc0\xa31\xaco'

# (2) base64编码,发生在客户端
base64_encrypt_data = base64.b64encode(encrypt_data).decode()
print("base64_encrypt_data:", base64_encrypt_data) #kx7cYb0Ise3v22PAozGsbw==

# (3) base64解码,发生在服务端
# base64_encrypt_data = "kx7cYb0Ise3v22PAozGsbw=="
base64_encrypt_data = "ipmd89j3VlVClCk6EuFQFVxIeag1OwY0FrEKRTz2c9Y="
encrypt_data = base64.b64decode(base64_encrypt_data)
print(encrypt_data)
# (4) 解密,发生在服务端

# 密钥
key = "1234567890123456".encode()
# 偏移量
iv = "aaaabbbbccccdddd".encode()

#解密
# 构建aes算法对象
aes = AES.new(key, AES.MODE_CBC, iv)
source_data = aes.decrypt(encrypt_data).decode()
print("source_data:", source_data)

import json

data_dict = json.loads(source_data.rstrip("\0"))
print("name:", data_dict.get("name"))
print("msg:", data_dict.get("msg"))