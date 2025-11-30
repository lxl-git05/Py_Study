# Python环境配置与包安装

[toc]

## 1. 环境配置

参考资料:

[`【Conda+vsCode】vsCode 中使用 conda 配置虚拟环境_vscode conda-CSDN博客`](https://blog.csdn.net/weixin_54383080/article/details/138613865?ops_request_misc=elastic_search_misc&request_id=f679bcd2783e218e9ab9e3d23613f073&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~baidu_landing_v2~default-5-138613865-null-null.142^v102^pc_search_result_base3&utm_term=vscode搭配conda环境&spm=1018.2226.3001.4187)

## 2. 环境指令

### 2-1 查看当前环境的库

```c
pip list	
# 或者是
conda list
```



### 2-2 **安装库**

```c
pip install numpy

# 或者
    
conda install numpy
```

区别:

**`pip`** → Python 官方库

**`conda`** → 带 C/C++ 库的科学计算包更方便



### 2-3 requirements.txt（项目依赖导出）

未来写项目要告诉别人你用了哪些包：

```
pip freeze > requirements.txt
```

别人安装：

```
pip install -r requirements.txt
```

这是团队协作、提交 GitHub 的基础能力。