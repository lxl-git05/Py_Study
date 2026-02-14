#-*-coding:utf-8-*-
print("======Chapter9======")
# 9-1 了解异常
print("# 9-1 了解异常")

# 9-2 异常的捕获方法
print("# 9-2 异常的捕获方法")
try :
    f = open("abc.txt" , "r" , encoding="UTF-8")
except:
    print("出现异常,这个文件不存在")

# 捕获指定的异常
try :
    print(name)
except NameError as e :
    print("出现了变量没有定义的异常")
    print(e)    # 异常的对象

# 捕获多个异常
try :
    print(name)
except(NameError , ZeroDivisionError) as e :
    print("出现了变量没有定义或者除以0的异常错误")
    print(e)

# 捕获所有异常
try :
    open("666" , "r" , encoding= "UTF-8")
except Exception as e :
    print(f"捕获所有异常:{e}")
else:
    print("没有异常,执行代码")
finally:
    print("有没有异常都执行")


# 9-3 异常的传递
print("# 9-3 异常的传递")

def func1():
    print("执行func1")
    num = 1 / 0 # 除0异常
    print("func1结束")

def func2():
    print("执行func2,开始运行func1")
    func1()
    print("func2结束")

def main():
    try :
        func2()
    except Exception as e :
        print(f"出现错误:{e}")
    finally:
        print("finally无论如何都执行")
        # func2()

main()

# 9-4 Python的模块
print("# 9-4 Python的模块")
import time
# print("开始延时3s")
# time.sleep(3)
# print("结束延时")

# 9-5 自定义Python模块
print("# 9-5 自定义Python模块")
import my_module
print(my_module.add(1 ,2))
print(my_module.de(1 ,2))

# 9-6 自定义python包
print("# 9-6 自定义python包")
# 第1种导入方法:
# import my_package.my_module1
# import my_package.my_module2

# my_package.my_module1.print1()
# my_package.my_module2.print2()

# 第2种导入方法:(习惯)
from my_package import my_module1, my_module2

my_module1.print1()
my_module2.print2()

# 9-7 导入外部包
print("# 9-7 导入外部包")
# 我们使用vscode 导入conda install 挺好

# 9-8 综合案例
print("# 9-8 综合案例")
from my_package_lian import str_util , file_util

print(str_util.str_reverse("abcdef"))
file_util.print_file_info("D:/github/2-1-Py_Projects/Py_Study/Study/Chapter9/9-lian.txt")
file_util.append_to_file("D:/github/2-1-Py_Projects/Py_Study/Study/Chapter9/9-lian.txt" , "新增数据\n")



