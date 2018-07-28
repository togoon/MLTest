# -*- coding:utf-8 -*-
# Created By zl

# 函数
# 函数, 是组织好的, 可重复使用的, 能够完成特定功能的代码块, 它是代码块的抽象
m = {
    'a': 100,
    'b': 100,
    'c': 200,
    'd': 300
}

print(m['a'])

# 输出100所对应的key
keys = [k for k, v in m.items() if v == 100]
print(keys)


# 将以上方法抽象成一个函数
def getKeys(data, value):
    return [k for k, v in data.items() if v == value]


print(getKeys(m, 200))


## 重要问题: 函数通过参数获取我们传递的值, 函数中改变了参数的值, 那么我们传递进去的值会改变吗?
def test(v):
    v += 10
    return v


a = 100
print(a, test(a), a)


def test2(v):
    v.append(200)
    return v


v = []
print(v)
print(test2(v), v)


# 由以上可知, 可变类型是可以被函数内的操作改变的
## 不建议对可变类型在函数内进行更改, 建议用函数返回值进行重新赋值

def test3(v):
    value = v.copy()  # 使用copy复制一个新的变量, 然后对新变量进行操作
    value.append(200)
    return value


v = []
v = test3(v)  # 通过函数返回值赋值的形式, 改变原变量的值
print(v)


# 参数收集--没讲明白
def test4(name, age, *args, **kwargs):
    print(name, age, *args, **kwargs)


## 装饰器
def test11():
    print("Test 11")


c = test11  # 可以把函数赋值给一个变量
print(c.__name__)


# 函数的参数也可以是一个函数
def test12(func):
    return func


def f1():
    print("This is Function")


# 函数可以作为另一个函数的返回值
d = test12(f1)
print(d.__name__, d())

# 举例, 有N个函数, 都是返回浮点值, 现在新增了一个需求, 要求所有浮点值保留3位有效数字
import random


def dd(fun):
    def wrapper(*args, **kwargs):
        return round(fun(*args, **kwargs), 3)

    return wrapper


@dd
def fun1():
    return random.random()


@dd
def fun2():
    return random.random() * 10


print(fun1(), fun2())
