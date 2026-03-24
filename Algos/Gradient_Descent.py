import numpy as np 

X = np.array([1, 2, 3, 4, 5])
y = np.array([2,4,6,8,10])

m = 0
b = 0
alpha = 0.01
n = len(X)

for i in range(1000):
    y_pred = m*X + b
    dm = (-2/n)