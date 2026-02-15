#-*-coding:utf-8-*-
print("======Chapter12综合案例======")
from pyecharts.charts import Bar , Timeline
from pyecharts.options import LabelOpts
# 数据处理
f = open("D:/github/2-1-Py_Projects/Py_Study/Study/Chapter12/data/data.csv" , "r" , encoding="UTF-8")
f.readline()    # 跳过第一条数据
list_all = []   # 构建总表
# 每一条信息的处理工作:将单行字符串转为list[year(int) , country(str) , data(亿,int)]
for line in f:
    # 得到一条list
    contry_list = line.strip().split(",")
    # list年份转化
    contry_list[0] = int(contry_list[0])
    # list的data进行str -> float
    contry_list_data = contry_list[2]
    if (contry_list_data.count("E")):
        data_list = contry_list_data.split("E+")
        contry_list_data = float(data_list[0]) * 10 **int(data_list[1]) / 1000000000
    else:
        contry_list_data = int(contry_list_data) / 1000000000
    contry_list[2] = contry_list_data
    # 加入总表
    list_all.append(contry_list)
f.close()
# 总表信息处理和图像绘制
year = 1960
timeline = Timeline()
while(year < 2020):
    # 每一年的数据处理
    list_year = []
    for list in list_all:
        if (list[0] == year):
            list_year.append(list)
    # 得到前8
    list_year.sort(key = lambda param : param[2] , reverse = True)
    list_year = list_year[0:8:1]
    list_year = list_year[::-1]
    # 拿取x轴数据:country , y轴数据:data
    list_country = []
    list_GDP     = []
    for x in list_year:
        list_country.append(x[1])
        list_GDP.append(x[2])
    # 构建图像
    bar = Bar()
    # 3. 添加x轴数据
    bar.add_xaxis(list_country)
    # 4. 添加y轴数据
    bar.add_yaxis("GDP" , list_GDP , label_opts = LabelOpts(position="right"))
    # 反转x y轴
    bar.reversal_axis()
    # 添加到时间轴
    timeline.add(bar , str(year))
    # 下一年
    year += 1

# 自动播放
timeline.add_schema(
    play_interval= 1000 ,
    is_timeline_show= True ,
    is_auto_play= True ,
    is_loop_play= True
)
# 时间线绘图
timeline.render("bar.html")
