import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Input (X): temperature
# Output (y): sales
X = np.array([[51], [65], [69], [72], [75], [81], [78]])  # 2D array for sklearn
y = np.array([1, 14, 20, 23, 26, 30, 26])

# Create the model
model = LinearRegression()

# Train the model
model.fit(X, y)

predicted_sale = model.predict([[83]])
r2_score = model.score(X, y)
print(f"Predicted sale for 83 degrees: {predicted_sale[0]:.2f}")
print(f"R^2 score: {r2_score:.2f}")

# Plot the data and the regression line
plt.scatter(X, y, color='blue', label='Actual data')
plt.plot(X, model.predict(X), color='red', label='Regression line')
plt.xlabel('Temperature')
plt.ylabel('Ice cream sales')
plt.title('Temperature vs Sales - Linear Regression')
plt.legend()
plt.show()
