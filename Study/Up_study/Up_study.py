#-*-coding:utf-8-*-
print("======进阶学习======")

# ========= 1. 闭包 =========
print("# ========= 1. 闭包 =========")
# 闭包: 好处:inner无需依赖外部全局变量,outer的logo扮演了类似外部变量的角色,
#      使得除开main调用outer()重新赋值外没有任何办法改变inner的"外部变量logo"

def outer(logo):

    def inner(msg):
        print(f"logo:{logo} , msg: {msg}")
    
    return inner

fn1 = outer("外部变量1")    # 返回的是个函数
print(type(fn1))
fn1("内部数据1")
fn1("内部数据1.2")

fn1 = outer("外部变量2")
fn1("内部数据2")

# 闭包改变内部全局变量,nonlocal后内部全局闭包变量会被静态记忆持续被修改
def outer2(num1):

    def inner2(num2):
        nonlocal num1 
        print(f"nonlocal改变前闭包内部变量num1:{num1}")
        num1 += num2
        print(f"nonlocal改变后闭包内部变量num1:{num1}")

    return inner2

fn2 = outer2(3)
fn2(2)
fn2(2)

# ========= 2. 装饰器 =========
print("# ========= 2. 装饰器 =========")
# 在不破坏目标函数原有的代码和功能的前提下为目标函数添加新功能
def outer(func):
    def inner():
        print("先验操作")
        func()
        print("后续操作")

    return inner

def func_print():
    print("中间回调函数操作")

# 写法一:显式表示
fn = outer(func_print)
fn()
print("======分割线======")
# 写法二:装饰隐式显示,其实也就是将函数作为参数传入outer,写法就是在函数前@outer,实现函数功能拓展但是本体内部没有更改(其实就是借助外部outer扩展功能)
@outer
def func_print():
    print("中间回调函数操作")

func_print()

# ========= 3. 单例模式 =========
print("# ========= 3. 单例模式 =========")
# 其实就是一个类只有一个实例(真对象),后续多少"对象"都共用相同的静态实例(都只调用这个对象,其实有点像全局变量的效果)
# 非单例
class StrTools:
    pass

s1 = StrTools()
s2 = StrTools()

print(s1)
print(s2)
print("地址不同,不是单例")

# 单例
class intTools:
    pass
# 单例,后续不准再构建对象了
inttool = intTools()
# 外部调用的时候:
t1 = inttool
t2 = inttool

print(t1)
print(t2)
print("地址相同,是单例")

# ========= 4. 工厂模式 =========
print("# ========= 4. 工厂模式 =========")
class Person:
    pass

class Worker(Person):
    pass

class Student(Person):
    pass

class Teacher(Person):
    pass

class Factory:
    def get_person(self, p_type:str):
        if (p_type == 'w'):
            return Worker()
        if (p_type == 's'):
            return Student()
        if (p_type == 't'):
            return Teacher()
# 构建工厂单例(统一入口)
pf = Factory()
# 加入人员,很方便
Worker1 = pf.get_person('w')
Worker2 = pf.get_person('w')
print(Worker1)
print(Worker2)

Teacher1 = pf.get_person('t')
Student1 = pf.get_person('s')

# ========= 5. 进程和线程-多线程 =========
print("# ========= 5. 进程和线程-多线程 =========")
import time
import threading    # 多线程
def task1(msg:str):
    while True:
        print(f"任务1:msg:{msg}")
        time.sleep(1.1)

def task2(msg:str):
    while True:
        print(f"任务2:msg:{msg}")
        time.sleep(2)

# 创建任务1线程与参数传递
task1_thread = threading.Thread(target=task1 , args=("任务1使用元组形式传递参数,单个参数记得加逗号表明是元组", ))
task2_thread = threading.Thread(target=task2 , kwargs={"msg":"任务2使用字典传递参数"})

# 开启线程
# task1_thread.start()
# task2_thread.start()

# ========= 6. 网络编程:服务端 =========
'''
print("# ========= 6. 网络编程:服务端 =========")
import socket
# 创建socket对象
socket_server = socket.socket()
# 绑定IP地址和端口
socket_server.bind(  ("localhost" , 8888)  )
# 监听端口:传入参数:允许连接的数量
socket_server.listen(1)
# 等待客户端连接
result = socket_server.accept( )
conn = result[0]    # 客户端和服务端的连接对象
address = result[1] # 客户端的地址信息
# accept()是阻塞式方法(一直阻塞)
print(f"接收到了客户端的连接,信息:{address}")

while True:
    # 接收 客户端消息(使用conn)
    data:str = conn.recv(1024).decode("UTF-8")  # 缓冲区,解码形式
    print(f"客户端消息:{data}")

    # 回复 消息
    msg = input("请输入回复消息").encode("UTF-8")
    print(f"打印的是{msg}")
    if (msg == b'exit'): # 退出对话,str前面加个b
        break
    conn.send(msg)


# 关闭连接
conn.close()
socket_server.close()
'''
'''
# ========= 7. 网络编程:客户端 =========
print("# ========= 7. 网络编程:客户端 =========")
import socket
# 创建对象
socket_clinet = socket.socket()
# 链接到服务器
socket_clinet.connect( ("localhost" , 8888) )


# 发送消息,服务端需要使用conn地址,地址会变,但是客户端就不需要
socket_clinet.send("你好".encode("UTF-8"))
# 接收返回信息
rec = socket_clinet.recv(1024).decode("UTF-8")
print(f"接收信息:{rec}")

# 关闭连接
socket_clinet.close()
'''
# ========= 8. 正则表达式-基础匹配:字符串匹配 =========
print("# ========= 8. 正则表达式-基础匹配:字符串匹配 =========")
import re   # 正则表达式
# 8-1 match匹配:只看头
print("======== match ========")
result = re.match("python" , "python and C")
print(result)

result = re.match("python" , "kpython and C")
print(result)

# 8-2 search匹配:从前往后寻找到第一个
print("======== search ========")
result = re.search("python" , "python and C")
print(result)

result = re.search("python" , "kpython8 and C")
print(result)

# 8-3 findall匹配:从前往后寻找,返回全部
print("======== search ========")

result = re.findall("python" , "kpython8 and C or kpython8 and C")
print(f"result : {result} and len: {len(result)}")

# ========= 9. 正则表达式-元字符匹配 =========
print("# ========= 9. 正则表达式-元字符匹配 =========")

s = "itheima @@python2 !! 666 3456mdsk#234"
result = re.findall(r"[a-hA-Z]" , s)  # r表示字符串中转义字符无效
print(result)

# 匹配账号,只能由字母和数字组成,长度限6到10位
s = "1234xa234"
result = re.findall(r"^[a-zA-Z0-9]{6,10}$" , s) # ^规则$ : 从头到尾都是这个匹配规则才行
print(result)

# 匹配QQ号，要求纯数字，长度5-11，第一位不为0
s = "3514478323"
result = re.findall(r"^[1-9][0-9]{4,10}$" , s) # ^规则$ : 从头到尾都是这个匹配规则才行
print(result)

# 匹配邮箱地址,只允许qq、163、gmaiL这三种邮箱地址
s = "3514478323@qq.com"
result = re.findall(r"(^[\w-]+(\.[\w]+)*@(qq|163|gmail)(\.[w-]+)+$)" , s) # ^规则$ : 从头到尾都是这个匹配规则才行
print(result)

# ========= 10. 递归 =========
print("# ========= 10. 递归 =========")
# 略,以后深度学
