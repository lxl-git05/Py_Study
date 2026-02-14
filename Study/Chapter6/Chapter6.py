#-*-coding:utf-8-*-
print("======Chapter6======")

# 6-1 数据容器入门
print("# 6-1 数据容器入门")

# 6-2 列表的定义语法
print("# 6-2 列表的定义语法")

list1 = [1, "lxl", [ 2 , 3 ], True, 5]
print(list1)
print(type(list1))

# 6-3 列表的下标索引
print("# 6-3 列表的下标索引")

print(list1[0])
print(list1[-1])
print(list1[2])
print(list1[2][1])

# 6-4 列表的常用操作
print("# 6-4 列表的下标索引")
mylist = [1 , "666" , [2 , 3 , 4 , 5 ] , True ]

# 1. 查找索引
print(mylist.index("666"))

# 2. 修改下标索引值
mylist[0] = 0
print(mylist[0])

# 3. 插入元素
mylist.insert( 0 , 2 )

# 4. 追加元素
mylist.append([6 , 7])

# 5. 追加一批元素
add_list = [[8 , 9] , False]
mylist.extend(  add_list  )

# 6. 删除元素(下标法)
# 6.1
del mylist[1]
# 6.2
get = mylist.pop(2)
print(f"Get :{get}")

# 6. 删除元素(内容法,第一个内容)
mylist.remove('666')

# 7. 清空
# mylist.clear()

# 8. 统计某元素在列表中的数量
count = mylist.count(1)
print(f"count = {count}")

# 9. 统计列表内元素个数
print(f"len(mylist) = {len(mylist)}")

print(mylist)

# ===== 练习begin =====
# 定义列表,变量接收
mylist = [21, 25, 21, 23, 22, 20]
print(f"mylist = {mylist}")

# 追加
mylist.append(31)
# 追加
mylist.extend([29,33,30])
# 取出
mylist.pop(0)
# 取出
mylist.pop(-1)
# 查找
print(f"mylist.index(31) = {mylist.index(31)}")

print(f"mylist = {mylist}")
# ===== 练习end =====

# 6-5 list的遍历
print("# 6-5 list的遍历")

# while遍历
def list_while_func():
    mylist = [1 ,2 ,3 ,4 , "hahaha" , True]
    print(f"mylist = {mylist}")
    index = 0
    while(index < len(mylist)):
        print(f"index : {index} , param : {mylist[index]}")
        index += 1

list_while_func()

# for遍历
def list_for_func():
    mylist = [1 ,2 ,3 ,4 , "hahaha" , True]
    print(f"mylist = {mylist}")
    for x in mylist:
        print(f"param : {x}")

list_for_func()

# 6-6 元组的定义和操作
print("# 6-6 元组的定义和操作")
t1 = ( 1, "hello" , True)
t2 = ()
t3 = tuple()

print(t1 , type(t1))
print(t2 , type(t2))
print(t3 , type(t3))

# 定义单个元素的元组需要另加一个,
t4 = ("Hello")
print(f"t4:{t4}  \t type(t4):{type(t4)}" , )

t4 = ("Hello", )
print(f"t4:{t4}  \t type(t4):{type(t4)}" , )

# 嵌套
t5 = ((1 , 2, 3) , ( 4 , 5, 6))
print(t5)

# 下标索引取元素 , 与list一模一样
print(f"t5[1][2] = {t5[1][2]}")

t6 = (1, 2, 3, 4, 4, 5, 6)

# 查找元素的下标
print(f"t6的元素4的下标 {t6.index(4)}")
# 统计某个元素的个数
print(f"t6的元素3的个数 {t6.count(3)}")
# 统计元组的元素数量
print(f"t6的元素数量    {len(t6)}")

print(t6)

# 元组的遍历
def tuple_while_func():
    mytuple = (1 ,2 ,3 ,4 , "hahaha" , True)
    print(f"mytuple = {mytuple}")
    index = 0
    while(index < len(mytuple)):
        print(f"index : {index} , param : {mytuple[index]}")
        index += 1

tuple_while_func()

def tuple_for_func():
    mytuple = (1 ,2 ,3 ,4 , "hahaha" , True)
    print(f"mytuple = {mytuple}")
    for x in mytuple:
        print(f"Param : {x}")

tuple_for_func()


# 修改元组元素是不行的,但是可以修改元组里面的list
t7 = (1, 2, 3, 4, ['hello', 5, 6, 7], 8, 9)
print(f"t7 的元素为 : {t7}")
t7[4].append(100)
print(f"t7 的元素为 : {t7}")

# ===== 练习begin =====
print("# ===== 练习begin =====")
mytouple = ('lxl' , 11 , ["Hello" , "World"])
print(f"mytouple : {mytouple}")
# 查询其年龄所在的下标位置
print(f"age_pos = {mytouple.index('lxl')}")
# 查询学生的姓名
print(f"name = {mytouple[0]}")
# 删除学生爱好中的football
print(f"before : {mytouple}")

mytouple[2].pop(0)

print(f"after : {mytouple}")
# 增加爱好：coding到爱好list内
print(f"before : {mytouple}")

mytouple[2].append("coding")

print(f"after : {mytouple}")
# ===== 练习end =====

# 6-7 字符串的常见操作
print("# 6-7 字符串的常见操作")
# 000000000123456789
my_str = "lxl and lxlpython"
# 下标索取值
print(f"第2个:{my_str[2]}和第3个值:{my_str[3]}!")
# index
print(f"寻找 and 的下标: {my_str.index("and")}")
# replace
new_my_str = my_str.replace("l" , "L")
print(f"老的str:{my_str} , 替换后接收的str:{new_my_str}")
# split
new_my_str = my_str.split("l")
print(f"老的str:{my_str} , 替换后接收的str:{new_my_str} , 类型:{type(new_my_str)}")
# strip
# 不传参数,就会去除首尾空格
my_str = "  lxl and lxlPython and lxlC   "
my_str_strip = my_str.strip()
print(f"my_str : !{my_str}! , my_str.split() : !{my_str_strip}! , Type:{type(my_str_strip)}")

# 传参数,会去除设涉及参数的所有元素(只看首尾,被隔开就无能为力了)
my_str = "lxl and lxlPython and lxlC"
my_str_strip = my_str.strip("lxl")
print(f"my_str : !{my_str}! , my_str.split() : !{my_str_strip}! , Type:{type(my_str_strip)}")

# 统计字符出现次数
print(f"count l : {my_str.count('l')}")

# 统计string长度
print(f"len : {len(my_str)}")

def string_while_func():
    index = 0 
    # 0000000-012345678
    my_str = "lxl666 ! "
    print(f"my_str : {my_str}")
    while(index < len(my_str)):
        print(f"index : {index} , param : {my_str[index]}")
        index += 1
    
string_while_func()

def string_for_func():
    my_str = "lxl666 ! "
    print(f"my_str : {my_str}")
    for x in my_str :
        print(f"param : {x}")

string_for_func()

# ===== 练习begin =====
my_str = "itheima itcast boxuegu"
# 统计it字符个数
print(f"统计it字符个数 : {my_str.count("it")}")
# 空格替换为|
my_str_replace = my_str.replace(" " , "|")
print(f"原来 : {my_str} , 替换后: {my_str_replace}")
# 按照|分隔得到列表
my_str_list = my_str_replace.split("|")
print(f"原来 : {my_str_replace} , 分隔后: {my_str_list}")
# ===== 练习end =====

# 6-8 数据容器的切片操作
print("# 6-8 数据容器的切片操作")
mylist = [0, 1, 2, 3, 4, 5, 6]

result1 = mylist[1:4:1]
print(result1)

result1 = mylist[4:1:-1]
print(result1)

my_str = "lxl hha "
result2 = my_str[::2]
print(result2)

result2 = my_str[::-1]
print(result2)

# ===== 练习begin =====
my_str = "万过薪月, 员序程马黑来, nohtyP学"
my_str_heima = my_str.split(",")[1].strip()[-2::-1]
print(my_str_heima)
# ===== 练习end =====

# 6-9 集合的定义和操作
print("# 6-9 集合的定义和操作")
myset = {True, 2, 'lxl', 5}
print(myset)

# 常用操作:
# 添加新元素
myset.add("add")

# 移出元素
myset.remove(5)

# 取出元素
print(f"随机取出元素:{myset.pop()}")

# 清空
# myset.clear()

print(myset)

# 差集
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.difference(set2)

print(set1)
print(set2)
print(set3)

print("===")

# 消除差集
set1 = {1, 2, 3}
set2 = {1, 5, 6}

print(set1)
print(set2)
print("===")
# 合并
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.union(set2)

print(set1)
print(set2)
print(set3)

# len
# 遍历
# 不支持while(因为没有顺序)
set1 = {1, 2, 3, 4, 5}
for x in set1:
    print(x)

# 6-10 字典基础
print("# 6-10 字典基础")
mydict = {'a': 99, 'b': 66, 'c': 77}

# 索引:
print(f"a: {mydict['a']}")

print(mydict)

# 嵌套字典
mydict = {
    "a" : {
        "1":77 ,
        "2":88 , 
        "3":99
    } , 'b' : {
        "1":76 ,
        "2":66 , 
        "3":99
    } , 'c': {
        "1":87 ,
        "2":96 , 
        "3":69
    }
}

print(mydict)

print(f"{mydict['a']['1']}")

# 6-11 字典的常用操作
print("# 6-11 字典的常用操作")

# 新增元素和更新元素
    # 因为key不能相同,所以加入key和更新key都是一样的操作

mydict = {'a': 99, 'b': 66, 'c': 77}
# 新增
mydict['d'] = 00
# 修改
mydict['a'] = 98
# 删除
mydict.pop("a")
# 清空
# mydict.clear()
# 获取全部的key
print(f"mydict.keys() = {mydict.keys()}")
# 遍历:不支持while,因为没有序列
def dict_for_func():
    mydict = {'a': 99, 'b': 66, 'c': 77}
    for x in mydict:
        print(f"Key: {x}")

dict_for_func()
# 长度
print(f"len : {len(mydict)}")

print(mydict)

# ===== 练习begin =====
mydict = {"王力宏": {
    "部门" : "科技部",
    "工资" : 3000 ,
    "级别" : 1
} , "周杰伦": {
    "部门" : "市场部",
    "工资" : 5000 ,
    "级别" : 2
} , "林俊杰" : {
    "部门" : "市场部",
    "工资" : 7000 ,
    "级别" : 3
} , "张学友" : {
    "部门" : "科技部",
    "工资" : 4000 ,
    "级别" : 1
} , "刘德华" : {
    "部门" : "市场部",
    "工资" : 6000 ,
    "级别" : 2
}}

# 输出信息
print(f"当前信息如下: {mydict}")

# 进行操作
for x in mydict :
    if (mydict[x]["级别"] == 1):
        mydict[x]["级别"] += 1
        mydict[x]["工资"] += 1000

# 再次输出信息
print(f"加薪后信息如下: {mydict}")
# ===== 练习end =====

# 6-13 通用操作
print("# 6-13 通用操作")


