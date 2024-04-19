import joblib

# Load the trained model for temperature prediction
model_temp = joblib.load('linear_regression_model_temp.pkl')

# Load the trained model for voltage prediction
model_voltage = joblib.load('linear_regression_model_voltage.pkl')

# Prepare input data
quantity_input = 962  # Example quantity value

# Make predictions for temperature
temp_prediction = model_temp.predict([[quantity_input]])

# Make predictions for voltage
voltage_prediction = model_voltage.predict([[quantity_input]])

# Print predictions
print("Predicted Temp:", temp_prediction)
print("Predicted Voltage:", voltage_prediction)

# Compare with actual values if available
# actual_temp = ...
# actual_voltage = ...
# print("Actual Temp:", actual_temp)
# print("Actual Voltage:", actual_voltage)
