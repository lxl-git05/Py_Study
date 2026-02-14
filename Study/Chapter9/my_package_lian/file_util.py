#-*-coding:utf-8-*-
# 文件处理相关工具

def print_file_info(file_name):
    f = None 
    try :
        f = open(file_name , "r" , encoding="UTF-8")
    except Exception as e :
        print(f"出现问题,问题为:{e}")
    else :
        print(f.read())
    finally:
        if (f):
            f.close()

def append_to_file(file_name , data):
    f = None
    try :
        f = open(file_name , "a" , encoding="UTF-8")
    except Exception as e :
        print(f"出现问题,问题为:{e}")
    else :
        f.write(data)
    finally:
        if (f):
            f.close()

if __name__ == '__main__' :
    # print_file_info("666")
    print_file_info("D:/github/2-1-Py_Projects/Py_Study/Study/Chapter9/9-lian.txt")
    append_to_file("D:/github/2-1-Py_Projects/Py_Study/Study/Chapter9/9-lian.txt" , "新增数据\n")
