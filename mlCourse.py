import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Example data: height (in inches) and weight (in pounds)
# Input (X): height
# Output (y): weight
X = np.array([[60], [62], [65], [67], [70], [72]])  # 2D array for sklearn
y = np.array([115, 120, 130, 140, 150, 160])

# Create the model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Predict weight for a new height (e.g., 68 inches)
predicted_weight = model.predict([[68]])
print(f"Predicted weight for 68 inches: {predicted_weight[0]:.2f} lbs")

# Plot the data and the regression line
plt.scatter(X, y, color='blue', label='Actual data')
plt.plot(X, model.predict(X), color='red', label='Regression line')
plt.xlabel('Height (inches)')
plt.ylabel('Weight (pounds)')
plt.title('Height vs Weight - Linear Regression')
plt.legend()
plt.show()
