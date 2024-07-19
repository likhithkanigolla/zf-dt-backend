from .models import ROFiltrationRequest, SoilContaminationRequest, SandContaminationRequest, MotorFlowRateRequest
from sklearn.preprocessing import StandardScaler
import pandas as pd
import math

# Constants
R = 8.314  # Ideal gas constant (J/(mol·K))
T = 298.15  # Temperature (25°C in Kelvin)
i = 1  # van't Hoff factor (assumed for simplicity)
C= 1.92 #

# 11.6 g of NaCl is dissolved in 100 g of water. The final mass concentration ρ(NaCl) is
# ρ(NaCl) = 
# 11.6 g
# /
# 11.6 g + 100 g
#  = 0.104 g/g = 10.4 %.
# The volume of such a solution is 104.3mL (volume is directly observable); its density is calculated to be 1.07 (111.6g/104.3mL)

# The molar concentration of NaCl in the solution is therefore

# c(NaCl) = 
# 11.6 g
# /
# 58 g/mol
#  / 104.3 mL = 0.00192 mol/mL = 1.92 mol/L.

# Calculation functions
def calculate_osmotic_pressure(C):
    """
    Calculate osmotic pressure using the formula:
    π = i * C * R * T
    """
    return i * C * R * T

def calculate_water_flux(P, delta_P, mu, L):
    """
    Calculate water flux using the formula:
    J = L * (P - ΔP) / μ
    """
    return L * (P - delta_P) / mu

def calculate_permeate_flow_rate(A, water_flux):
    """
    Calculate permeate flow rate using the formula:
    Q = A * J
    """
    return A * water_flux / 1000  # Converting to liters per minute

def calculate_tds_reduction(initial_tds, tds_reduction_rate):
    """
    Calculate TDS reduction using the formula:
    TDS_final = TDS_initial * (1 - TDS_reduction_rate)
    """
    return initial_tds * (1 - tds_reduction_rate)

def calculate_tds(voltage, temperature):
    """
    Calculate TDS using the formula:
    TDS = 133.42 * (CV ** 3) - 255.86 * (CV ** 2) + 857.39 * CV * 0.5
    """
    CV = voltage / (1.0 + 0.02 * (temperature - 25))
    return 133.42 * (CV ** 3) - 255.86 * (CV ** 2) + 857.39 * CV * 0.5

def calculate_simulation(input_data):
    result = input_data.number1 + input_data.number2 + input_data.number3 + input_data.number4
    return {"result": result}

# Write me a recursive function to calculate how many cycles it will take to reach the desired TDS
# The function should take in the initial TDS, the desired TDS, and the TDS reduction rate
# The function should return the number of cycles it will take to reach the desired TDS
def calculate_cycles(initial_tds, desired_tds, tds_reduction_rate, permeate_flow_rate, volume_of_water):
    """
    Calculate the number of cycles to reach the desired TDS, the final TDS value, and the time it will take to filter the water
    :param initial_tds: The initial TDS value
    :param desired_tds: The desired TDS value
    :param tds_reduction_rate: The TDS reduction rate
    :param permeate_flow_rate: The permeate flow rate in liters per minute
    :param volume_of_water: The volume of water in liters
    :return: The number of cycles to reach the desired TDS, the final TDS value, and the time in hours to filter the water
    """
    if desired_tds >= initial_tds:
        return 0, initial_tds, 0
    else:
        initial_tds_temp = initial_tds
        cycles = 0
        time_hours = 0
        while initial_tds_temp > desired_tds:
            cycles += 1
            initial_tds_temp = calculate_tds_reduction(initial_tds_temp, tds_reduction_rate)
            time_hours += volume_of_water / (permeate_flow_rate * 60)
        return cycles, initial_tds_temp, time_hours

def calculate_ro_filtration(params: ROFiltrationRequest):
    """
    Calculate the reverse osmosis filtration based on the input parameters
    :param params: ROFiltrationRequest
    :return: Dictionary with the calculated reverse osmosis filtration
    """
    initial_tds = params.initial_tds
    desired_tds = params.desired_tds
    P = params.applied_pressure
    delta_P = params.hydraulic_pressure_drop
    mu = params.dynamic_viscosity
    L = params.membrane_permeability
    A = params.effective_membrane_area
    C = params.molar_concentration
    voltage = params.voltage
    temperature = params.temperature
    # timeMultiplier = params.timeMultiplier
    timeMultiplier = 1
    volume_of_water = params.sump_capacity
    print("Volume of the water:", volume_of_water)
    print("type of desired", type(desired_tds), desired_tds)
    
    # initial_tds=calculate_tds(voltage,temperature)
    osmotic_pressure = calculate_osmotic_pressure(C)

    water_flux = calculate_water_flux(P, delta_P, mu, L)
    permeate_flow_rate = calculate_permeate_flow_rate(A, water_flux)
    
    cycle_count,tds_final,time_estimation_hours = calculate_cycles(initial_tds, desired_tds, 0.70, permeate_flow_rate, volume_of_water)

    return {
        "osmotic_pressure": osmotic_pressure,
        "water_flux": water_flux,
        "permeate_flow_rate": permeate_flow_rate*timeMultiplier,
        "final_tds_concentration_after_ro_tank": tds_final,
        "calculated_tds_value": initial_tds,
        "cycle_count": cycle_count,
        "time_estimation_hours": time_estimation_hours/timeMultiplier
    }

def motor_flow_rate(params: MotorFlowRateRequest):
    voltage = params.voltage
    current = params.current
    power_factor = params.power_factor
    motor_efficiency = params.motor_efficiency
    depth  = params.depth
    # timeMultiplier = params.timeMultiplier
    timeMultiplier = 1
    
    power_input = voltage * current * (math.sqrt(3)) * power_factor
    p_mechanical = power_input * motor_efficiency
    p_hydraulic = p_mechanical
    flowrate = p_hydraulic / (1000 * 9.81 * depth)
    flowrate_lpm = flowrate * 1000 #Converting to liters per minute
    return {"flowrate_per_min": flowrate_lpm*timeMultiplier}

def calculate_soil_contamination(params: SoilContaminationRequest, soil_model, soil_scaler):
    """
    Calculate the soil contamination based on the input parameters
    :param params: SoilContaminationRequest
    :param soil_model: The loaded machine learning model for soil contamination
    :param soil_scaler: The scaler used for preprocessing soil data
    :return: Dictionary with the calculated soil contamination
    """
    input_data = [params.temperature, params.sumpCapacity, params.SoilQuantiy]
    feature_names = ['Temp', 'Quantity', 'Soil '] 
    # Feature names used in the model at the time of training

    # Create a DataFrame from the input data
    input_features = pd.DataFrame([input_data], columns=feature_names)

    # Use the fitted scaler to transform the new data
    input_features_scaled = soil_scaler.transform(input_features)

    # Use the loaded model to make predictions on the scaled data
    predictions = soil_model.predict(input_features_scaled)

    return predictions.tolist()[0]

def calculate_sand_contamination(params: SandContaminationRequest, sand_model, sand_scaler):
    """
    Calculate the sand contamination based on the input parameters
    :param params: SandContaminationRequest
    :param sand_model: The loaded machine learning model for sand contamination
    :param sand_scaler: The scaler used for preprocessing sand data
    :return: Dictionary with the calculated sand contamination
    """
    input_data = [params.temperature, params.sumpCapacity, params.SandQuantiy]
    feature_names = ['Temp', 'Quantity', 'Sand'] 
    # Feature names used in the model at the time of training

    # Create a DataFrame from the input data
    input_features = pd.DataFrame([input_data], columns=feature_names)

    # Use the fitted scaler to transform the new data
    input_features_scaled = sand_scaler.transform(input_features)

    # Use the loaded model to make predictions on the scaled data
    predictions = sand_model.predict(input_features_scaled)

    return predictions.tolist()[0]