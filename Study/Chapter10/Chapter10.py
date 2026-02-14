#-*-coding:utf-8-*-
print("======Chapter10======")
# 10-1 Json格式学习
print("# 10-1 Json格式学习")
import json

# 字典转换为JSON
data = [{"name":"lxl" , "age":20} , {"name":"zjl" , "age":40} , {"name":"esn" , "age":44}]
json_str = json.dumps(data)
print(f"json_str:{json_str} , type:{type(json_str)}")

# JSON 转换为 Python 数据类型
s = '[{"name": "lxl", "age": 20}, {"name": "zjl", "age": 40}, {"name": "esn", "age": 44}]'
l = json.loads(s)
print(f"py_str:{l} , type:{type(l)}")

# 10-2 pyecharts模块快速入门
print("# 10-2 pyecharts模块快速入门")
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












