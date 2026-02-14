#-*-coding:utf-8-*-
print("======Chapter10综合项目:疫情图标构建======")
# 思路
# 得到json文件,首先清除首尾垃圾数据,接着转换为py文件
# 根据层次递进选择需要的数据List
# 使用pyecharts进行折线图的绘制

'''
总结:
    其实绘制这种图像,最需要的是数据处理 + 图像绘制
        数据处理:
            对于一个含有垃圾值的json文件,先进行open读取,read转为字符串,然后开始处理
                去除垃圾,然后才能json.loads()转为正常dict字典,随后去到网站:
                https://www.bejson.com
                进行json格式观察,随后进行层次提取
        图像绘制:
            最重要的是模仿例程,其他的没了
'''

import json

# 读取文件
f_us = open("D:/github/2-1-Py_Projects/Py_Study/Study/Chapter10/data/us.txt" , "r" , encoding="UTF-8")
# read变成str,进行首尾垃圾数据处理
data_us = f_us.read()
# 首尾
data_us = data_us.split("(")[1] 
data_us = data_us[0:-2:1]
# 转换为py文件:dict
data_us = json.loads(data_us)
# 取出相应数据,最关键
list_x_us = data_us["data"][0]["trend"]["updateDate"][0:314:1]
list_y_us = data_us["data"][0]["trend"]["list"][3]["data"][0:314:1]

# 绘制图像

# 1. 导入包
from pyecharts.charts import Line
# 2. 创建折线图对象
line = Line()
# 3. 添加x轴坐标
line.add_xaxis(list_x_us)
# 4. 添加y轴坐标
line.add_yaxis("新增确诊" , list_y_us )
# 5. 生成
line.render()
