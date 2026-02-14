#-*-coding:utf-8-*-
#  字符串工具

# 翻转
def str_reverse(s):
    return s[::-1]

# 切片
def substr(s , x , y):
    return s[x:y]


if __name__ == '__main__' :
    print(str_reverse("hello"))
    print(substr("hello" , 1 , 3))

