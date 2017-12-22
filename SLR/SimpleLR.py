# -*- coding:utf-8 -*-
# Created By zl

import numpy as np


def fitSLR(x, y):
    n = len(x)
    # 分子
    numerator = 0
    # 分母
    denomirator = 0
    for i in range(n):
        numerator += (x[i] - np.mean(x)) * (y[i] - np.mean(y))
        # 两个乘号表示乘方, 后边是2就是平方
        denomirator += (x[i] - np.mean(x))**2

    b1 = numerator / float(denomirator)
    b0 = np.mean(y) - b1 * float(np.mean(x))

    return b0, b1


def predict(x, b0, b1):
    return b0 + x * b1


x = [1, 3, 2, 1, 3]
y = [14, 24, 18, 17, 27]

b0, b1 = fitSLR(x, y)
print("b0: %s, b1: %s" % (b0, b1))

x_t = 6

y_t = predict(x_t, b0, b1)

# 又学到一种打印的技巧
print("Y_Test:", y_t)
