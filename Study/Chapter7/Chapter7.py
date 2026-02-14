#-*-coding:utf-8-*-
print("======Chapter7======")
# 7-1 函数的多返回值
print("# 7-1 函数的多返回值")
# return 多个即可
def test_retuen():
    return 1, 2, 4

x , y, z = test_retuen()
print(x, y, z)

# 7-2 函数多种参数方式
print("# 7-2 函数多种参数方式")

# 位置参数
def user_print(name , age , gender):
    print(f"姓名:{name} , 年龄:{age} , 性别:{gender}")

user_print("小米" , gender="女" , age = 55)

# 缺省参数
def user_print(name , age , gender="默认"):
    print(f"姓名:{name} , 年龄:{age} , 性别:{gender}")

user_print("小米" , age = 99)

# 不定长参数
# 1. 位置传递
def user_info(*args):
    print(f"args类型 : {type(args)} ,内容 : {args}")

user_info( 1 , 2 , "haha")

# 2. 关键字传递
def user_info(**kwargs):
    print(f"args类型 : {type(kwargs)} ,内容 : {kwargs}")

user_info(name = "小王" , age = 666)


# 7-3 匿名函数
# 1. 回调函数
def test(callback):
    print(f"date : 20260214")
    print(f"callback回调函数的类型:{type(callback)}")
    callback()

def Func():
    print("我是回调函数,我支持寒假延长")

test(Func)

# 2. lambda匿名函数
def test_add(callback):
    print(f"date : 20260214")
    print(f"callback回调函数的类型:{type(callback)}")
    result = callback(1 , 2)
    print(result)

test_add(lambda a , b : a + b)

