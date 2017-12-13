# -*- coding:utf-8 -*-
# Created By zl
# 复杂示例

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.datasets import make_blobs

# 设置随机种子为0, 这样每次随机出来的数据都是一样的
# scikit中的make_blobs方法常被用来生成聚类算法的测试数据 http://blog.csdn.net/u013066730/article/details/54314190
# make_blobs使用方法http://blog.csdn.net/ichuzhen/article/details/51768934
# 以下代码的意思是: 生成一个40行的数据集, 要生成的样本围绕2个中心点, random_state=0参数很重要,它指定了每次随机的种子,置为0可以让每次随机出的数据不变
# data表示生成的样本数据集, label表示对应的标签
data, label=make_blobs(n_samples=40, centers=2, random_state=0)

# 绘图 scatter是散点图(scatter释义:分散 散开的)
# X[:,0]是numpy中数组的一种写法，表示对一个二维数组，取该二维数组第一维中的所有数据，第二维中取第0个数据，直观来说，X[:,0]就是取所有行的第0个数据, X[:,1] 就是取所有行的第1个数据
plt.scatter(data[:, 0], data[:, 1], c=label)
plt.show()

clf=svm.SVC(kernel='linear')
clf.fit(data, label)
print(clf)

###############
"""
对于二维的分类函数, 可以写成f(x)=wx+b=0
因为x是二维平面的坐标, 所以w也是一个二维的向量
w0 . x + w1 . y + w3 = 0 <==> y= -(w0 / w1)x + (w3 / w1) 
"""

