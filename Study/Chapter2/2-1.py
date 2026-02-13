#-*-coding:utf-8-*-
# 2-1 字面量
print("# 2-1 字面量")
print("666") 
print('py学习')
print(13.14)

# 2-2 注释
print("# 2-2 注释")
# 单行注释
'''多行注释'''

# 2-3 变量
print("# 2-3 变量")
money = 50 ;
print("钱包还有:" , money , "元")

# ===== 练习begin =====
money = 50 # 初始余额
ice = 10 
colo = 5
print("Left : " , money - ice - colo)
# ===== 练习end =====

# 2-4 数据类型
print("# 2-4 数据类型")
print("money: " , money , "Type:" , type(money))
money -= 3.2 
print("money: " , money , "Type:" , type(money))

# 2-5 数据类型转换
print("# 2-5 数据类型转换")

'''万物皆可转字符串'''

num_str = str(11)
num_float = float(11)
num_int = int(11.2)
print( "Num: " , num_str , "Type :" , type(num_str))
print( "Num: " , num_float , "Type :" , type(num_float))
print( "Num: " , num_int , "Type :" , type(num_int))

# 2-6 标识符
print("# 2-6 标识符")

# 2-7 运算符
# 基础运算
print(9 // 2)
print(9 % 2)
print(9**2)

# 复合运算: 注意,c和py在// 和 / : c的取整:/(int取整,float就是除法) py的取整:// 除法:/
num1 = 9
num2 = 9
num1 //= 2
print(num1)

num2 /= 2
print(num2)

# 2-8 字符串
print("# 2-8 字符串")
name1 = '单引号定义法'
name2 = "双引号"
name3 = """三引号"""
name4 = '''如果不使用变量接收的话,那这就是纯注释'''
name5 = "\"转义字符表示引号"
'''
打印结果
'''
print(name1)
print(name2)
print(name3)
print(name4)
print(name5)

# 2-9 字符串的拼接
print("# 2-9 字符串的拼接")
print("使用加号" + "进行string拼接")
print("拼接非string:" , num1 , "像这样")

# 2-10 字符串格式化
print("# 2-10 字符串格式化")
name = "Python"
date = 20260213
msg = "学习%s , 日期:%d" % (name , date)
print(msg)

# 2-11 字符串格式化的精度控制
print("# 2-11 字符串格式化的精度控制")
num = 79.236
print("数据:%5.2f" % num)
print("数据:%07.2f" % num)

# 2-12 字符串格式化2
print("# 2-12 字符串格式化2")
print(f"学习{name} , 日期: {date}")

# 2-13 格式化表达式
print("# 2-13 格式化表达式")
print(f"{1 + 1} = {4 // 2}")

# ===== 练习begin =====
name = "传智播客"
stock_price = 19.99
stock_code = "003032"
print(f"公司: {name} , 股票代码: {stock_code} , 当前股价: {stock_price}")
print("每日增长系数是:%.1f , 经过%d天的增长后, 股价达到了: %.2f" % (1.2 , 7 , 71.63))
# ===== 练习end =====

# 2-14 数据输入
print("# 2-14 数据输入")

# name = input("你是谁?")
# print("我是%s"%name)

num = input("银行密码:")
print(f"银行密码:{num} , 数据类型:{type(num)}")
print(f"银行密码:{num} , 数据转换:{type(int(num))}")

