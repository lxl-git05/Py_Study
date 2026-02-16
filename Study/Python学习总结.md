[toc]

# 1. 基础知识

## 1-1 数据类型转换

- 万物皆可转字符串: `str(万物)`
- int 和 float 必须原本是数字才能转换

## 1-2 print输出

- ① 使用占位符 %s %d ... , 后续参数使用 %引出:
	- 精度控制: `m.n`
- ```python
  msg = "学习%s , 日期:%d" % (name , dete)
  print(msg)
  ```

- ② f"内容{变量}"   但是不进行精度控制 , 原本什么样就什么样
+ ```python
  print(f"学习{name} , 日期: {date}")
  ```

## 1-3 数据输入

- input(问题(string))函数
- 返回值都是str
- 需要得到数据的话需要进行数据类型转换

# 2. 基础语法

## 2-1 if else

```python
if 比较表达式 : 
	执行,记得缩进
elif 表达式:
	执行
else :
	执行
```

## 2-2 loop

### 2-2-1 while

```python
while(条件):
	执行
```

### 2-2-2 for

- range语句

- 语法:
	- range(n) : 得到 0 - n(不含) 的数据序列 , 总共还是n次循环
	- range(n1 , n2) : n1(含) - n2(不含) 数据序列
	- range(n1 , n2 , step ) : n1 - n2(不含) , 步进为step

```python
for 临时变量 in 待处理的数据集:
	执行代码
```

## 2-3 Function

### 2-3-1 基础语法

- 切记:变量的作用域, ==函数控制全局变量需要global声明!!!==

- 语法:

```python
def 函数名 (参数):
	函数体
	return 返回值
```

### 2-3-2 多返回值写法

- 多返回值

```c
def test_retuen():

    return 1, 2, 4
```

### 2-3-3 多参数写法

- 位置参数

- 关键字参数

- ==缺省参数(默认值)==

- **不定长参数:**

- 位置传递
```c
def fuc(*arg):
	执行
```

传进的所有参数都会被args变量收集，它会根据传进参数的位置==合并为一个元组(tuple)== args是元组类型，这就是位置传递

- 关键字传递

```c
def fuc(**kwargs):
	执行
```

注意：
参数是“键=值”形式的形式的情况下，所有的“键=值”都会被kwargs接受，同时会根据“键=值”==组成字典==

### 2-3-4 回调函数与匿名函数

#### 2-3-4-1 函数作为形参传递(回调函数)

- 其实类似C语言的回调函数

```c
def test(callback):
    print(f"date : 20260214")
    callback()
    
def Func():
    print("我是回调函数,我支持寒假延长")

test(Func)
```

#### 2-3-4-2 lambda匿名函数

- 语法

```python
lambda 传入参数：函数体(返回值) 
```

# 3. 数据容器

## 3-1 列表(list)

- 特点:
	- 有序
	- 值可直接更改

| 编号  | 使用方式              | 作用                           |
| --- | ----------------- | ---------------------------- |
| 1   | ==列表.append(元素)== | 向列表中追加一个元素                   |
| 2   | 列表.extend(容器)     | 将数据容器的内容依次取出，追加到列表尾部         |
| 3   | 列表.insert(下标, 元素) | 在指定下标处，插入指定的元素               |
| 4   | del 列表[下标]        | 删除列表指定下标元素                   |
| 5   | ==列表.pop(下标)==    | 删除列表指定下标元素                   |
| 6   | 列表.remove(元素)     | 从前向后，删除此元素第一个匹配项             |
| 7   | 列表.clear()        | 清空列表                         |
| 8   | ==列表.count(元素)==  | 统计此元素在列表中出现的次数               |
| 9   | ==列表.index(元素)==  | 查找指定元素在列表的下标 找不到报错ValueError |
| 10  | ==len(列表)==       | 统计容器内有多少元素                   |

## 3-2 元组(tuple)

- 特点
	- 可以看成是值不可修改的list
	- 但是元组内部的list是可以修改的

|编号|方法|作用|
|---|---|---|
|1|index()|查找某个数据，如果数据存在返回对应的下标，否则报错|
|2|count()|统计某个数据在当前元组出现的次数|
|3|len(元组)|统计元组内的元素个数|

## 3-3 集合(set)

- 特点
	- 不支持元素的重复
	- 元素无序

| 编号  | 操作                         | 说明                              |
| --- | -------------------------- | ------------------------------- |
| 1   | ==集合.add(元素)==             | 集合内添加一个元素                       |
| 2   | 集合.remove(元素)              | 移除集合内指定的元素                      |
| 3   | ==集合.pop()==               | 从集合中随机取出一个元素                    |
| 4   | 集合.clear()                 | 将集合清空                           |
| 5   | 集合1.difference(集合2)        | 得到一个新集合，内含2个集合的差集 原有的2个集合内容不变   |
| 6   | 集合1.difference_update(集合2) | 在集合1中，删除集合2中存在的元素 集合1被修改，集合2不变  |
| 7   | 集合1.union(集合2)             | 得到1个新集合，内含2个集合的全部元素 原有的2个集合内容不变 |
| 8   | ==len(集合)==                | 得到集合长度                          |

## 3-4 字典(dict)

- 特点
	- key : value
	- key不可以重复
	- key和value可以嵌套,key不能定义为dict , value可以定义为任何数据容器

| 编号  | 操作                  | 说明                           |
| --- | ------------------- | ---------------------------- |
| 1   | ==字典[Key]==         | 获取指定Key对应的Value值             |
| 2   | ==字典[Key] = Value== | 添加或更新键值对                     |
| 3   | 字典.pop(Key)         | 取出Key对应的Value并在字典内删除此Key的键值对 |
| 4   | 字典.clear()          | 清空字典                         |
| 5   | ==字典.keys()==       | 获取字典的全部Key，==可用于for循环遍历字典==  |
| 6   | ==len(字典)==         | 计算字典内的元素数量                   |
## 3-5 字符串(str)

### 3-5-1 字符串基础

- 三种定义法
	- 单引号
	- 双引号
	- 三引号: 如果不使用变量接收的话,那就是纯注释

- 字符串的拼接
	- 字符串间使用加号 " + " 进行拼接
	- 含有字符可以使用 , 内容进行一对一拼接
```python
print("使用加号" + "进行string拼接")

print("拼接非string:" , num1 , "像这样")
```

### 3-5-2 字符串操作

- ==字符串不可修改==!所以一般的操作都是返回一个新字符串,但是老的没变

- **字符串的替换**
	- 得到的返回值是新的,但是老的不变
		- 这也好理解,毕竟字符串不可修改,所以只能是返回新的值,但是老的不变
	- 语法
	- ```python
	  字符串.replace(str1 , str2)
	  ```
	  - 也就是将str1全部替换为str2

- ==**字符串的分割**==
	- 按照**指定的分隔符**字符串，将字符串划分为多个字符串，==并存入列表对象中==
	- 字符串本身不变，而是得到了一个列表对象
	- 语法
	- ```python
	  字符串.split(",")  # 以 , 作为分隔符
	  ```

- **字符串的规整操作**
	- 只看首尾,被隔开就无能为力了
	- 语法:
	- ```c
	  mystr.strip()
	  # 如果内容是空的,就除去mystr的首尾空格和\n\r
	  # 如果内容不是空的,就除去首尾含内容的量
	  ```

- 其他操作
	- `.count`
	- `len()`

## 3-6 通用操作

- max()
- min()
- 数据容器间的转换
	- 转为list or tuple
		- dict只会保留key
		- str每个char都被取出来
	- 转为字符串
		- 其实就是加上了"内容"
	- 转为集合
		- 顺序乱了
		- 其他的和list一样
		- 但是字符串内容会被去重
	- 转不了字典,因为字典要求键值对

- 通用排序功能
	- ```c
	  sorted(对象<,reverse = true>)
	  ```
	- return list对象
		- 使用函数返回list排序参考
	- dict的value丢失

| 功能                             | 描述                           |
| ------------------------------ | ---------------------------- |
| 通用for循环                        | 遍历容器（字典是遍历key）               |
| max                            | 容器内最大元素                      |
| min()                          | 容器内最小元素                      |
| len()                          | 容器元素个数                       |
| list()                         | 转换为列表                        |
| tuple()                        | 转换为元组                        |
| str()                          | 转换为字符串                       |
| set()                          | 转换为集合                        |
| ==sorted(序列, [reverse=True])== | 排序，reverse=True表示降序 得到排好序的列表 |

## 3-7 总结

| 列表   | 元组               | 字符串               | 集合        | 字典          |                                    |
| ---- | ---------------- | ----------------- | --------- | ----------- | ---------------------------------- |
| 元素数量 | 支持多个             | 支持多个              | 支持多个      | 支持多个        | 支持多个                               |
| 元素类型 | 任意               | 任意                | 仅字符       | 任意          | Key: ValueKey: 除字典外任意类型Value: 任意类型 |
| 下标索引 | 支持               | 支持                | 支持        | 不支持         | 不支持                                |
| 重复元素 | 支持               | 支持                | 支持        | 不支持         | 不支持                                |
| 可修改性 | 支持               | 不支持               | 不支持       | 支持          | 支持                                 |
| 数据有序 | 是                | 是                 | 是         | 否           | 否                                  |
| 使用场景 | 可修改、可重复的一批数据记录场景 | 不可修改、可重复的一批数据记录场景 | 一串字符的记录场景 | 不可重复的数据记录场景 | 以Key检索Value的数据记录场景                 |


# 4. 文件处理

## 4-1 open的三种方式

- 流程
	- 打开 
	- ==w / r / a==
		- w : 
			- 文件不存在 : 创建文件然后写入
			- 文件存在 : 把内容清空然后重新写入新内容
			- 
		- r :
			- 只读,注意读取光标的位置不会复位
		- a :
			- 与"w"不同
			- 文件不存在,创建,写入
			- 存在,不清空 , 直接追加(\n换行)
	- 关闭

```c
f = open(name , mode , encoding = ) # encoding需要使用关键字传参
```

```c
f.flush() # w后刷新
f.close() # 内置flush的功能
```


## 4-2 文件的基础操作

- 切记: **encoding =** "UTF-8" , 写漏一点都❌️

| 方法            | 返回类型      | 是否包含\n | 内存占用 | 适合场景   | 备注  |
| ------------- | --------- | ------ | ---- | ------ | --- |
| for line in f | str（逐行）   | ✔      | ⭐    | 大文件    | 含\n |
| readlines()   | list[str] | ✔      | ⭐⭐   | 小文件    | 含\n |
| read()        | str       | ✔      | ⭐⭐⭐  | 整体文本处理 |     |

- str清除\n:
	- str.strip()

| 功能                                    | 描述                       |
| ------------------------------------- | ------------------------ |
| file = open(文件名, mode, ==encoding===) | 打开文件得到文件对象               |
| 文件对象.read(num)                        | 读取指定长度字节 不指定num读取文件全部    |
| 文件对象.readline()                       | 读取一行                     |
| 文件对象.readlines()                      | 读取全部行，得到列表               |
| for line in 文件对象                      | for循环文件对象，一次循环得到一行数据     |
| 文件对象.close()                          | 关闭文件对象                   |
| with open() as f                      | 通过with open语法打开文件，可以自动关闭 |

# 5. 异常处理

- 捕获所有异常
```c
# 捕获所有异常
try :
    open("666" , "r" , encoding= "UTF-8")
except Exception as e :
    print(f"捕获所有异常:{e}")
```


- ==常用格式==
```c
try :
    open("666" , "r" , encoding= "UTF-8")
except Exception as e :
    print(f"捕获所有异常:{e}")
else:
    print("没有异常,执行代码")
finally:
    print("有没有异常都执行")
```



# 6. import模块与包

## 6-1 模块

- 模块导入区别:

```c
from time import *
// 那么可以使用sleep()

import time 
// 那么需要time.sleep()

import time as tm  // 改名罢了
// 那么需要tm.sleep()
```


- 自定义模块示例:

```python
#-*-coding:utf-8-*-

__all__ = ['add']   # import * 时只能all里面的才能被执行

def add(a , b):
    return a + b

def de(a , b):
    return a - b

if __name__ == '__main__' :
    print("=========== 当前在my_module模块测试中 ===========")
    print(f"add(1 , 2) = {add(1 , 2)}")
```


## 6-2 包

- 包导入示例

```c
# 第1种导入方法:
import my_package.my_module1
import my_package.my_module2

my_package.my_module1.print1()
my_package.my_module2.print2()

  
# 第2种导入方法:(习惯)
from my_package import my_module1, my_module2

my_module1.print1()
my_module2.print2()
```

- 自定义包
	- 其实就是一个文件夹,==里面必须有`__init__.py`空文件==标识这是一个py包,内含各种模块(module)

# 7. 类和对象

## 7-1 基础语法

- 其实类和对象是一个集合体,不止有变量,还有函数
	- 而C语言只有结构体,结构体是类的缩减版,只有变量

- 类
	- 成员变量
		- 公共变量(外部可以访问)
		- 私有变量("\_\_"前缀)
	- 成员方法(方法 = 函数)
		- 函数必须有`self`默认参数, 同时`self`也能作为类的实例在类里面的函数调用
		- 魔术方法
			- `__init__`方法: 创建一次对象会自动执行一次,可以用作初始化
			- `__lt__` + `__le__` + `__eq__`方法: 用于比较大小,用法看下面例子(建议使用return <号)
			- `__str__`方法: 使得打印对象的时候能调用这个函数的return值,而不是地址
			- 其他魔术方法
		- 成员方法(外部可调用)
			- 没啥可说的
		- 私有方法
			- `__`前缀


```python
class Student:
	# 成员变量
	name = None
	age  = None
	nation = None
	__ID = None  # 私有成员
	
	# 魔术方法:
	# 0. 创建对象自动执行一次的setup函数:(可以用于初始化)
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
    # 4. __eq__实现比较是否相等
    def __eq__(self, other):
        return self.age == other.age
	
	# 成员方法
	def say_hello(self):
		pass
	
	# 私有方法
	def __change_id(self , new_id):
		self.__id = new_id

# 创建对象及其使用
stu = Student("lxl" , 20)
stu.nation = "中国"
stu.say_hello()
```

## 7-2 类型注解

- 因为python的类型是根据承载的值来的,不像C语言是需要声明定义的,所以有时候编译器不知道变量是什么类型,无法给出提示,所以才有了类型注解
	- 格式
	- `: 类型`
 - 相关例子:
	- [6. 类型注解](Python类与对象/类与对象.md#6.%20类型注解)

## 7-3 继承,复写与多态

### 7-3-1 继承父类
- 其实就是基于父类进行功能的新增,复写等
	- 新增: 就增呗
	- 复写: 就写呗(可以复写变量和函数)
	- 还想访问原本父类的参数or函数
		- 父类名.参数调用 (Phone.pro)
		- super().原参数 调用原父类的 (super().pro)


```python
class Phone:
    IMEI = None
    pro = "lxl"
    
    def call_by_4G(self):
        print("4G通话")
        
# 继承(新增)
class Phone2026(Phone):
	pro = "lxl666"   #! 复写 !
    face_id = "10001"

    def call_by_5G(self):
        print("5G通话(继承更新功能)")
        
newPhone = Phone2026()
print(newPhone.face_id)
newPhone.call_by_4G()
newPhone.call_by_5G()
```


### 7-3-2 多继承

- 多继承操作,self是各个父类的共同self,父类参数相同的时候,顺序覆盖
	- ==(一个孩子引用多个父亲的功能)==


```python
class MyPhone(Phone2026 , NFC , RC):
    pass
    
myphone = MyPhone()
myphone.write_NFC()
print(myphone.face_id)
```


### 7-3-3 多态

- ==(多个孩子引用同一个父亲的接口)==

- 父亲只提供接口
- 孩子负责实现父亲的接口
- 后续进行功能调用使用父亲的接口作为形参
	- 但是真正实现的却是传入孩子的对象


- 使用行业标准: 形参
- 实际实现是各个厂商: 实际传入的参数

```python
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
```


# 8. 闭包与装饰器

## 8-1 闭包

+ 一句话:**解决外部变量容易被其他函数修改的问题**

- 闭包: 好处:inner==无需依赖外部全局变量(外部全局变量可以被任何方式访问)==,outer的logo**扮演了类似外部变量**的角色,使得==除开main调用outer()重新赋值外没有任何办法改变inner的"外部变量==logo"

- 内部函数改变outer的闭包全局变量: 使用nonlocal关键字修饰外部变量就可以修改了



```python
def outer(num1):

	def inner(num2):
		nonlocal num1
		# 操作
	
	return inner
	
# 外部调用
fn = outer(100)  # fn是函数,其实就是inner,inner的全局变量是闭包的num1,只能内部调用且为静态
fn(20)
fn(30)
```

## 8-2 装饰器

装饰器就是使用创建一个闭包函数在闭包函数内调用目标函数
  可以达到不改动目标函数的同时，增加额外的功能。

两种使用方式

```python
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
```

# 9. 单例模式 工厂模式

## 9-1 单例模式

+ 其实就是一个类只有一个实例(对象)
	+ 也就是C语言的一个结构体只声明给一个变量,然后其他函数全局调用这个变量
	+ 所以任何调用该实例的操作的都是公共的相同的资源
	+ 节省资源
+ 其实就是一个类只有一个实例(真对象),后续多少"对象"都共用相同的静态实例(都只调用这个对象,其实有点像全局变量的效果)



## 9-2 工厂模式

+ ==在大工程很好用==
	- 给大批量的变量提供一个统一接口,容易维护

+ 示例演示

```python
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
# 地址不同,是不同个体
print(Worker1)
print(Worker2)

Teacher1 = pf.get_person('t')
Student1 = pf.get_person('s')
```

# 10. Python的拓展方向基础

## 10-1 Python数据绘图

+ `pyechart`入门
	+ 其实不难,看例程照着写就行了
	+ 美化图表看官方API

### 10-1-0 简单的数据处理

+ ==Json与Py数据格式的互转==
	- json转为py其实就是:
		- ==**字符串格式的json**(File文件操作read得来)进行json.loads()转换为py的字典,然后剩下的就交给py进行数据处理==
	- py转json就是`json.dumps(data)`

+ ==列表sort排序==
- **语法:** 
	- `列表.sort(key=选择排序依据的函数,reverse=True|False)`
	- 参数key，是要求传入一个函数，表示将列表的每一个元素都传入函数中，返回排序的依据
	- 参数reverse，是否反转排序结果，True表示降序，False表示升序

### 10-1-1 折线图

- 模仿例程即可:
```python
# 1. 导入包
from pyecharts.charts import Line
# 2. 创建折线图对象
line = Line()
# 3. 添加x轴坐标
line.add_xaxis(["中国" , "美国" , "英国"])
# 4. 添加y轴坐标
line.add_yaxis("GDP" , [60 , 70 , 90] )
# 5. 生成
line.render()
```

### 10-1-2 地图

```python
# 1. 导入模块
from pyecharts.charts import Map
# 2. 准备地图对象
map = Map()
# 3. 数据填充:由于视频跟不上平台变化,现在是list套list而不是list套tuple
data = [
    ["北京市",  99],
    ["上海市", 199],
    ["湖南省", 299],
    ["台湾省", 399],             # 建议写“台湾省”
    ["广东省", 499]
]
# 4. 数据与地图联通
map.add("测试地图" , data , "china")
# 配置全局选项:可选,map.set_global_opts,记得导库,这里不搞了
# 5. 绘制图像
map.render("china_map.html")
```

### 10-1-3 柱状图

```python
# 1. 导入包
from pyecharts.charts import Bar , Timeline
from pyecharts.options import LabelOpts
# 2. 构建柱状图
bar = Bar()
# 3. 添加x轴数据
bar.add_xaxis(["中国" , "美国" , "英国"])
# 4. 添加y轴数据
bar.add_yaxis("GDP" , [30 , 20 , 10] , label_opts = LabelOpts(position="right"))
# 反转x y轴
bar.reversal_axis()
# 5. 绘图
bar.render("bar.html")
```

## 10-3 多线程任务

+ 直接上示例代码
	+ 创建任务
		+ **要在while死循环**
		+ **需要延迟休息,不能一直占用资源**
	+ 创建线程
		+ 两种传参方式
			+ 元组传参
			+ 字典传参
	+ 开启线程

```python
print("# ========= 进程和线程-多线程 =========")

import time
import threading    # 多线程

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
task1_thread.start()
task2_thread.start()
```

## 10-4 网络编程

### 10-4-1 服务端示例

```python
print("# ========= 网络编程:服务端 =========")
import socket
# ================== 初始化连接 ==================
# 创建socket对象
socket_server = socket.socket()
# 绑定IP地址和端口
socket_server.bind(  ("localhost" , 8888)  )
# 监听端口:传入参数:允许连接的数量
socket_server.listen(1)
# 等待客户端连接
result = socket_server.accept( )
conn = result[0]    # 客户端和服务端的连接对象
address = result[1] # 客户端的地址信息
# accept()是阻塞式方法(一直阻塞)
print(f"连接成功,地址信息:{address}")

# ================== 信息收发 ==================
while True:
    # 接收 客户端消息(使用conn)
    data:str = conn.recv(1024).decode("UTF-8")  # 缓冲区,解码形式
    print(f"客户端消息:{data}")
  
    # 回复 消息
    msg = input("请输入回复消息").encode("UTF-8")
    print(f"打印的是{msg}")
    if (msg == b'exit'): # 退出对话,str前面加个b
        break
    conn.send(msg)

# ================== 关闭连接 ==================
conn.close()
socket_server.close()
```

### 10-4-2 客户端示例

```python
print("# ========= 网络编程:客户端 =========")
import socket
# ================== 初始化连接 ==================
# 创建对象
socket_clinet = socket.socket()
# 链接到服务器
socket_clinet.connect( ("localhost" , 8888) )

# ================== 信息收发,后续可以套上while =================
# 发送消息,服务端需要使用conn地址,地址会变,但是客户端就不需要
socket_clinet.send("你好".encode("UTF-8"))
# 接收返回信息
rec = socket_clinet.recv(1024).decode("UTF-8")
print(f"接收信息:{rec}")

# ================== 关闭连接 =================
socket_clinet.close()
```

## 10-5 正则表达式

### 10-5-1 基础匹配-字符串搜寻匹配

正则表达式，又称规则表达式（RegularExpression），是使用==单个字符串来描述、匹配某个句法规则的字符串==，常被用来检索、替换那些符合某个模式（规则）的文本。

- 三个基础方法
	- `re.match('目标字符串' , str)`
		- 从被匹配字符串==开头(仅看开头)==进行匹配，匹配成功返回匹配对象（包含匹配的信息），匹配不成功返回空。
	- `re.search('目标字符串' , str)`
		- 从前往后寻找到第一个
	- findall匹配:从前往后寻找,返回全部

 + 案例

```python
import re   # 正则表达式
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
```

### 10-5-2 元字符匹配

- 使用的函数仍然是前面3个,搭配后面的匹配规则

- 注意:!!!
	- ==不要留任何空格,拧巴一点写==

- 字符匹配

|字符|功能|
|---|---|
|.|匹配任意1个字符（除了\n），\．匹配点本身|
|[]|匹配[]中列举的字符|
|\d|匹配数字，即0-9|
|\D|匹配非数字|
|\s|匹配空白，即空格、tab键|
|\S|匹配非空白|
|\w|匹配单词字符，即a-z、A-Z、0-9、_|
|\W|匹配非单词字符|
- \[\]内部是匹配范围,比如
	- \[a-zA-Z0-9\] 表示匹配所有字母和数字

- 数量匹配

|字符|功能|
|---|---|
|*|匹配前一个规则的字符出现0至无数次|
|+|匹配前一个规则的字符出现1至无数次|
|?|匹配前一个规则的字符出现0次或1次|
|{m}|匹配前一个规则的字符出现m次|
|{m,}|匹配前一个规则的字符出现最少m次|
|{m,n}|匹配前一个规则的字符出现m到n次|

- 边界匹配

| 字符  | 功能        |
| --- | --------- |
| ^   | 匹配字符串开头   |
| $   | 匹配字符串结尾   |
| \b  | 匹配一个单词的边界 |
| \B  | 匹配非单词边界   |

- 分组匹配

|字符|功能|
|---|---|
|\||匹配左右任意一个表达式|
|（）|将括号中字符作为一个分组|
