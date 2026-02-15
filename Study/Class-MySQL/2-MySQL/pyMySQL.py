#-*-coding:utf-8-*-
print("======MySQL======")

# 创建到MySQL的数据库链接
from pymysql import Connection
# 构建到MySQL数据库的链接
conn = Connection(
    host="localhost",   # 主机名
    port=3306,          # 端口
    user="root",        # 账户
    password="123456",  # 密码
    autocommit=True     # 自动提交
)
# 看看连接成功没有
print(conn.get_server_info())
# 获取游标对象
cursor = conn.cursor()

# ========== 执行非查询性质SQL:创建库+表 ==========
# 选择数据库
conn.select_db("test")
# cursor.execute("create table test_pymysql(id int);")

# ========== 执行查询性质SQL ==========
conn.select_db("world") # 选择数据库
cursor.execute("select * from student;")
# 拿取查询性质SQL结果
result = cursor.fetchall()
print(result)

# ========== 插入数据 ==========
conn.select_db("world") # 选择数据库
# cursor.execute("insert into student values(6,'韩红',62,'女');")
# conn.commit()         # 手动确认
# 关闭连接
conn.close()