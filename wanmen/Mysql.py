# -*- coding:utf-8 -*-
# Created By zl

# 3.1 Python 操作mysql
## 推荐Python数据结构可视化工具: http://www.pythontutor.com/live.html#mode=edit

# json
import json

d1 = '{"a":100, "b":200}'
d2 = "{'a':100, 'b':200}"

# json.loads(d2)# 这样写会报错json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes
json.loads(d1)

# 因此, json里需要用双引号

# Python 操作Mysql
# 左侧项目列表中External Libraries中查找Anaconda的版本, 发现是3
# 开始菜单里找到Anaconda3--Anaconda Pormpt--conda install xxx
# mysql-python是python2.6版本的包名, python3要使用conda install mysqlclient

import MySQLdb

DATABASE = {
    'host': '192.168.5.135',
    'database': 'dmp',
    'user': 'openapi',
    'password': 'openapi',
    'charset': 'utf8'
}

# 打开数据库连接
#db = MySQLdb.connect("192.168.5.135", "openapi", "openapi", "dmp", charset='utf8' )
db = MySQLdb.connect(**DATABASE)


# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 执行一个查询
sql = "select * from role"
cursor.execute(sql)

# 获取查询结果
res = cursor.fetchall()

# 打印结果
for r in res:
    print(r)

# 插入操作
db.autocommit(False)
sql = "insert into role(name) values('test')"
cursor.execute(sql)
db.commit()

# 删除操作
sql="delete from role where name='test';"
cursor.execute(sql)
db.commit()

# 异常捕获
try:
    1 + 'hello'
except Exception as e:
    print(e)
    db.rollback()

db.close()