# -*- coding:utf-8 -*-
# Created By zl
# https://github.com/lawlite19/MachineLearning_Python
import numpy as np


# sigmod 双曲线函数
def tanh(x):
    return np.tanh(x)


# 求tanh函数的导数
def tanh_deriv(x):
    return 1.0 - np.tanh(x) * np.tanh(x)


# 逻辑函数1/(1+e(-x))
def logsitic(x):
    return 1 / (1 + np.exp(-x))


# 逻辑函数导数
def logsitic_deriv(x):
    return logsitic(x) * (1 - logsitic(x))


class NerualNetwork():
    def __init__(self, layers, activation='tanh'):
        """
        :param layers: 每层神经网络里有多少个神经元,
                        例如有一个2层的神经网络, 输入层有10个节点, 隐藏层有2个节点, 输出层有2个
                        那么layers=[10, 2, 2]
        :param activation: 神经网络的激活函数, 可选值包含'tanh' 或 'logsitic'
        """
        if activation == 'tanh':
            self.activation = tanh
            self.activation_deriv = tanh_deriv
        elif activation == 'logsitic':
            self.activation = logsitic
            self.activation_deriv = logsitic_deriv

        # 定义一个List, 用来存放神经网络中所有的神经元之间的权重(weight)
        # 因为神经网络的权重本身就是可以修正的, 所以初始的权重随机生成就可以
        self.weights = []

        # 假如一个神经网络包括输入/隐藏/输出 3层, 那么range(1, 3-1)
        # 因为3层的时候, 输入->隐藏层每个节点之间有权重, 隐藏->输出每个节点之间有权重
        # random.random()用于生成一个0到1的随机符点数: 0 <= n < 1.0
        # -0.25 <= (2n-1) * 0.25 < 0.25
        # np.random.random((6, 3)) 表示创建一个6行3列的二维矩阵
        # TODO 暂时没明白为什么第一层和第二层要用layers[0] + 1, ==以下给与解释==
        # 随机产生第一层和第二层之间的权重
        # O(j)为第j层到第j+1层映射的权重矩阵，就是每条边的权重
        # j层单元要加1, 是因为要补一个bias(通常bias为1)
        # O(j) ==》j+1的单元数 *（j层的单元数+1）, 即 random((layers[i+1], layers[i]+1)
        for i in range(0, len(layers)-1):
            self.weights.append((2 * np.random.random((layers[i+1], layers[i]+1)) - 1) * 0.25)

    def fit(self, X, y, learning_rate=0.2, epochs =10000):
        """

        :param X:
        :param y:
        :param learning_rate:学习率
        :param epochs: 训练次数, 每次只从数据集中抽取一个实例训练神经网络, 当到达epochs时, 停止迭代
        :return:
        """
        # 判断实例必须至少是两维的
        X = np.atleast_2d(X)


        temp = np.ones(X.shape[0], X.shape[1])