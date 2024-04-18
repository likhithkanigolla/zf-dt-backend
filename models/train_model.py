import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
# from sklearn.externals import joblib
import joblib


# Load the data from Excel
df = pd.read_excel("../../Sand_test/Sump_1L/Sand Data.xlsx")

# Extract features (soil quantity) and target variables (temp and voltage)
X = df[["Quantity"]]
y_temp = df["Temp"]
y_voltage = df["Voltage"]

# Split the data into training and testing sets for temperature prediction
X_train_temp, X_test_temp, y_train_temp, y_test_temp = train_test_split(X, y_temp, test_size=0.2, random_state=42)

# Train the Linear Regression model for temperature prediction
model_temp = LinearRegression()
model_temp.fit(X_train_temp, y_train_temp)

# Make predictions for temperature
y_pred_temp = model_temp.predict(X_test_temp)

# Evaluate the model for temperature prediction
mse_temp = mean_squared_error(y_test_temp, y_pred_temp)
print("Mean Squared Error for Temp Prediction:", mse_temp)

# Save the trained model for temperature prediction
joblib.dump(model_temp, 'linear_regression_model_temp.pkl')

# Split the data into training and testing sets for voltage prediction
X_train_voltage, X_test_voltage, y_train_voltage, y_test_voltage = train_test_split(X, y_voltage, test_size=0.2, random_state=42)

# Train the Linear Regression model for voltage prediction
model_voltage = LinearRegression()
model_voltage.fit(X_train_voltage, y_train_voltage)

# Make predictions for voltage
y_pred_voltage = model_voltage.predict(X_test_voltage)

# Evaluate the model for voltage prediction
mse_voltage = mean_squared_error(y_test_voltage, y_pred_voltage)
print("Mean Squared Error for Voltage Prediction:", mse_voltage)

# Save the trained model for voltage prediction
joblib.dump(model_voltage, 'linear_regression_model_voltage.pkl')
