#-*-coding:utf-8-*-
print("======MySQL综合案例======")
# 项目思路
    # 1. 初始化
    # 2. MySQL创建库,然后创建表
    # 3. 引入数据处理,然后插入数据到表中
    # 4. 关闭MySQL

# ======== 1. 初始化 ========
# 创建到MySQL的数据库链接
from pymysql import Connection
# 构建到MySQL数据库的链接
conn = Connection(
    host="localhost",   # 主机名
    port=3306,          # 端口
    user="root",        # 账户
    password="123456",  # 密码
    autocommit=True     # 自动提交
)
# 看看连接成功没有
print(conn.get_server_info())
# 获取游标对象
cursor = conn.cursor()

# ======== 2. MySQL创建库,然后创建表 ========
# 创建数据库
try :
    cursor.execute("create database pysql charset UTF8 ;")
except Exception as e:
    print(f"{e}")
    print("库已被创建,无法重复创建")
# 选择数据库
conn.select_db("pysql")
# 在新建的库中新建表
try:
    cursor.execute("create table orders(order_date DATE, order_id varchar(255) , money INT , province varchar(10));")
except Exception as e:
    print(f"{e}")
    print("相同的表不能重复创建")

# ======== 3. 引入数据处理,然后插入数据到表中 ========
import json
# 1-1 读取1月份数据
def month1_data_deal(address: str) -> dict:
    # 数据存储的字典:1月
    dict = {}
    # 数据处理
    try :
        f = open(address , "r" , encoding="UTF-8")
    except Exception as e:
        print(f"文件读取失败,出现的问题:{e}")
    else:
        for line in f:
            line = line.strip().split(",")
            # 将数据进行 事件:总量++的格式使用字典接收
            try :
                dict[line[0]] += int(line[2]) 
            except:
                dict[line[0]]  = int(line[2]) 
    finally:
        if (f != None):
            f.close()
        return dict

# 1-2 读取2月份数据
def month2_data_deal(address: str) -> dict:
    dict = {}
    try :
        f = open(address , "r" , encoding="UTF-8")
    except Exception as e:
        print(f"文件读取失败,出现的问题:{e}")
    else:
        for line in f :
            line = json.loads(line) # 得到本行的字典值
            try:
                dict[line['date']] += line['money']
            except:
                dict[line['date']]  = line['money']
    finally:
        if (f != None):
            f.close()
        return dict

# 1-3 构建数据字典 date + money
dict_1 = month1_data_deal("Study/Class-MySQL/2-MySQL/data/2011-1.txt")
dict_2 = month2_data_deal("Study/Class-MySQL/2-MySQL/data/2011-2-json.txt")
dict_total = {}
for key in dict_1 :
    dict_total[key] = dict_1[key]
for key in dict_2 :
    dict_total[key] = dict_2[key]

# 插入数据到数据表中
str_send = "insert into orders(order_date, money) values "
for key in dict_total :
    str_send += "('" + str(key) + "'," + str(dict_total[key]) + "),"
str_send = str_send[:-1:1] + ";"
print(str_send)
# cursor.execute(str_send)  # 成功实现
# ======== 4.关闭MySQL ========
conn.close()
