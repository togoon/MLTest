# -*- coding:utf-8 -*-
# Created By zl

print("Hello, world!")

print(10 ** 3)
print(10 ** (1 / 3))

import math

print(math.pi)
print(math.sin(math.pi / 2))

print(100 / 3, round(100 / 3), round(100 / 3, 3))

apple_price = 5
apple_weight = 2
apple_cost = apple_price * apple_weight
print(apple_cost)

grape_price = 15
grape_weight = 1.5
grape_cost = grape_price * grape_weight
print(grape_cost)

total_cost = apple_cost + grape_cost
print("苹果的花费:{}, 葡萄的花费:{}, 总花费:{}".format(apple_cost, grape_cost, total_cost))

## 交换2个值
a = 10
b = 20
a, b = b, a
print("a is {}, b is {}".format(a, b))

## Python 是大小写敏感的
n = 10
N = 20

##数值类型
num = 10
num = num + 10
num += 10
num -= 10
num *= 10

## 乘方
print(math.pow(10, 3))

## 最大/小值
print(min(1, 2, 3))
print(max(1, 2, 3))

## sum
print(sum([1, 2, 3]))

## List Dict Tuple
ll = list[1, 2, 3]
dd = {
    "zhang": 10,
    "zhao": 10
}

tt = (a, 1, 100, "str11")
