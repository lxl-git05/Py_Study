# 1. 使用input
# 用法: input("提示信息"),从而赋值给一个接收的变量

name = input("请输入你的名字：")
print("你好，" + name)

# 2. 使用print
print("你好，%s" % name)
print("你好，{}".format(name))
print(f"你好，{name} , {name}")
# 最推荐
name = "Alice"
age = 18
score = 97.568
print(f"Name:{name}, Age:{age:d}, Score:{score:.1f}")
