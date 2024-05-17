import joblib
import xgboost
import numpy as np
import os

def get_soil_module():
    """
    Load the soil contamination model and scaler from the disk
    :return: Tuple of the loaded model and the scaler
    """
    current_dir = os.path.dirname(__file__)
    soil_model_path = os.path.join(current_dir, 'data_models', 'soil_XGBoost.pkl')
    soil_scaler_path = os.path.join(current_dir, 'data_models', 'soil_scaler.pkl')
    soil_model = joblib.load(soil_model_path)
    soil_scaler = joblib.load(soil_scaler_path)
    return soil_model, soil_scaler


