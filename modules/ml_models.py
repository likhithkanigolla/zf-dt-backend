import joblib
import yaml
import xgboost
import numpy as np
import os

def load_soil_module():
    root_dir = os.path.dirname(os.path.abspath(__file__))  # Get the current directory of the script
    root_dir = os.path.dirname(root_dir)  # Get the parent directory
    # print("Root directory: ", root_dir)
    config_path = os.path.join(root_dir, 'configuration.yaml')
    print("Config path: ", config_path)
    # Read the configuration file and extract the file paths
    with open(config_path, 'r') as config_file:
        config_data = yaml.load(config_file, Loader=yaml.SafeLoader)  # Assuming configuration.yaml is in YAML format
        models = config_data['models']
        soil_model_path = os.path.join(root_dir, models[0]['path'])
        soil_scaler_path = os.path.join(root_dir, models[1]['path'])
    # print("Soil model path: ", soil_model_path)
    # print("Soil scaler path: ", soil_scaler_path)
    
    try:
        soil_model = joblib.load(soil_model_path)
        soil_scaler = joblib.load(soil_scaler_path)
        print("Soil Models loaded successfully.")
    except Exception as e:
        print("Error loading soil models:", str(e))

    return soil_model, soil_scaler

def load_sand_module():
    root_dir = os.path.dirname(os.path.abspath(__file__))  # Get the current directory of the script
    root_dir = os.path.dirname(root_dir)  # Get the parent directory
    # print("Root directory: ", root_dir)
    config_path = os.path.join(root_dir, 'configuration.yaml')
    print("Config path: ", config_path)
    # Read the configuration file and extract the file paths
    with open(config_path, 'r') as config_file:
        config_data = yaml.load(config_file, Loader=yaml.SafeLoader)  # Assuming configuration.yaml is in YAML format
        models = config_data['models']
        sand_model_path = os.path.join(root_dir, models[2]['path'])
        sand_scaler_path = os.path.join(root_dir, models[3]['path'])
    # print("Sand model path: ", sand_model_path)
    # print("Sand scaler path: ", sand_scaler_path)
    
    try:
        sand_model = joblib.load(sand_model_path)
        sand_scaler = joblib.load(sand_scaler_path)
        print("Sand Models loaded successfully.")
    except Exception as e:
        print("Error loading sand models:", str(e))

    return sand_model, sand_scaler

