import numpy as np
import matplotlib.pyplot as plt 

def compute_cost(X, y, m, c):
    n = len(y)
    predictions = m * X + c 
    cost = (1 /(2 *n)) * np.sum((predictions - y)**2)
    return cost

def gradient_descent(X, y, m, c, learning_rate, iterations):
    n = len(y)
    cost_history = []

    for i in range(iterations):
        predictions = m  * X + c
        dm = (1 / n) * np.sum((predictions - y) * X)
        dc = (1 / n) * np.sum(predictions -y)

        m = m - (learning_rate * dm)
        c = c - (learning_rate * dc)

        cost = compute_cost(X, y, m, c)
        cost_history.append(cost)
    return m, c, cost_history

X = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])

m, c = 0, 0 
alpha = 0.01            # Learning Rate
epochs = 4000           # iterations

m_final, c_final, cost_history = gradient_descent(X, y, m, c, alpha, epochs)

print(f"Optimized Slop (m): {m_final:.2f}")
print(f"Optimized Intercept (c): {c_final:.2f}")


# Plot Regression Line
y_pred = m_final * X + c_final 

plt.figure()
plt.scatter(X, y)
plt.plot(X, y_pred)
plt.xlabel("X")
plt.ylabel("y")
plt.title("Linear Regression using Gradient Descent")
plt.show()


# Plot MSE 

plt.figure()
plt.plot(range(epochs), cost_history)
plt.xlabel("Iterations")
plt.ylabel("Cost")
plt.title("Cost Reduction Over Iterations")
plt.show()