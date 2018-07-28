# -*- coding:utf-8 -*-
# Created By zl

a = True
b = False
print("a and b is {}".format(a and b))

m = [1, 2, 3]
n = [4, 5, 6]
# and因为m n都需要判断, 所有返回最后一个元素, 即n
print("m and n is {}".format(m and n))
# or如果第一个为真, 那么就不继续判断, 所以返回m
print("m or n is {}".format(m or n))
# 如果前边为空, 即为False, 那么or就会继续判断后边的元素
x = ""
y = (1, 2)
print("x or y is {}".format(x or y))

# 空字符, 空list dict tuple都被认为是False
print(not [], not "", not {})

cost = 10
if cost > 2:
    print("大于2")
elif cost < 0:
    print("小于0")
else:
    print("0--2")

# 断言
age = 18
assert age == 18, "他居然不是18岁"

# 循环 for while
costs = [1, 2, 4, 6, 8]
for cost in costs:
    print("消费{}元".format(str(cost).center(15)))

# 用while生成一个长度为20, 内容为1-9随机的list
# 建议能用for的时候,就不要用while, 因为每次while都要判断一下, 而且while容易造成死循环
import random

random_num = []
while (len(random_num) < 20):
    random_num.append(random.randint(1, 10))
print(random_num, len(random_num))

random_num = []
for i in range(20):
    random_num.append(random.randint(1, 10))
print(random_num, len(random_num))

# range的妙用, range(5)本身是生成一个list, 0--4,步长默认为1
print(range(5))
print(list(range(5)), list(range(2, 20, 2)))

# 当条件和数量/序号没有关系时, 就只能用while循环
# 向列表中添加随机数, 直到添加的数字为9, 然后停止
random_num = []
while 9 not in random_num:
    random_num.append(random.randint(0, 10))
print(random_num)

a = [1, 2, 3]
b = 1
c = (b in a)
print(c, type(c))
# 注意, 如果元组中只包含一个值, 那么他的类型就是该值的类型, 要想定义一个只包含一个值的元组, 需要在后边加一个逗号
a = []
b = ()
a1 = [1]
b1 = (1)
b2 = (1, 2)
b3 = (1,)
print(type(a), type(b), type(a1), type(b1), type(b2), type(b3))

nums = [3, 4, 5, 6, 7, 8]
for n in nums:
    if n % 2 == 0:
        print(n, " is 偶数")
    else:
        print(n, " is 奇数")
        break
else:
    print("就是要打印")
# 在for 循环中，如果没有从任何一个break中退出，则会执行和for对应的else, 只要从break中退出了，则else部分不执行

# 重要内容, for循环可以构建推导式, 类似于scala中的 yield
# 对nums里边的每个元素*10后, 生成一个新的列表, 传统做法是使用for循环
new_nums = []
for n in nums:
    new_nums.append(n * 10)
print(new_nums)

# 推导式的方式实现
# 列表推导式---生成一个列表
new_nums = [n * 10 for n in nums]
print(new_nums)

# 字典推导式---生成一个字典
new_dicts = {n: "A" for n in nums}
print(new_dicts)
