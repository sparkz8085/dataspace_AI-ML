import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# Load student scores data
df = pd.read_csv("./student_scores.csv")

# Display the dataset to understand the structure
print("Dataset:")
print(df)

# Select features and target
# Using Hours_Study, Attendance, and Hours_Sleep as features to predict Score
X = df[['Hours_Study', 'Attendance', 'Hours_Sleep']]  # All relevant features
y = df['Score']                                       # Target variable

# Check shapes
print(f"\nFeature shape: {X.shape}, Target shape: {y.shape}")

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Compare actual vs predicted scores
compare_df = pd.DataFrame({
    'Actual Score': y_test,
    'Predicted Score': y_pred
})
print("\nActual vs Predicted Scores:")
print(compare_df)

# Visualize the regression line (using Hours_Study vs Score)
plt.figure(figsize=(10, 6))
plt.scatter(X['Hours_Study'], y, color="blue", label="Actual Data", alpha=0.7)
plt.plot(X['Hours_Study'], model.predict(X), color='red', linewidth=2, label='Regression Line')
plt.title("Linear Regression Line - Student Score Prediction (Based on Hours of Study)")
plt.xlabel("Hours of Study")
plt.ylabel("Score")
plt.legend()
plt.grid(True)
plt.show()

# Model Evaluation
print("\nModel Evaluation")
print(f"R² Score: {r2_score(y_test, y_pred):.4f}")
print(f"Mean Absolute Error: {mean_absolute_error(y_test, y_pred):.2f}")
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred):.2f}")
print(f"Root Mean Squared Error: {np.sqrt(mean_squared_error(y_test, y_pred)):.2f}")

# Predict new score for a student with given study hours, attendance, and sleep hours
new_study_hours = np.array([[5]])
new_attendance = np.array([[90]])
new_sleep_hours = np.array([[7]])

# Combine into a single input array
new_data = np.column_stack((new_study_hours, new_attendance, new_sleep_hours))
predicted_score = model.predict(new_data)

print(f"\nPredicted score for a student with {new_study_hours[0][0]} hours of study, {new_attendance[0][0]}% attendance, and {new_sleep_hours[0][0]} hours of sleep = {predicted_score[0]:.2f}")
