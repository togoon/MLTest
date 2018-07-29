# -*- coding:utf-8 -*-
# Created By zl

# 4.1 数据处理 pandas
import pandas as pd
import numpy as np
from config.path import pandas_data_path

df = pd.read_csv(pandas_data_path)
print(df.head())  # 默认打印前5行, 可以使用head(10)指定行数

# 打印类型, 列名, 索引
print(type(df))
print(df.columns)
print(df.index)

# 根据索引获取第N行数据
print(df.loc[0])

# 筛选数学成绩大于80的记录
data = df.数学 > 80  # 等价于df['数学'], 这样获取到的是一个Series
print(data, type(data))
# 再套一层df, 就能获取到实际的数据
real_data = df[df.数学 > 80]
print(real_data)
# 复杂筛选, 语 数 外 都>90
r2 = df[(df.语文 > 90) & (df.数学 > 90) & (df.英文 > 90)]
print("R2:", r2)

# 排序
ds = df.sort_values(['数学']).head()
# 多列排序
ds2 = df.sort_values(['数学', '语文']).head()
print("Sort:", ds)
print("Sort2:", ds2)

# 数据访问
# 行, 下标从0开始
print("行:", df.loc[2])
# 支持切片
print("多行:", df.loc[:2])
# iloc与loc的区别: iloc是用的数字下标, loc用的是行索引, 当行索引被改写的时候, loc就必须用真正的索引名
# 后期出了ix方法, 合并了iloc和loc, 如果存在数字索引就使用数字索引, 如不不存在, 就使用从0开始的下标索引
print("New行:", df.ix[2])
# 注意, 当只访问一行的时候df[2]是错误的, 但是多行的时候df[:2],切片是可以的

# 列
df.数学
df['数学']
# 多列, 注意是2层括号
df[['数学', '语文']]

# 数组
print(df.values)
print(df.数学.values)


# 重点
# 根据数学是否>60分组
def func(score):
    if score > 60:
        return '及格'
    else:
        return '不及格'


df['数学分类'] = df.数学.map(func)
print(df.head())
# 可以写成lambda表达式的形式
# #if 条件为真的时候返回if前面内容，否则返回else后边的
f = lambda score: '及格' if score > 60 else '不及格'
print("Lambda:", df.语文.map(f))

# 对所有元素进行操作, 使用applymap
print("ApplyMap:", df.applymap(lambda x: str(x) + '_').head())

# apply, 根据多列/多行生成一个新的数据
df['new_score'] = df.apply(lambda x: x.数学 + x.语文, axis=1)
print(df.head())

# 删除 drop 记得删除列的时候要加axis=1
df = df.drop(['new_score'], axis=1)
print(df.head)

# pandas中的操作, 基本和Numpy中的二维数组的操作是一样的
