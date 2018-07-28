# -*- coding:utf-8 -*-
# Created By zl

# 类
class Person:
    # 初始化函数self后边的变量, 是实例化对象的属性, 如果加了_, 表示这个属性是私有的, 不应该在外边被访问
    # self.name =name  与  self._name = name
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def rename(self, new_name):
        self.name = new_name


p = Person('wang', 20)
print(p.get_name())
p.rename('wang lei')
print(p.get_name())

# 类的继承
# pass代表什么都不做, 只是占个位而已
class Student(Person):
    pass

s = Student('li lei', 15)
print(s.get_name())