# -*- coding:utf-8 -*-
# Created By zl

# 4.2 绘图 MatPlotLib.pyplot
# [Python--matplotlib绘图可视化知识点整理](https://www.cnblogs.com/zhizhan/p/5615947.html)
# %matplotlib inline
# 在NoteBook中, 上一行是必须的, 表示将图表画在NoteBook中

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0 ,10 ,20)
y = np.sin(x)

fig = plt.figure() # 创建一个画布
plt.plot(x, y, '--')
plt.plot(x, np.cos(x))
# plt.show()

# fig.savefig("d://1.png")

# 拆分画布, 画多个图形 subplot
# plt.subplot(2,1, 1) # 2行1列, 绘制第一个
# plt.plot(x, np.sin(x), '--')
#
# plt.subplot(2,1, 2) # 2行1列, 绘制第二个
# plt.plot(x, np.cos(x), 'o', color= 'red') # 点状样式
# plt.show()

# 增加标签
plt.plot(x, np.sin(x), '--', label='sin(x)')
plt.plot(x, np.cos(x), label="cos(x)")
plt.legend(loc=0) # 默认loc=0,还可以指定1,2,3....
# plt.show()

# 限定坐标范围
plt.plot(x, np.sin(x), '--', label='sin(x)')
plt.ylim(0.5, -0.5)
plt.xlim(2,8)
# plt.show()

# pandas里边自带的绘图
df = pd.DataFrame(np.random.rand(100, 4).cumsum(0), columns=['A', 'B', 'C', 'D'])
df.plot()
plt.show()

df.A.plot()
plt.show()