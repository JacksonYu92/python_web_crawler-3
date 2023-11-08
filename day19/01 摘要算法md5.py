import hashlib

# 案例1
md5_object = hashlib.md5()
# 摘要数据
data = "我喜欢你，OK？"
# 摘要函数
md5_object.update(data.encode())
# 获取摘要结果
print(md5_object.hexdigest())
# 37405d29075f9334f768fc59693003f6


# 案例2
md5_object = hashlib.md5()
# 摘要数据
data01 = "hello"
# 摘要函数
md5_object.update(data01.encode())
data02 = "yuan"
# 摘要函数
md5_object.update(data02.encode())

# 获取摘要结果
print(md5_object.hexdigest())

# d843cc930aa76f7799bba1780f578439


# 案例3: 加盐salt
username = 'yuan'
password = "123456"

# md5_object = hashlib.md5()               #e10adc3949ba59abbe56e057f20f883e
md5_object = hashlib.md5(b"asdfghjkl")     #5b48c185e886ff93be5244f979b2864b

# 摘要函数
md5_object.update(password.encode())
# 获取摘要结果
print(md5_object.hexdigest())
print(md5_object.digest())