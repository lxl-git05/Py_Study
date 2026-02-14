#-*-coding:utf-8-*-

__all__ = ['add']   # import * 时只能all里面的才能被执行

def add(a , b):
    return a + b

def de(a , b):
    return a - b

if __name__ == '__main__' :
    print("=========== 当前在my_module模块测试中 ===========")
    print(f"add(1 , 2) = {add(1 , 2)}")

