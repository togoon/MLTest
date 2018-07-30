# -*- coding:utf-8 -*-
# Created By zl

import os

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
pandas_data_path = os.path.join(PROJECT_ROOT, "../data/pandas1.csv")
titanic_test_path = os.path.join(PROJECT_ROOT, "../data/titanic/test.csv")
titanic_train_path = os.path.join(PROJECT_ROOT, "../data/titanic/train.csv")

# print(PROJECT_ROOT, pandas_data_path)