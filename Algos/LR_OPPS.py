import numpy as np
import matplotlib.pyplot as plt

class Linear_Regression:
    def __init__(self):
        self.m = None
        self.b = None

    def fit(self, x, y):
        x = np.array(x)
        y = np.array(y)

        x_mean = np.mean(x)
        y_mean = np.mean(y)

        numerator = np.sum((x - x_mean) * (y - y_mean))
        denominator = np.sum((x - x_mean)**2)

        if denominator == 0:
            raise ValueError("Denominator is zero. Check your X values.")
        
        self.m = numerator / denominator
        self.b = y_mean - (self.m * x_mean)
        return self

    def predict(self, x):

        return(self.m * np.array(x)) + self.b
    
    def score(self, x, y):

        y = np.array(y)
        y_pred = self.predict(x)

        ss_res = np.sum((y - y_pred)**2)
        ss_tot = np.sum((y - np.mean(y))**2)

        return 1 - (ss_res / ss_tot)

experience = [1, 2, 3, 4, 5]
salary = [2.1, 3.8, 6.2, 8.1, 10.3]

model = Linear_Regression()
model.fit(experience, salary)

print(f"Calculated Slop (m): {model.m:.2f}")
print(f"Calculated Intercept (b): {model.b:.2f}")
print(f"Accuracy (R^2 Score): {model.score(experience, salary):.4f}")

prediction = model.predict([6])
print(f"Prediction for 6 years: {prediction[0]:.2f} Lakhs")