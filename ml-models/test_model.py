import joblib
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
import numpy as np

# Load the trained model from the file
loaded_model = joblib.load("polynomial_regression_model.pkl")

# Define the polynomial features transformer
degree = 3
poly_features = PolynomialFeatures(degree=degree)

# Load the scaler used for scaling the target variable during training
target_scaler = joblib.load("target_scaler.pkl")

# Take input from the user for prediction
input_features = np.array([30, 1, 100]).reshape(1, -1)

# Transform the input features using polynomial features
input_features_poly = poly_features.transform(input_features)

# Make predictions using the loaded model
predicted_value_scaled = loaded_model.predict(input_features_poly)

# Unscaled the predicted value
predicted_value = target_scaler.inverse_transform(predicted_value_scaled.reshape(-1, 1))

# Print the predicted value
print("Predicted value:", predicted_value)
