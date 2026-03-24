import numpy as np 
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 6, 8])

x_mean = np.mean(x)
y_mean = np.mean(y)

numerator = np.sum((x - x_mean) * (y - y_mean))
denominator = np.sum((x - x_mean)**2)
m = numerator / denominator

b = y_mean - (m * x_mean)

print(f"Equation: y = {m:.2f}x + {b:.2f}")

y_pred = m * 6 + b
print(f"Prediction for x 6: {y_pred:.2f}")

plt.scatter(x, y, color='blue', label='Actual Data')
plt.plot(x, m*x + b, color='red', label='Regression Line')
plt.xlabel('X (Feature)')
plt.show()