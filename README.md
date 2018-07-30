# MLTest
这是一个使用Python实现机器学习的学习项目

# 一. 准备工作
- 首先, 整个项目的都是在Win10系统上完成的
- Python 3.6
- [Anaconda3-5.0.1](https://repo.continuum.io/archive/Anaconda3-5.0.1-Windows-x86_64.exe) 
- [graphviz-2.38.msi](https://graphviz.gitlab.io/_pages/Download/windows/graphviz-2.38.msi)
- Pycharm
- 程序运行需要的数据都在`PubData`目录下


# 二. 如何在Pycharm中使用Anaconda的python
- 创建新项目的时候, 在`Project Interpreter`中选择`Anaconda`安装目录下的python.exe
- 如果项目已经存在, 那么可以在`Settings`->`Project Setting`->`Project Interpreter`中更改

# 三. 注意的点
- Python函数调用时带不带括号的问题
```markdown
- 不带括号时，调用的是这个函数本身 ，是整个函数体，是一个函数对象，不须等该函数执行完成
- 带括号（参数或者无参），调用的是函数的执行结果，须等该函数执行完成的结果
```

- Pandas输出的结果, 控制台有时候会换行, 需要增加如下设置
```python
pd.set_option('display.width', 1000)
```