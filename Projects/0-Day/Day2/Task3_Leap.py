"""

输入年份 如果是闰年输出True 否则输出False

Version: 0.1
Author: lxl
Date: 2025-12-1

"""
year = int(input("请输入年份："))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("是闰年")
else:
    print("不是闰年")
