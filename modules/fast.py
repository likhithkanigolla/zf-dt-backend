from fastapi import FastAPI
from sklearn.linear_model import LinearRegression
import numpy as np

app = FastAPI()

# Define the voltage data
voltage_data = {
    0: 1.2,
    100: 2.3,
    200: 3.4,
    300: 4.5,
    400: 5.6,
    500: 6.7,
}

# Prepare the data for training
X = np.array(list(voltage_data.keys())).reshape(-1, 1)
y = np.array(list(voltage_data.values()))

# Train the linear regression model
model = LinearRegression()
model.fit(X, y)

@app.get("/predict/{soil_quantity}")
async def predict_voltage(soil_quantity: int):
    if 1 <= soil_quantity <= 500:
        # Predict the voltage for the given soil quantity
        predicted_voltage = model.predict([[soil_quantity]])
        return {"predicted_voltage": predicted_voltage[0]}
    else:
        return {"error": "Soil quantity must be between 1 and 500 grams."}

