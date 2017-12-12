# -*- coding:utf-8 -*-
# Created By zl

from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import preprocessing
from sklearn import tree
import graphviz

## 此文档对应麦子学院(基础2)机器学习深度学习基础, 第三节决策树AllElectronics.py
# rb是Python open命令的参数, 表示以二进制读模式打开文件, 源代码有问题, 不能使用rb, 因为next(reader)要求是txt, 只能使用r
# https://www.cnblogs.com/dkblog/archive/2011/02/24/1980651.html
# 文件路径前加r是表示字符串中的字符不进行转义, 如果不带r, 路径中如果有\t, 就会转义为制表符
# https://www.cnblogs.com/cyiner/archive/2011/09/18/2180729.html
allData = open(r"F:\PyWorkspace\pubdata\AllElectronics.csv", "r")

reader = csv.reader(allData)

# headers = reader.next()
# Python2 才有此方法, Python3使用如下方法
# headers就是csv文件的标题行
# 请注意: next方法在取出第一行数据的同时, 已经将指针指向第二行了
headers = next(reader)

# print(headers)


# scikit learn要求所有属性和label的值都必须是数值型, 而不是能是字符, 所以使用决策树之前要做数据转换
featureList = []
labelList = []

# 如何处理数据???
# 将每一个属性的所有取值变成一个向量, 那么对于单一属性值, 就可以转换成行向量
# 例如 对于age来说, 它的取值范围是青年 中年 老, 那么对于第一行的数据youth就转换成1  0  0
# 同理将收入high也转换成 1  0  0
# 最终['1', 'youth',   'high',  'no',  'fair', 'no']转化成一个向量x
#           (1, 0, 0,  1, 0, 0, 0, 1,  1, 0,   0)
# skt里边带有一个包, 帮助我们转化数据
for row in reader:
    # 将最后的一列, 放入Label列表中
    labelList.append(row[len(row) - 1])
    rowDic = {}
    for i in range(1, len(row) - 1):
        # 将属性名称和对应的值放入字典
        # age = youth, income = high
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


