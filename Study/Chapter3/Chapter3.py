#-*-coding:utf-8-*-
print("======Chapter3======")

# 3-1 比较运算符
print("# 3-1 比较运算符")

result1 = 10 > 5
print(result1)

result2 = "day" == "Day"
print(result2)

print(f"类型: {type(result1)}")

# 3-2 if语句的基本格式
print("# 3-2 if语句的基本格式")
age = 2
if (age > 18) :
    print("成年")
elif age <= 0:
    print("666")
else :
    print("未成年")

# ===== 练习begin =====
# age = int(input("请输入年龄"))
# if age >= 18 :
#     print("成年了,你通过!")
# else:
#     print("未成年,gui!")
# ===== 练习end =====

# 3-3 if else 语句

# 略 , 练习也略

# 3-4 if elif else 语句

# 内容略

# ===== 练习begin =====
# num_goal = 5
# num = int(input("请在0-9猜一个数字"))
# while(num != num_goal):
#     num = int(input("猜错了,请再在0-9猜一个数字"))
# print("恭喜猜对了")
# ===== 练习end =====

# 3-5 语句的嵌套
print("# 3-5 语句的嵌套")

# 略

# ===== 综合案例begin =====
import random
num_goal = random.randint(1,10)

time = 3
num = int(input("猜数字,你有三次机会,开始吧:"))
while(1):
    if (num == num_goal):
        print("666,猜到了")
        break ;
    elif (num > num_goal):
        num = int(input("猜大了,重新输入"))
    else :
        num = int(input("猜小了,重新输入"))
    time -= 1
    if (time == 0):
        print(f"废物,这都猜不出来, 答案是{num_goal}")
        break

# ===== 综合案例end =====
