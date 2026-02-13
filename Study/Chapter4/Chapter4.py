#-*-coding:utf-8-*-
print("======Chapter4======")

# 4-1 while 循环基础
print("# 4-1 while 循环基础")
# ===== 练习 begin =====
i = 1 
total = 0 
while(i <= 100):
    total += i 
    i += 1
print("1 + 2 + 3 + ... + 100 = %d" % total)
# ===== 练习 end =====

# 4-2 while循环的嵌套运用
print("# 4-2 while循环的嵌套运用")
# 输出不换行
print("print输出不换行:" , end = "")
print("没换行吧")
# 制表符:对齐作用
print("Hello \tWorld")
print("123456789")

# ===== 练习 begin =====
# 打印9*9乘法表
i = 1  # 行
j = 1  # 列 , 小于等于行i
while(i <= 9):
    while(j<=i):
        print(f"{j}*{i}={j*i}\t" , end="")
        j += 1
    print("")
    i += 1
    j = 1
# ===== 练习 end =====

# 4-3 for循环的基础语法
name = "lxl666"
for x in name:
    print(f"{x}" , end="")
print()


# ===== 练习 begin =====
# "itheima is a brand of itcast" 有多少个a?
name = "itheima is a brand of itcast"
num_a = 0
for x in name:
    if (x == 'a'):
        num_a += 1
print(f"语句 \" {name} \" 含有 {num_a} 个 \' a \' ")
# ===== 练习 end =====

# 4-4 range语句
'''
- 语法:
	- range(n) : 得到 0 - n(不含) 的数据序列
	- range(n1 , n2) : n1(含) - n2(不含) 数据序列
	- range(n1 , n2 , step ) : n1 - n2(不含) , 步进为step
'''
# 语法1
range1 = range(6)
for x in range1:
    print(f"{x}" , end="")
print()

# 语法2
for x in range(2 , 7):
    print(f"{x}" , end="")
print()

# 语法3
for x in range(2 , 7 , 2):
    print(f"{x}" , end="")
print()

# 4-5 变量作用域

# 略

# 4-6 for循环的嵌套使用

