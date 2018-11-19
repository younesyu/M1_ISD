# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 14:09:55 2018

@author: r15022305
"""

import matplotlib as plt
import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

"""
ones = np.zeros(8)
ones.fill(1)

y = np.array([420, 380, 350, 400, 440, 380, 450, 42])

aug_x = np.column_stack((x, ones))
print(aug_x)


reg = lm.LinearRegression().fit(aug_x, y)
# print(lm.LinearRegression().coef_)

print(reg.score(aug_x, y))
print(reg.score(aug_x, y))
print(reg.score(aug_x, y))
"""
#def q112():
r = LinearRegression()
x = np.array([[5.5], [6.0], [6.5], [6.0], [5.0], [6.0], [4.5], [5]])
y = np.array([420, 380, 350, 400, 440, 380, 450, 42])


reg = r.fit(x, y)

predict_x = reg.predict(x)


mse = mean_squared_error(y, reg.predict(x)) 
print("Mean squared error : %f" %mse)


print("score \t\t: %f" %reg.score(x, y))
print("coef \t\t: %f" %reg.coef_)
print("intercept \t: %f" %reg.intercept_)

x0, x1 = 4.0, 7.0

y0 = reg.coef_ * x0 + reg.intercept_
y1 = reg.coef_ * x1 + reg.intercept_

plt.plot([x0, x1], [y0, y1], c = "red")

plt.scatter(x, y, c = "blue")

plt.show()