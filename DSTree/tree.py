# -*- coding:utf-8 -*-
# Created By zl

from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import preprocessing
from sklearn import tree
import graphviz

allData = open(r"F:\PyWorkspace\pubdata\AllElectronics.csv", "r")

reader = csv.reader(allData)

headers = next(reader)

# print(headers)

featureList = []
labelList = []

for row in reader:
    labelList.append(row[len(row) - 1])
    rowDic = {}
    for i in range(1, len(row) - 1):
        rowDic[headers[i]] = row[i]

    featureList.append(rowDic)

# print(featureList)
# print(labelList)

# 使用DictVectorizer中的fit_transform, toarray()方法将dic变成矩阵(注意大小写问题)
vec = DictVectorizer()
dummyX = vec.fit_transform(featureList).toarray()

print("dummyX:" + str(dummyX))
# print(vec.get_feature_names())

# 使用LabelBinarizer中的fit_transform, 转换label
lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(labelList)
# print("dummyY:" + str(dummyY))

# 创建决策树, 指定使用ID3算法, criterion='entropy'(criterion:标准，准则, entropy:熵), 如果不指定, 默认使用CART算法, 基尼系数criterion="gini"
# http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier
clf = tree.DecisionTreeClassifier(criterion="entropy")
clf = clf.fit(dummyX, dummyY)

# 打印训练出来的决策树
print("Clf:" + str(clf))

# 因为接下来要使用Graphviz, 所以接下来一段文字说明安装Graphviz时遇到的坑
# 1. 不能直接通过python的pip install graphviz安装, 因为这个项目是用Anaconda管理的, 用默认的pip安装后照样提示找不到
# 2. 可以直接在本文件头部import graphviz, Pycharm会自动检测该包没有安装, 然后使用conda install, 这是最快捷的方式
# http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier
# http://blog.csdn.net/skyztttt/article/details/71601365
# 输出可视化模型到文件

dot_data = tree.export_graphviz(clf, feature_names=vec.get_feature_names(), out_file=None)
graph = graphviz.Source(dot_data)

# 直接render会报错, make sure the Graphviz executables are on your systems' PATH
# 下载https://graphviz.gitlab.io/_pages/Download/windows/graphviz-2.38.msi, 安装后把目录配置到PATH中, 需要重启电脑
graph.render("iris")

# 产生一行新的数据, 用于测试模型
# dummyX是一个矩阵, 采用二维数组的形式存储, 下边这行代码就是取数组第一行
oneRowX = dummyX[0, :]
print("oneRowX: " + str(oneRowX))

newRowX = oneRowX
newRowX[0] = 1
newRowX[2] = 0

# 如果不加下班这两句,会遇到错误 ValueError: Expected 2D array, got 1D array instead
# 这个错误是说算法的输入要求是二维矩阵, 不能是一维数组
newRowList = [newRowX]
print("newRowX: " + str(newRowList))

# 预测并打印预测结果
predictY = clf.predict(newRowList)
print("predictY:" + str(predictY))


