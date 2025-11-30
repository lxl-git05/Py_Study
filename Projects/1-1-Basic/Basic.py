#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. print
print("Hello World")    # 单引号或者双引号

# 2. String
str1 = "1'2'3"  # 表示引号1
print(str1)

str2 = '1"2"3'  # 表示引号2
print(str2)

str3 = '1\'2\'3'  # 表示引号3
print(str3)

# 也就是在单引号或者双引号中，如果需要使用单引号或者双引号，可以使用转义符\

# 3. integer 
int1 = 1 * 2
int2 = 1 / 2
print(int1)
print(int2)
print(type(int1))
print(type(int2))

# 4. float
float1 = 1.0 * 2.0
float2 = 1.0 / 2.0
print(float1)
print(float2)
print(type(float1))
print(type(float2))

print(0.55 + 0.41)  # 0.9600000000000001 , 浮点数计算精度问题,在比大小和比较相等时，需要注意
print(0.55 == 0.41 + 0.14)  # False , 但是vscode中可以正确识别

# 5. bool
# 布尔值可以用 and(&)、or(||) 和 not(!) 运算
bool1 = True and False
bool2 = True or False
bool3 = not True
print(bool1)
print(bool2)
print(bool3)

# 6. None
# None 表示空值，它和其他语言中的 null 一样，可以用在任何类型中

# 7. 数据类型转换
# 7-1 int()转换
str1 = '100'
str2 = '300'
print(str1 + str2)
print(int(str1) + int(str2))    
# 这里是符合规则的字符串类型，如果是文字形式等字符串是不可以被 int() 函数强制转换的,小数形式的字符串也是不能用 int() 函数转换的
# 这并不是意味着浮点数不能转化为整数，而是小数形式的字符串不能强转为字符串。浮点数还是可以通过 int() 函数转换的,但是会被截断

# 8. 变量
# 8-1 变量的创建与赋值:动态语言,不需要声明变量类型,在赋值时会自动判断类型

# 8-2 变量的指向问题
a = 'hello'
b = a 
a = 'world'
print(a)
print(b) 
# 可以看到a的值已经被改变了,但是b的值并没有改变,这是因为a和b指向了不同的内存地址,a指向了新的内存地址,b指向了原来的内存地址,也就是a和b类似C语言的动态指针,指向了不同的静态内存地址

# 8-3 多个变量命名
a = b = c = 1 
print(a)
print(b)
print(c)    

a, b, c = 1 , 2 , "hi"
print(a)
print(b)
print(c) 

