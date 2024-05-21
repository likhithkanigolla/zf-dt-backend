import joblib

# Load the model from the file
model = joblib.load('./random_forest_model.pkl')

# temp, quantity, sand 
# Make predictions on new data
new_data = [[19.3125, 6000, 1809]]
predictions = model.predict(new_data)

print(predictions)