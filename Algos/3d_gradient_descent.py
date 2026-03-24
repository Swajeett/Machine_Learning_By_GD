import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#create cost function surface

w1 = np.linspace (-5 , 5, 100)
w2 = np.linspace (-5 , 5, 100)


W1 , W2 = np.meshgrid(w1 , w2)

#J = cost function
J = W1**2 + W2**2


#initiate gradient descent
learning_rate = 0.1
w1_current = 4
w2_current = 4
iterations = 25


w1_history = [w1_current]
w2_history = [w2_current]
J_history = [w1_current*2 + w2_current*2]

# Perform Gradient Descents
for i in range(iterations) :
    grad_w1 = 2 * w1_current
    grad_w2 = 2 * w2_current


    w1_current = w1_current - learning_rate * grad_w1
    w2_current = w2_current - learning_rate * grad_w2

    w1_history.append(w1_current)
    w2_history.append(w2_current)
    J_history.append(w1_current ** 2 + w2_current ** 2)

#Plot 3D Graph
fig = plt.figure(figsize = (8,6))
ax = fig.add_subplot(111, projection='3d')

#surface
ax.plot_surface(W1, W2, J, alpha = 0.3)

#Gradient Descent Path
ax.plot(w1_history , w2_history, J_history , marker = 'o')

ax.set_xlabel("w1")
ax.set_ylabel("w2")
ax.set_zlabel("Cost J")
ax.set_title("3D Gradient Descent")

plt.show()