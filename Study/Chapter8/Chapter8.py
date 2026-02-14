#-*-coding:utf-8-*-
print("======Chapter8======")
# 8-1 文件编码概念
print("# 8-1 文件编码概念")

# 8-2 文件读取
print("# 8-2 文件读取")
# 打开文件
f = open("D:/github/2-1-Py_Projects/Py_Study/Study/Chapter8/8-2.txt" , "r" , encoding="UTF-8")
print(type(f))

# 光标意识:
    # 读取是使用光标进行读取的,不会因为再次调用而回到开始

# 读取文件 read会读取后,光标停在读取结束处
# print(f"读取2个字节: {f.read(2)}")
# print(f"读取剩下全部字节: {f.read()}")

# 读取文件的全部行,封装到列表,每行都是/n结束 
# lines = f.readlines()
# print(f"读取lines : {lines}")

# 一次读取一行,每行都是/n结束 
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(f"第1行:{line1}")
# print(f"第2行:{line2}")
# print(f"第3行:{line3}")
# list = [line1 , line2 , line3]
# print(list)

# for循环读取文件行
# for x in f:
#     print(f"{x}")

# 关闭文件对象
f.close()

# with open 语法 , 结束后自动关闭
with open("D:/github/2-1-Py_Projects/Py_Study/Study/Chapter8/8-2.txt" , "r" , encoding="UTF-8") as f:
    for line in f :
        print(f"每一行语句:{line}")

# ===== 练习begin =====
with open("D:/github/2-1-Py_Projects/Py_Study/Study/Chapter8/8-2-lian.txt","r",encoding="UTF-8") as f:
    count = 0   # 统计itheima出现的次数
    for line in f:
        count += line.count("itheima")
    print(count)
# ===== 练习end =====

# 8-3 文件写入
print("# 8-3 文件写入")
f = open("D:/github/2-1-Py_Projects/Py_Study/Study/Chapter8/8-3.txt","w",encoding="UTF-8")
f.write("lxl")

f.flush()
f.close() # 内置flush的功能

# 8-4 文件追加
print("# 8-4 文件追加")
f = open("D:/github/2-1-Py_Projects/Py_Study/Study/Chapter8/8-4.txt","a",encoding="UTF-8")
f.write("/nlxl666")
f.close()

# ===== 综合案例 =====
print("# 8 综合案例")
f_bill = open("D:/github/2-1-Py_Projects/Py_Study/Study/Chapter8/8-zonghe.txt","r",encoding="UTF-8")
f_bak  = open("D:/github/2-1-Py_Projects/Py_Study/Study/Chapter8/8-zonghe-bak.txt","w",encoding="UTF-8")
# 遍历进行操作
for line in f_bill:
    # 文件测试部分丢弃
    if (line.count("测试") > 0):
        continue
    # 备份操作
    f_bak.write(line)
# 关闭文件
f_bill.close()
f_bak.close()
# ===== 综合案例结束 =====
