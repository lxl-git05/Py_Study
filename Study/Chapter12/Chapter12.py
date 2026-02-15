#-*-coding:utf-8-*-
print("======Chapter12======")

# 12-1 基础柱状图使用
print("# 12-1 基础柱状图使用")
# 1. 导入包
from pyecharts.charts import Bar , Timeline
from pyecharts.options import LabelOpts
# 2. 构建柱状图
bar1 = Bar()
bar2 = Bar()
bar3 = Bar()
# 3. 添加x轴数据
bar1.add_xaxis(["中国" , "美国" , "英国"])
bar2.add_xaxis(["中国" , "美国" , "英国"])
bar3.add_xaxis(["中国" , "美国" , "英国"])
# 4. 添加y轴数据
bar1.add_yaxis("GDP" , [30 , 20 , 10] , label_opts = LabelOpts(position="right"))
bar2.add_yaxis("GDP" , [20 , 10 , 40] , label_opts = LabelOpts(position="right"))
bar3.add_yaxis("GDP" , [10 , 90 , 80] , label_opts = LabelOpts(position="right"))

# 反转x y轴
bar1.reversal_axis()
bar2.reversal_axis()
bar3.reversal_axis()
# 数值标签放在右侧

# 时间轴
timeline = Timeline()
timeline.add(bar1 , "点1")
timeline.add(bar2 , "点2")
timeline.add(bar3 , "点3")
# 自动播放
timeline.add_schema(
    play_interval= 1000 ,
    is_timeline_show= True ,
    is_auto_play= True ,
    is_loop_play= True
)
# 时间线绘图
timeline.render("bar.html")
# 5. 绘图
# bar1.render("bar.html")

