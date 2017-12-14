# -*- coding:utf-8 -*-
# Created By zl

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

        self.weights = []


