import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix

# Input (X): Blood glucose 
# Output (y): Diabetic? (0 = No, 1 = Yes)
X = np.array([[66], [107], [112], [71], [87]])
y = np.array([0, 1, 1, 0, 1])

# Create and train logistic regression model
model = LogisticRegression()
model.fit(X, y)

# Make a prediction
glucose_level = 89
predicted_class = model.predict([[glucose_level]])[0]
predicted_proba = model.predict_proba([[glucose_level]])[0, 1]  # Probability of class 1

# Predict for all and calculate metrics
y_pred = model.predict(X)
accuracy = accuracy_score(y, y_pred)
precision = precision_score(y, y_pred)
recall = recall_score(y, y_pred)
f1 = f1_score(y, y_pred)
roc_auc = roc_auc_score(y, model.predict_proba(X)[:, 1])

print(f"Prediction for glucose level {glucose_level}: {predicted_class} (Probability: {predicted_proba:.2f})")
print(f"Accuracy: {accuracy:.2f}, Precision: {precision:.2f}, Recall: {recall:.2f}, F1 Score: {f1:.2f}, ROC AUC: {roc_auc:.2f}")

# Plotting
plt.scatter(X, y, color='blue', label='Actual data')
X_plot = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
y_plot = model.predict_proba(X_plot)[:, 1]
plt.plot(X_plot, y_plot, color='red', label='Logistic regression curve')
plt.axvline(x=glucose_level, color='gray', linestyle='--', label=f'Test Glucose: {glucose_level}')
plt.xlabel('Blood glucose')
plt.ylabel('Probability of being Diabetic')
plt.title('Blood glucose vs Diabetic? - Logistic Regression')
plt.legend()
plt.grid(True)
plt.show()
