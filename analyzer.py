from sklearn.linear_model import LinearRegression
import numpy as np

# 1. Prepare historical data (e.g., Weeks 1, 2, 3, 4)
# Let's say Ahmed's scores were: 88, 89, 91, 92
weeks = np.array([1, 2, 3, 4]).reshape(-1, 1)
scores = np.array([88, 89, 91, 92])

# 2. Build the Model
model = LinearRegression()
model.fit(weeks, scores)

# 3. Predict Week 5
prediction = model.predict([[5]])

print(f"--- PREDICTIVE INSIGHTS ---")
print(f"Ahmed's predicted score for next week: {prediction[0]:.2f}%")
