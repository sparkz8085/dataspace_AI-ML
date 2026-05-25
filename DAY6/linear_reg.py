import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# -------------------------------
# Step 1: Create Sample Dataset
# -------------------------------

# Suppose area is in square feet and price is in lakhs
data = {
    'area': [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000],
    'price': [50, 65, 80, 95, 110, 125, 140, 155, 170]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

# -------------------------------
# Step 2: Visualize the Data
# -------------------------------

plt.scatter(df['area'], df['price'], color='blue', marker='o')
plt.title("House Price vs Area")
plt.xlabel("Area (sq ft)")
plt.ylabel("Price (lakhs)")
plt.grid(True)
plt.show()

# -------------------------------
# Step 3: prep data
# -------------------------------

X = df[['area']]
y = df['price']


X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)


# -------------------------------
# Step 4:  train Linear Reg data
# -------------------------------


model = LinearRegression()
model.fit(X_train, y_train)

# -------------------------------
# Step 5: Visualize the Data
# -------------------------------

y_pred = model.predict(X_test)

#compare Actual Vs Predicted
compare_df = pd.DataFrame({'Actal Price': y_test, 'Predicted price': y_pred})
print("\n Actual Vs  Prediction :")
print(compare_df)

# -------------------------------
# Step 6: Visualize Refression Line
# -------------------------------


plt.scatter(X,y, color="blue", label="actual data")
plt.plot(X,model.predict(X), color='red', linewidth=2, label='Regression Line')
plt.title("linear Regression Line - House  price Pred")
plt.xlabel("Area (sq ft)")
plt.ylabel("price (in lacs)")
plt.legend()
plt.show()


# -------------------------------
# Step 7: Model Eval
# -------------------------------


print("\n Model Eval")
print(f"R2 Score: {r2_score(y_test, y_pred)}")
print(f"Mean Absolute Error: {mean_absolute_error(y_test, y_pred):.2f}")
print(f"mean square error: {mean_squared_error(y_test, y_pred):.2f}")
print(f"Root Mean Squared Error: {np.sqrt(mean_squared_error(y_test, y_pred)):.2f}")


# -------------------------------
# Step 8: predict new value
# -------------------------------

new_area = np.array([[4200]])
predicted_price = model.predict(new_area)
print(f"\n Predicted price for a house with {new_area[0][0]} sq ft area = {predicted_price[0]:.2f} lacs")
