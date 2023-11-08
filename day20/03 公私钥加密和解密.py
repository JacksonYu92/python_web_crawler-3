from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64

# (1) 数据加密
# data = "I like you"
#
# with open("rsa.public.pem", "r") as f:
#     publick_key = f.read()
#     print("public_key:", publick_key)
#     # (1) 基于公钥做加密
#     rsa_pk = RSA.importKey(publick_key)
#     rsa = PKCS1_v1_5.new(rsa_pk)
#
#     encrypt_data = rsa.encrypt(data.encode())
#     print("encrypt_data:", encrypt_data)
#
#     # (2) base64编码
#     b64_encrypt_data= base64.b64encode(encrypt_data).decode()
#     print("b64_encrypt_data:",b64_encrypt_data)



b64_encrypt_data = 'u7vbqm3eosFzMTWb2YXN3+MpfkwB6axUmmSd0boAIQ1I9wnuT1WXN9jbRdy+8rEPZFnZCMKom3+8ioTK9D6Ga+tqTjfsXez1p4fdudH55HVZHZK+iHKE2/p2TtbP5SkGtKbT6+7CyTk8OLMaLyxI73T+SLoK5yejKXo+yA3Jm9M='

# (3) base64解码
encrypt_data = base64.b64decode(b64_encrypt_data)
print("encrypt_data:",encrypt_data)

# (4) 基于私钥解密
with open("rsa.private.pem", "r") as f:
    private_key = f.read()
    rsa_pk = RSA.importKey(private_key)
    rsa = PKCS1_v1_5.new(rsa_pk)

    data = rsa.decrypt(encrypt_data, None)
    print("data:", data.decode())