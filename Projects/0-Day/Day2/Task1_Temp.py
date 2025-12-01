"""

将华氏温度转换为摄氏温度
F = 1.8C + 32

Version: 0.1
Author: lxl
Date: 2025-12-1

"""
# lxl

# 温度输入
Temp_F = input("请输入华氏温度：")
# 数据格式转换
Temp_F = float(Temp_F)
# 打印温度值
print(Temp_F)
# 打印转化后的的温度
print("摄氏温度为:" , Temp_F * 1.8 + 32)

# gh
f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))

# 1. 使用数据转换 + input直接进行转化,不用再起一行

# 2. print 的使用, 可以直接使用, 也可以使用占位符, 使用占位符可以直接进行数据的转化

