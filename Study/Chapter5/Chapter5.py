#-*-coding:utf-8-*-
print("======Chapter5======")

# 5-1 函数初认识
print("# 5-1 函数初认识")
str1 = "itheima"
str2 = "lxl666"
str3 = "Counter"

cnt = 0
for x in str1:
    cnt += 1
print(cnt)

# 自定义函数
def my_len(data):
    cnt = 0
    for x in data:
        cnt += 1
    return cnt

print(my_len(str2))

# 5-2 函数定义
print("# 5-2 函数定义")
def say_hello():
    print("Hello World")
say_hello()

# ===== 练习begin =====
def Check():
    print("欢迎!!!")
    print("出示健康码")

Check()
# ===== 练习end =====

# 5-2 函数的参数
print("# 5-2 函数的参数")
def add(x , y):
    return x+y
print(add(3,4))

# ===== 练习begin =====
# def Check2(temp):
#     if (temp > 37.5):
#         print("发烧")
#     else:
#         print("你通过!")

# temp = int(input("输入体温"))
# Check2(temp)
# ===== 练习end =====

# 5-3 函数的返回值
print("# 5-3 函数的返回值")

# 5-4 函数的返回值的none
print("# 5-4 函数的返回值的none")
# 函数写不写return,其实结果都是return none默认

# 5-5 函数说明文档
print("# 5-5 函数说明文档")

# 5-6 函数嵌套调用
print("# 5-6 函数嵌套调用")

# 5-7 函数变量作用域
print("# 5-7 函数变量作用域")
num1 = 1
num2 = 2

# 无法访问外部变量
def check3():
    num1 = 1000
    print(num1)

check3()
print(num1)

# 除非声明外部变量
def check4():
    global num2 
    num2 = 1000
    print(num2)

check4()
print(num2)

# ================== 综合案例 ==================
print("# 综合案例")

# 初始资产
money = 500
# 总选择控制
choice = 0
# 函数
# 退出界面
def menu_back():
    global choice
    input("按下任意按键退回主菜单")
    choice = 0

# 0. 打印主菜单界面
def mune_print():
    print("========== 主菜单 ==========")
    print("lxl , 你好 , 欢迎来到ATM机 , 请选择操作:")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    print("请输入您的选择:")

# 1. 查询余额
def menu_money_check():
    print("================ 查询余额 ================\n")
    global money 
    # 功能
    print(f"lxl你好 , 你的余额剩余: {money}")
    menu_back()

# 2. 存款
def menu_money_save():
    print("================ 存款 ================\n")
    global money 
    # 功能
    save = int(input("请输入存款额度"))
    money += save
    print(f"您存款{save}元成功")
    print(f"您的余额剩余:{money}")
    menu_back()

# 3. 取款
def menu_money_get():
    print("================ 取款 ================\n")
    global money 
    # 功能
    save = int(input("请输入取款额度"))
    money -= save
    print(f"您取款{save}元成功")
    print(f"您的余额剩余:{money}")
    menu_back()

# 总控制台
def menu_control():
    global choice
    # 进入菜单循环
    while(choice != 4):
        if (choice == 0):
            mune_print()    # 打印主菜单界面
            choice = int(input())
        elif (choice == 1):
            menu_money_check() ;
        elif (choice == 2 ):
            menu_money_save() ;
        elif (choice == 3 ):
            menu_money_get() ;
        else:
            print("输入错误!!!退出菜单")
            break

# 运行
menu_control()


