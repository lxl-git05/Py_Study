#-*-coding:utf-8-*-
print("======Class======")
# 思路:
# 1. 读取数据
    # 处理1月,得到每日账单字典
    # 处理2月,得到每日账单字典
    # 字典合并,后续可以轻松得到x-y数据列表
# 2. 绘制图像
    # x数据 : 日期
    # y数据 : 每日销售额
# 3. 整体封装实现:
    # 账单处理函数,返回字典,try
    # 图像绘制函数,输入x,y列表,绘制图像
    # 记得写类型注解和try尝试操作

# 全局变量
import json
f = None            # 文件读取
dict_1 = {}         # 数据存储的字典:1月
dict_2 = {}         # 数据存储的字典:2月
dict_total = {}     # 1月和2月的字典集合

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

# 1-3 字典合并

dict_1 = month1_data_deal("Study/Class-MySQL/1-Class/data/2011-1.txt")
dict_2 = month2_data_deal("Study/Class-MySQL/1-Class/Class-Zonghe.py")

for key in dict_1 :
    dict_total[key] = dict_1[key]
for key in dict_2 :
    dict_total[key] = dict_2[key]

def draw_bar_func(bar_x :list, bar_y :list, title:str):
    # 3-1 导入包
    from pyecharts.charts import Bar
    from pyecharts  import options as opts
    # 3-2 创建折线图对象
    bar = Bar()
    # 3-3 添加x轴坐标
    bar.add_xaxis(bar_x)
    # 3-4 添加y轴坐标
    bar.add_yaxis(title , bar_y )
    # 3-5 生成
    bar.render("bar.html")


# 2.绘制图像
list_bar_x = []
list_bar_y = []

# 2-1 x数据:日期
for key in dict_total:
    list_bar_x.append(key)

# 2-2 y数据:每日销售额
for key in dict_total:
    list_bar_y.append(dict_total[key])

# 3. 绘制图像
draw_bar_func(list_bar_x , list_bar_y , "每日销售额")
