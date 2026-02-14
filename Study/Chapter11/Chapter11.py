#-*-coding:utf-8-*-
print("======Chapter11======")

# 11-1 基础地图使用
print("# 11-1 基础地图使用")
# 1. 导入模块
from pyecharts.charts import Map
# 2. 准备地图对象
map = Map()
# 3. 数据填充:由于视频跟不上平台变化,现在是list套list而不是list套tuple
data = [
    ["北京市",  99],
    ["上海市", 199],
    ["湖南省", 299],
    ["台湾省", 399],             # 建议写“台湾省”
    ["广东省", 499]
]
# 4. 数据与地图联通
map.add("测试地图" , data , "china") 
# 配置全局选项:可选,map.set_global_opts,记得导库,这里不搞了
# 5. 绘制图像
map.render("china_map.html")

# 11-2  ================== 国内疫情地图绘制 ==================
print("# 11-2 国内疫情地图绘制")
# 进行数据处理
f = open("D:/github/2-1-Py_Projects/Py_Study/Study/Chapter11/data/map.txt" , "r" , encoding="UTF-8")
# json的py的str格式转为py的dict格式
import json
data = json.loads(f.read())
# 寻找母列表
data = data["areaTree"][0]["children"]  # 所有省份的list集合
# 添加数据
map_data = []
map_data = []
for x in data:
    name = x["name"]
    # 手动补全后缀
    if name in ["北京", "天津", "上海", "重庆"]:
        name += "市"
    elif name in ["香港", "澳门"]:
        name += "特别行政区"
    elif name == "台湾":
        name = "台湾省"           
    elif name == "西藏":
        name = "西藏自治区"
    elif name == "新疆":
        name = "新疆维吾尔自治区"
    elif name == "内蒙古":
        name = "内蒙古自治区"
    elif name == "广西":
        name = "广西壮族自治区"
    else:
        name += "省"
    map_data.append([name, x["total"]["confirm"]])

print(map_data)
# 绘制图像
# 1. 导入模块
from pyecharts.charts import Map
# 2. 准备地图对象
map = Map()
# 3. 数据填充:由于视频跟不上平台变化,现在是list套list而不是list套tuple
# 就是 map_data
# 4. 数据与地图联通
map.add("疫情省份确诊图" , map_data , "china") 
# 配置全局选项:可选,map.set_global_opts,记得导库,这里不搞了
# 5. 绘制图像
map.render("china_map.html")
