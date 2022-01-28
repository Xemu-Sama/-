import os

print(os.getcwd())
file = open('message.txt','w')
file.write("这是一个文件\n")
file.close()