# -*- coding:utf-8 -*-
# Created By zl

# 多元线性回归

from numpy import genfromtxt
import numpy as np
from sklearn import datasets, linear_model

dataPath = r"F:\PyWorkspace\github\MLTest\PubData\Delivery.csv"
# genfromtxt 默认会把数据转为浮点数, 所以打印出来的整数后边都有"."
deliveryData = genfromtxt(dataPath, delimiter=',')

print("Data:", deliveryData)

# 冒号表示所有, 即取所有行, -1表示倒数第一列, :-1是左闭右开区间,不包含最后一列
X = deliveryData[:, :-1]
# 取所有行的最后一列
Y = deliveryData[:, -1]

print("X:", X)
print("Y:", Y)

regr = linear_model.LinearRegression()

regr.fit(X, Y)

# 每个x对应的前边的系数
print(regr.coef_)
# 截距
print(regr.intercept_)

t_tmp = [[102, 6]]

Y_tmp = regr.predict(t_tmp)
print("Result:", Y_tmp)
