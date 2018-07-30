# -*- coding:utf-8 -*-
# Created By zl

# 5 Titanic数据处理与分析
# [Titanic数据分析报告](https://blog.csdn.net/csqazwsxedc/article/details/51336798)
# 数据集中共有12个字段，
# PassengerId：乘客编号，
# Survived：乘客是否存活，
# Pclass：乘客所在的船舱等级；
# Name：乘客姓名，
# Sex：乘客性别，
# Age：乘客年龄，
# SibSp：乘客的兄弟姐妹和配偶数量，
# Parch：乘客的父母与子女数量，
# Ticket：票的编号，
# Fare：票价，
# Cabin：座位号，
# Embarked：乘客登船码头

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

from config.path import titanic_test_path
from config.path import titanic_train_path

# 不加这句的话, 控制台输出会换行
pd.set_option('display.width', 1000)

titanic = pd.read_csv(titanic_train_path)
print(titanic.head())

# 打印数据的统计信息
# info:
# describe: 对所有数值字段进行统计
# print(titanic.info())
print(titanic.describe())

# 重要, 统计数据中空值的个数
print("Null Count:", titanic.isnull().sum())

# 替换所有空值为0
# titanic.fillna(0)
# 替换Age里的空值为0
# titanic.Age.fillna(0)

# 处理年龄数据
# 先取年龄的中位数
age_m = titanic.Age.median()
print(age_m)
# 按年龄中位数填充, fillna返回的是一个Series, 需要对titanic重新赋值
titanic.Age.fillna(age_m)
# inplace=True表示直接填充, 改变原值
titanic.Age.fillna(age_m, inplace=True)
# 再次统计Age的空值
print("After FillNA:", titanic.isnull().sum())
"""
# 分析
# 首先尝试从性别进行分析
# 简单统计性别中不同值的个数
print(titanic.Sex.value_counts())
# 分开统计男女在是否获救中的比例
survived = titanic[titanic.Survived == 1].Sex.value_counts()
unsurvived = titanic[titanic.Survived == 0].Sex.value_counts()
print("获救:", survived)
print("未获救:", unsurvived)

# 使用pandas自带的绘图函数绘制柱状图
df = pd.DataFrame([survived, unsurvived], index=['survived', 'unsurvived'])
df.plot.bar() # 等价于 df.plot(kind='bar')
plt.show()
# 以上绘图成功, 但是不是我们想要的效果
# 将df转置一下
df = df.T
df.plot.bar()
plt.show()
# 进一步显示堆叠图
df.plot(kind='bar', stacked=True)
plt.show()
# 再进一步, 显示百分比堆叠图
# 首先算出百分比加入df中, 形成新的2列
df['p_survived']= df.survived / (df.survived + df.unsurvived)
df['p_unsurvived']= df.unsurvived / (df.survived + df.unsurvived)
print(df)
# 取出百分比的2列, 作图
df[['p_survived', 'p_unsurvived']].plot(kind='bar', stacked=True)
plt.show()

# 以下从年龄的角度进行分析
print("Age Counts:", titanic.Age.value_counts())

survived = titanic[titanic['Survived']==1]['Age']
unsurvived = titanic[titanic['Survived']==0]['Age']

df = pd.DataFrame([survived, unsurvived], index=['survived', 'unsurvived'])
df = df.T
print(df.head())

# 画直方图, bins用来控制直方图柱子的个数
df.plot(kind='hist', stacked=True, bins=30) # 中间一个特别高, 是因为我们把空值都替换为了中位数
plt.show()

# 重要: 直方图不够直观, 此时画密度图
df.plot(kind='kde')
plt.show()
# 可以调用describe函数, 看一下年龄的范围, 密度图X轴与实际数据范围不符
print(titanic['Age'].describe())
# 限制X取值范围
df.plot(kind='kde', xlim=[0, 80], ylim=[0, 0.05])
plt.show()

# 可以对年龄先分段, 然后再处理、绘图
age = 16
young = titanic[titanic['Age']<age]['Survived'].value_counts()
old = titanic[titanic['Age']>=age]['Survived'].value_counts()
df = pd.DataFrame([young, old], index=['young', 'old'])
df =df.T
print(df)
df.plot.bar()
plt.show()

# 分析票价
survived = titanic[titanic['Survived']==1]['Fare']
unsurvived = titanic[titanic['Survived']==0]['Fare']
df = pd.DataFrame([survived, unsurvived], index=['survived', 'unsurvived'])
df = df.T
print(titanic['Fare'].describe())
df.plot(kind='kde', xlim=[0, 513])
plt.show()
# 由上图可以看出, 票价低的生还率较低


# 组合特征
# 分析年龄+票价, 对生还率的影响
# 使用plt绘制散点图, scatter
ax = plt.subplot()

# 生还者
x = titanic[titanic.Survived==1].Age
y = titanic[titanic.Survived==1].Fare
plt.scatter(x, y, s= 10, c='red')
# 未生还者
x = titanic[titanic.Survived==0].Age
y = titanic[titanic.Survived==0].Fare
plt.scatter(x, y, s= 10, c='green')
plt.legend(['survived','unsurvived'])
ax.set_xlabel('age')
ax.set_ylabel('fare')
plt.show()
"""

# 隐含特征
# 截取姓名中的Mr Miss等
titanic['title']=titanic['Name'].apply(lambda name: name.split(',')[1].split('.')[0].strip())
print(titanic['title'].value_counts())