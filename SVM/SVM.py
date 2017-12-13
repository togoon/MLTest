# -*- coding:utf-8 -*-
# Created By zl

from sklearn import svm

x = [[1, 1], [2, 3], [2, 0]]
y = [0, 1, 0]

# Support Vector Machine for classification
# http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC
clf = svm.SVC(kernel='linear')
clf.fit(x, y)
# 打印模型参数
print(clf)
# 打印出支持向量
print(clf.support_vectors_)
# 打印出支撑点在数据集中的下标
print(clf.support_)
# 打印出一共有几个支撑点
print(clf.n_support_)


newLine = [[2.5, 1.5]]
newLabel = clf.predict(newLine)
print(newLabel)
