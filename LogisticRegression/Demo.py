# -*- coding:utf-8 -*-
# Created By zl

# 逻辑回归简单示例代码

import numpy as np
import random


def gradientDescent(x, y, theta, alpha, m, numIterations):
    """
    梯度下降算法
    :param x:
    :param y:
    :param theta: θ, 要学习的参数值
    :param alpha: 学习率, 决定梯度下降的时候每一步下降多少
    :param m: 数据集中一共有多少实例
    :param numIterations: 梯度下降算法更迭多少次
    :return:
    """

    xTrans = x.transpose()

    for i in range(0, numIterations):
        hypothesis = np.dot(x, theta)
        loss = hypothesis - y

        cost = np.sum(loss ** 2) / (2 * m)
        print("Iterator %d | Cost is %f" % (i, cost))

        gradient = np.dot(xTrans, loss) / m

        theta = theta - alpha * gradient

    return  theta


def genData(numPoints, bias, variance):
    """
    生成测试数据
    :param numPoints: 要生成多少条实例数据
    :param bias: 偏向
    :param variance: 方差
    :return:
    """

    # 生成一个全是0的二维矩阵, 行数是numPoint2的值, 列数是2
    x = np.zeros(shape=(numPoints, 2))

    # 生成label
    y = np.zeros(shape=numPoints)

    for i in range(0, numPoints):
        # 第一列全是1, 第二列写入i的值
        x[i][0] = 1
        x[i][1] = i

        # 随机生成label的值
        # random.uniform(0,1): 随机的从0-1之间产生数字
        y[i] = (i + bias) + random.uniform(0, 1) * variance

    return x, y


x, y = genData(100, 25, 10)
print("X:", x)
print("Y:", y)

m, n = np.shape(x)
n_y = np.shape(y)

print("X shape:", m, n)
print("Y shape:", n_y)

numIterations = 100000
alpha = 0.0005
# m个实例, n个维度, 所以θ的shape=n
theta = np.ones(n)

# 使用之前定义的梯度下降算法计算θ
theta = gradientDescent(x, y, theta, alpha, m, numIterations)
print("θ is:", theta)

