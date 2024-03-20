from .models import ROFiltrationRequest
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
    return i * C * R * T

def calculate_water_flux(P, delta_P, mu, L):
    return L * (P - delta_P) / mu

def calculate_permeate_flow_rate(A, water_flux):
    return A * water_flux

def calculate_tds_reduction(initial_tds, tds_reduction_rate):
    return initial_tds * (1 - tds_reduction_rate)

def calculate_tds(voltage, temperature):
    CV = voltage / (1.0 + 0.02 * (temperature - 25))
    return 133.42 * (CV ** 3) - 255.86 * (CV ** 2) + 857.39 * CV * 0.5

def calculate_simulation(input_data):
    result = input_data.number1 + input_data.number2 + input_data.number3 + input_data.number4
    return {"result": result}

def calculate_ro_filtration(params: ROFiltrationRequest):
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
    volume_of_water = params.sump_capacity
    print("Volume of the water:", volume_of_water)
    
    initial_tds=calculate_tds(voltage,temperature)

    max_iterations = 10
    cycle_count = 0
    
    osmotic_pressure = calculate_osmotic_pressure(C)

    while cycle_count < max_iterations:
        cycle_count += 1
        water_flux = calculate_water_flux(P, delta_P, mu, L)
        permeate_flow_rate = calculate_permeate_flow_rate(A, water_flux)
        time_estimation_hours = volume_of_water / permeate_flow_rate
        tds_reduction_rate = 0.70
        print("initial TDS", initial_tds)
        tds_final = calculate_tds_reduction(initial_tds, tds_reduction_rate)
        initial_tds = tds_final

        print(cycle_count,tds_final)
        if desired_tds >= tds_final:
            break

    tds_calculated = calculate_tds(voltage, temperature)

    return {
        "osmotic_pressure": osmotic_pressure,
        "water_flux": water_flux,
        "permeate_flow_rate": permeate_flow_rate,
        "final_tds_concentration_after_ro_tank": tds_final,
        "calculated_tds_value": tds_calculated,
        "cycle_count": cycle_count,
        "time_estimation_hours": time_estimation_hours
    }
