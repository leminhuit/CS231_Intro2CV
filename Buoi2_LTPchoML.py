from argparse import Namespace
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import numpy as np


# Xu Ly File Salary_Data
# data = pd.read_csv('datasets/Salary_Data.csv');
# data = data.to_numpy()
# X = data[:, 0]
# Y = data[:, 1]
# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state= 0)

# model = LinearRegression()
# model.fit(X_train.reshape(-1,1), Y_train)
# X = np.array([[1.5]])
# Y_pred = model.predict(X_test.reshape(-1,1))

# l2 = ((Y_pred - Y_test)**2).sum()
# l2 = (l2**0.5)/Y_test.shape[0]
# print('L2 Loss: ', l2)

# l1 = (Y_pred - Y_test)
# l1 = np.absolute(l1).sum()
# l1 = l1/Y_test.shape[0]
# print('L1 Loss:', l1)


# Xu Ly File Position_Salary
data = pd.read_csv('datasets/Position_Salaries.csv')
def one_hot(x, num_class = None):
    classes, index = np.unique(x, return_inverse=True)
    one_hot_vectors = np.zeros((x.shape[0], len(classes)))
    for i, cls in enumerate(index):
        one_hot_vectors[i, cls] = 1
    return one_hot_vectors

# Check one_hot
# names = np.array(['a', 'b', 'c', 'a', 'c'])
# one_hot_vect = one_hot(names)
# print(one_hot_vect)

# print(data)
data = data.to_numpy()
X = data[:, :-1]
Y = data[:, -1]
X_onehot = one_hot(X[:, 0])
print(X_onehot.shape)

transformed_X = np.concatenate([X_onehot, X[:, 1:]],axis=-1)
print('transformed_X: ', transformed_X.shape)

X_train, X_test, Y_train, Y_test = train_test_split(transformed_X, Y, test_size=0.3)
# print(X_train)

model = LinearRegression()
model_tree = DecisionTreeRegressor(max_depth=2, random_state=0)
model_random_forest = RandomForestRegressor(max_depth=2, random_state=0)

model_tree.fit(X_train, Y_train)
model_random_forest.fit(X_train, Y_train)

Y_pred1 = model_tree.predict(X_test)
Y_pred2 = model_random_forest.predict(X_test)

l2 = ((Y_pred1 - Y_test)**2).sum()
l2 = (l2**0.5)/Y_test.shape[0]
print('L2 Loss of Tree: ', l2)

l2_rforest = ((Y_pred2 - Y_test)**2).sum()
l2_rforest = (l2**0.5)/Y_test.shape[0]
print('L2 Loss of Forest: ', l2_rforest)


l1 = (Y_pred1 - Y_test)
l1 = np.absolute(l1).sum()
l1 = l1/Y_test.shape[0]
print('L1 Loss:', l1)