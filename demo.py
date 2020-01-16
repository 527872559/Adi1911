# 所有的字符串都能转换为字节串
# 并不是所有的字节串都能转换为字符串

s = "Hello world"

s = b"Hello world" # 字节串  适用于ascii字符

s = "你好".encode()  # 将字符串 转换为 字节串

# s_ = b'\xe0\xcd\xa2\xe7\xa5\xbd'.decode()  # 字节串 转换为 字符串

s_ = s.decode()

print(s_)

print(type(s))
