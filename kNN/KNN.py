# -*- coding:utf-8 -*-
# Created By zl

# import math
#
#
# def calcEuclideanDistance(x1, y1, x2, y2):
#     return math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))
#
#
# d_ag = calcEuclideanDistance(3, 104, 18, 90)
# d_bg = calcEuclideanDistance(2, 100, 18, 90)
# d_cg = calcEuclideanDistance(1, 81, 18, 90)
# d_dg = calcEuclideanDistance(101, 10, 18, 90)
# d_eg = calcEuclideanDistance(99, 5, 18, 90)
# d_fg = calcEuclideanDistance(98, 2, 18, 90)
# print("d_ag: %s, d_bg: %s, d_cg: %s, d_dg: %s, d_eg: %s, d_fg: %s" % (d_ag, d_bg, d_cg, d_dg, d_eg, d_fg))

from sklearn import neighbors

# 导入sklearn自带的数据集
from sklearn import datasets

# 创建KNN分类器
knn = neighbors.KNeighborsClassifier()

# 加载鸢尾花数据集
# 花萼长度，花萼宽度，花瓣长度，花瓣宽度4个属性
# 预测鸢尾花卉属于（Setosa，Versicolour，Virginica）三个种类中的哪一类
iris = datasets.load_iris()
# print(iris)

# 使用鸢尾花数据集训练KNN算法
knn.fit(iris.data, iris.target)
print(knn)

# 定义一个新的数据, 并使用训练好的KNN算法预测结果
newRecord = [[0.1, 0.2, 0.3, 0.4]]
predictedLabel = knn.predict(newRecord)
print(predictedLabel)
