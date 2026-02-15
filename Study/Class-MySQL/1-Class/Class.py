#-*-coding:utf-8-*-
print("======Class======")

# 1-初识对象
print("# =========== 1-初识对象 ===========")
# 设计一个类
class Student :
    name = None             # 学生姓名
    gender = None           # 性别
    age = None              # 年龄

# 创建对象
stu1 = Student()

# 对象属性赋值
stu1.name = "hahaha"
stu1.gender = "男"
stu1.age = 30

# 获取对象信息
print(f"stu1.name = {stu1.name}")

# 2-成员方法
print("# =========== 2-成员方法 ===========")
# 设计一个类
class Student :
    # 成员变量
    name = None             # 学生姓名
    gender = None           # 性别
    age = None              # 年龄
    # 成员方法(其实就是类里面的内部函数)
    # self:代表类的内部变量,其实就是 self = Student()供函数内部调用
    def say_hi(self):
        print(f"你好 , 我是{self.name}")
    
    def say_hello(self , msg):
        print(f"你好 , 我是{self.name} , {msg}")

# 构建并且使用对象
stu1 = Student()
stu1.name = "lxl"
stu1.say_hi()
stu1.say_hello("哈哈哈")

# 3-类和对象
print("# =========== 3-类和对象 ===========")
# 构建类
class Clock:
    id = None
    price = None

    def ring(self):
        import winsound
        print("开始响铃")
        winsound.Beep(2000 , 100)
        print("结束响铃")

# 构建对象
clock1 = Clock()
clock1.id = 666
clock1.price = 19.99
print(f"clock1.id = {clock1.id} , clock1.price = {clock1.price}")
# clock1.ring()

# 4-构造方法
print("# =========== 4-构造方法 ===========")
# 设计一个类
class Student :
    # 成员变量
    name = None             # 学生姓名
    gender = None           # 性别
    age = None              # 年龄
    
    # __init__自动化执行函数
    def __init__(self , name , age , geder):
        self.name = name
        self.age = age
        self.geder = geder
        print("只要创建了一个对象,那么__init__函数就会自动运行,self后面的参数就是类()内的参数")

    # 成员方法
    def say_hi(self):
        print(f"你好 , 我是{self.name}")
    
    def say_hello(self , msg):
        print(f"你好 , 我是{self.name} , {msg}")

stu1 = Student("lxl" , 20 , "男")
stu1.say_hello("msg")

# 5-魔术方法
print("# =========== 5-魔术方法 ===========")

class Student:
    def __init__(self , name , age):
        self.name = name
        self.age = age
    # 1. 字符串方法
    # 其实就是print对象后能打印出有用的东西来,如果不使用__str__那么只能打印出类对象的地址,其实是没什么用的
    def __str__(self):
        return f"Student 类对象 , name:{self.name} , age{self.age}"
    # 2. __lt__小于符号比较方法:一般来说对象之间是不能比较的,但是加上__lt__方法就能提供比较的标准了,一般给小于号,后面也能比较大于
    def __lt__(self,other):
        return self.age < other.age
    # 3. 使用__le__就能比较>= 和 <=了
    def __le__(self , other):
        return self.age <= other.age
    # 3. __eq__实现比较是否相等
    def __eq__(self, other):
        return self.age == other.age

stu1 = Student("周杰伦" , 31)
stu2 = Student("林俊杰" , 32)
stu3 = Student("王力宏" , 33)
stu4 = Student("刘德华" , 33)

print(stu1 > stu2)
print(stu3 <= stu2)
print(stu3 == stu4)

# 6-封装
print("# =========== 6-封装 ===========")
# 私有成员变量和私有成员方法:
    # __作为开头就行了
class Phone:
    # 私有变量
    __current_V = None
    # 私有方法
    def __keep_single_core(self):
        print("私有变量")

phone = Phone()
# print(phone.__current_V)
# phone.__keep_single_core()

# 7-继承
print("# =========== 7-继承 ===========")
# 基于现有的类进行更新修改(继承)
class Phone:
    IMEI = None
    pro = "lxl"

    def call_by_4G(self):
        print("4G通话")

# 继承(新增)
class Phone2026(Phone):
    face_id = "10001"

    def call_by_5G(self):
        print("5G通话(继承更新功能)")

newPhone = Phone2026()
print(newPhone.face_id)
newPhone.call_by_4G()
newPhone.call_by_5G()

# 多继承
class NFC:
    NFCtype = "第5代"

    def read_NFC(self):
        print("NFC读卡")

    def write_NFC(self):
        print("NFC写卡")

class RC:
    RC_type = "第1代"

    def RC_Send(self):
        print("RC发射")
    def RC_Get(self):
        print("RC接收")

# 多继承操作,self是各个父类的共同self,父类参数相同的时候,顺序覆盖
class MyPhone(Phone2026 , NFC , RC):
    pass

myphone = MyPhone()
myphone.write_NFC()
print(myphone.face_id)

# 8-复写父类成员
print("# =========== 8-复写父类成员 ===========")
# 子类继承父类的成员属性和成员方法后,如果对其“不满意”，那么可以进行复写.
# 直接改就行(重定义,相当于当成新的就行)
# 还想访问原本的父类的参数就使用 
    # 1. super().原参数 调用原父类的
    # 2. 父类名.参数调用

# 9-类型注解:变量
print("# =========== 9-类型注解:变量 ===========")
# 在=前插入 :类型
# 基础数据类型注解
var_1: int  = 10
var_2: bool = True
var_3: str  = "str"

# 类对象类型注解
class H:
    pass
h: H = H()

# 基础容器类型注解
my_list: list = [2, 3, 5]
my_dict: dict[str , int] = {"lxl": 666}

# 在注释中类型注解
# type: int , 这样更方便
var_5 = 4         # type: int
my_tuple = (2 ,4) # type:tuple

# 10-类型注解:函数
print("# =========== 10-类型注解:函数 ===========")

def num_add(a:int , b:int): 
    print(a+b)

def func(data:list) -> list:
    print(f"return list")
    return data

num_add(2,4)
print(func([2,3,4]))

# 11-类型注解:union
print("# =========== 11-类型注解:union ===========")
# 作用:注解混合类型(一大堆不太好顺序声明)
# 必须先导包
from typing import Union
my_list:list[Union[int,str]] = [1 ,2 ,"lxl"]

# 12-多态
print("# =========== 12-多态 ===========")
# 总指挥只提供接口,孩子进行集成并且复写连接
class Control:
    def Cool(self):
        pass
    def Hot(self):
        pass
    def Ice(self):
        pass

class Medi(Control):
    def Cool(self):
        print("美的的冷却功能")
    def Hot(self):
        print("美的的暖气功能")
    def Ice(self):        
        print("美的的冰冷功能")

class Geli(Control):
    def Cool(self):
        print("格力的冷却功能")
    def Hot(self):
        print("格力的暖气功能")
    def Ice(self):        
        print("格力的冰冷功能")

# 外部调用
def COOL(control : Control):
    control.Cool()

medi = Medi()
geli = Geli()

COOL(medi)
COOL(geli)
