import turtle
 
# 初始建立画布
turtle.screensize() #返回默认大小(500, 400

turtle.pensize() # 设置画笔的宽度；
 
turtle.pencolor()# 没有参数传入，返回当前画笔颜色，传入参数设置画笔颜色，可以是字符串如"green", "red",也可以是RGB 3元组。
 
turtle.speed(5)#设置画笔移动速度，画笔绘制的速度范围[0,10]整数，数字越大越快。

# 完成绘图,保持窗口打开
turtle.done()

'''
更多资料:
https://blog.csdn.net/weixin_64338372/article/details/128076908?ops_request_misc=elastic_search_misc&request_id=a7b8e5418fc6aeb68fdfc2b3fdc5cce9&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-128076908-null-null.142^v102^pc_search_result_base3&utm_term=turtle%E7%BB%98%E5%9B%BE&spm=1018.2226.3001.4187
'''