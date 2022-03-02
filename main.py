import os

print(os.getcwd())
with open('message.txt','w') as file:
    file.write("这是一个文件\n")
print("完成写入\n")

