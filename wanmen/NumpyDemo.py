# -*- coding:utf-8 -*-
# Created By zl

# 4.1 数据处理 Numpy
# 数组与列表的区别: 列表可以同时存储任意类型的数据, 而数组只能存储一种类型的数据

import array

a = array.array('i', range(10))  # i表示int类型
print(a)

# 实际使用中更多的是使用numpy, 而不是用array这个包
import numpy as np

# 可以从list转为数组
list_a = list(range(10))
np_array = np.array(list_a)
print(np_array)

# 也可以通过np自带的方法生成数组
z_array = np.zeros(10)
print(z_array)
# 查看生成的数组元素类型
print(z_array.dtype)
# 生成数组时可以指定类型
z1_array = np.zeros(10, dtype=int)
print(z1_array.dtype)
# 生成多维数组, 指定行数和列数
z2_array = np.zeros((4, 4), dtype=int)
print(z2_array)
# 同理, zeros生成0元素数组, ones生成1元素数组
z3_array = np.ones((3, 3), dtype=int)
print(z3_array)
# 生成一个指定元素的数组
z4_array = np.full((3, 3), 3.14)
print(z4_array)

# 类似random模块, np里也有random方法, 用来生成随机数组
# 生成一个随机的3*3的数组
z5 = np.random.random((3, 3))
print(z5)
# 生成一个5-10之间随机的3*4数组
z6 = np.random.randint(5, 10, (3, 4), dtype=int)
print(z6)

# 范围取值
# range可以生成一个0-10, 步长为2的list
r = list(range(0, 10, 2))
print(r)
# np.arange是同样的功能, 只不过生成的是数组
r2 = np.arange(0, 10, 2)
print(r2)
# 另一个类似的是linspace, 从0-4中取20个数
r3 = np.linspace(0, 4, 20)
print(r3)

# 数组的基础运算
# + - * / 基础运算是对数组里的每一个元素都做运算
t = np.full((3, 4), 10, dtype=int)
print(t)
print(t + 5)

# 求和
a = np.array([[1, 2], [3, 4]])
print(a)
print("Sum0: ", sum([1, 2, 3]))
print("Sum1: ", sum(a))  # 默认是对列求和
# 所以, 实际情况中是使用np.sum求和
print("Sum2 : ", np.sum(a))  # 所有元素求和
print("Sum3 : ", np.sum(a, axis=0))  # 列元素求和
print("Sum4 : ", np.sum(a, axis=1))  # 行元素求和

# 数组的比较
print("Q1 : ", a > 3)
print("Q2 : ", a == 3)
print("Q3 : ", a != 3)

# 数组的变形, 注意: 行*列=总数, 变形前后, 总数要相等
b = np.full((2, 10), 2, dtype=int)
print("Before:", b)
print(b.shape, b.size)
c = b.reshape((4, 5))
print("After:", c)
print(c.shape, c.size)
# 但此时的b是不变的
print("Show:", b)
print(b.shape, b.size)

# 排序
l = [
    [1, 2, 3, 5, 4],
    [31, 20, 25, 40, 33]
]

s = np.array(l)
print("Before:", s)
# np.sort不改变原数组值, s.sort改变值
s1 = np.sort(s)
print("S1:", s1)
print("S:", s)
s.sort()
print("S:", s)

# 倒序排列 TODO:为什么返回None?
print("S_r:", s.sort(axis=0))
