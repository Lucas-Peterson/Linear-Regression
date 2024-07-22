import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


X = np.array([50, 60, 70, 80, 90]).reshape(-1, 1)  
y = np.array([150, 180, 210, 240, 270])     


model = LinearRegression()
model.fit(X, y)

a = model.intercept_  
b = model.coef_[0]    

print(f"Model: price = {a:.2f} + {b:.2f} * area")


X_new = np.array([55, 75, 95]).reshape(-1, 1)
y_pred = model.predict(X_new)
print(f"Projected prices for areas {X_new.flatten()}: {y_pred}")


plt.scatter(X, y, color='blue', label='Start data')
plt.plot(X, model.predict(X), color='red', label='Line of regression')
plt.scatter(X_new, y_pred, color='green', label='Predictable prices')
plt.xlabel('Area (sq.m)')
plt.ylabel('Price')
plt.legend()
plt.show()
