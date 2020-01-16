"""
每次读取5字符，读取一个文件全部内容进行打印
"""
filename = input("File:")

f = open(filename) # r 打开

while True:
    data = f.read(5)
    if not data:
        break
    print(data,end='')

f.close()
