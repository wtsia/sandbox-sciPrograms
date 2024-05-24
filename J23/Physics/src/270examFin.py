import math
import scipy.constants as const
import sympy as sp
import numpy as np
from scipy.constants import c, physical_constants
from scipy.constants import h, proton_mass
from scipy.constants import physical_constants
from scipy.constants import e, epsilon_0, h, pi
from math import cos, sin, pi, radians
from scipy.constants import pi, c, hbar, e, epsilon_0, m_e, k, N_A, R, day

## GLOBAL 
mu_0 = 4 * math.pi * (10 ** -7)
hbar = const.hbar
electron_mass = const.m_e
energy_electron_keV = 1.36 * 1e3 * const.e
seconds_per_day = day
microcuries_conversion = 3.7e10


def degreeToRadian(degree):
    return degree * math.pi / 180
def radianToDegree(radian):
    return radian * 180 / math.pi


def method1():
    print("give n, energy, n2")
    n = float(input("n: "))
    energy = float(input("energy: "))
    n2 = float(input("n2: "))

    # Given energy in the n=18 state in keV
    energy_electron_18_keV = energy * 1e3 * const.e  # Convert keV to Joules

    # Calculating L using n=18 and its energy
    L = ((n**2 * const.pi**2 * hbar**2) / (2 * electron_mass * energy_electron_18_keV)) ** 0.5

    # Calculate energy for n=3
    energy_electron_3 = (n2**2 * const.pi**2 * hbar**2) / (2 * electron_mass * L**2)
    energy_electron_3_keV = energy_electron_3 / (1e3 * const.e)  # Convert Joules to keV

    # Energy of the emitted photon
    energy_photon_keV = (energy_electron_18_keV - energy_electron_3) / (1e3 * const.e)

    # Calculate wavelength of the photon
    wavelength_photon_nm = (const.c * const.h) / (energy_photon_keV * 1e3 * const.e) * 1e9  # Convert m to nm
    result = wavelength_photon_nm
    print(result)
    print("")

def method2():
    print("give potDiff, uncertainty")
    potDiff = float(input("potDoff: "))
    uncertainty = float(input("uncertainty: "))

    V = potDiff*10**3  # Potential difference in volts

    # Energy gained by the proton (eV), then converted to Joules
    E_kinetic = V * 1.60218e-19  # Proton charge in Coulombs times voltage

    # Momentum of the proton using p = sqrt(2mE)
    p_proton_joules = np.sqrt(2 * proton_mass * E_kinetic)  # in kg*m/s

    # Given uncertainty in position in meters
    delta_x = uncertainty*10**-15  # in meters

    # Calculate the minimum uncertainty in momentum using Heisenberg's principle
    hbar = physical_constants['Planck constant over 2 pi'][0]
    delta_p_min = hbar / (2 * delta_x)

    # Calculate the minimum percent uncertainty in momentum
    delta_p_percent = (delta_p_min / p_proton_joules) * 100
    result = delta_p_percent
    print(result)
    print("")

def method3():
    print("give n, energy")
    n = float(input("n: "))
    energy = float(input("energy: "))

    # Constants
    electron_mass = const.m_e  # Mass of electron in kg
    hbar = const.hbar  # Reduced Planck's constant in J*s
    energy_electron_13_keV = energy * 1e3 * const.e  # Convert 0.8 keV to Joules

    # Calculate L for n=13 using the energy level formula
    L_13_nm = ((n**2 * const.pi**2 * hbar**2) / (2 * electron_mass * energy_electron_13_keV)) ** 0.5

    # Convert L from meters to nanometers
    L_13_nm = L_13_nm * 1e9  # 1 meter = 1e9 nanometers
    result = L_13_nm

    print(result)
    print("")

def method4():
    print("give n")
    n = float(input("n: "))

    # Quantum number n=7
    n7 = n

    # Speed of the electron in the Bohr model for hydrogen
    v_n7 = (e**2) / (2 * epsilon_0 * h) / n7

    # Convert speed from m/s to km/s
    v_n7_kms = v_n7 / 1000
    result = v_n7_kms
    print(result)
    print("")


def method5():
    print("give atomicMass, halfLife, kinEnergy, initAtoms")
    atomicMass = float(input("atomicMass: "))
    halfLife = float(input("halfLife: "))
    kinEnergy = float(input("kinEnergy: "))
    initAtoms = float(input("initAtoms: "))

    half_life_seconds = halfLife * seconds_per_day  # Half-life in seconds
    N_0 = initAtoms*10**12  # Initial number of atoms
    decay_constant = np.log(2) / half_life_seconds
    initial_activity_bq = decay_constant * N_0  # Activity in Bq
    result = initial_activity_bq / microcuries_conversion * 1e6  # Convert to microcuries

    print(result)
    print("")

def method6():
    print("give degrees1, percent, beta")
    degrees1 = float(input("degrees1: "))
    percent = float(input("percent: "))
    beta = float(input("beta: "))
    beta = beta*10**-6  # Coefficient of volume expansion in per degree Celsius
    initial_volume_increase_percent = percent
    delta_T = (initial_volume_increase_percent / 100) / beta
    final_temperature = degrees1 + delta_T  # Initial temperature was 20 degrees Celsius
    result = final_temperature
    print(result)
    print("")

def method7():
    print("give initTemp, pressure, vol, pressure2, vol2")
    initTemp = float(input("initTemp: "))
    pressure = float(input("pressure: "))
    vol = float(input("vol: "))
    pressure2 = float(input("pressure2: "))
    vol2 = float(input("vol2: "))

    # Given data
    P_initial = pressure  # in atm
    V_initial = vol*10**-6  # in m^3 (converted from cm^3)
    T_initial_kelvin = initTemp + 273.15  # Convert to Kelvin
    P_final = pressure2  # in atm
    V_final = vol2*10**-6  # in m^3

    # Calculate the number of moles using PV = nRT for initial conditions
    n_moles_corrected = P_initial * V_initial / (R * T_initial_kelvin)

    # Recalculate final temperature using corrected moles
    T_final_kelvin_corrected = P_final * V_final / (n_moles_corrected * R)
    T_final_celsius_corrected = T_final_kelvin_corrected - 273.15  # Convert back to Celsius

    result = T_final_celsius_corrected
    print(result)
    print("")

def method8():
    print("give molar_mass, thermal_speed")
    molar_mass = float(input("molar_mass: "))
    thermal_speed = float(input("thermal_speed: "))
    temp1 = (molar_mass * thermal_speed * thermal_speed / 3 / 8.314) / 1000
    result = temp1 - 273.15
    print(result)
    print("")

def method9():
    print("give length, width, height, pressure, temp, molar_weight")
    length = float(input("length: "))
    width = float(input("width: "))
    height = float(input("height: "))
    pressure = float(input("pressure: "))
    temp = float(input("temp: "))
    molar = float(input("molar: "))
    result = 3/2 * pressure * 1.013 * length/100 * width/100 * height
    print(result)
    print("")

def method10():
    print("give mass, c_Cu, init_temp, m_ice, init_temp2, c_ice, L_f")
    mass = float(input("mass: "))
    c_Cu = float(input("c_Cu: "))
    init_temp = float(input("init_temp: "))
    m_ice = float(input("m_ice: "))
    init_temp2 = float(input("init_temp2: "))
    c_ice = float(input("c_ice: "))
    L_f = float(input("L_f: "))
    Q_Cu = mass/1000*c_Cu * (init_temp - 0)
    Q_icewarm = m_ice * c_ice * abs(init_temp2)
    result = m_ice - (Q_Cu - Q_icewarm)/(L_f*1000)
    print(result)
    print("")

def method11():
    print("give moles, initialTemp, Q")
    n = float(input("moles: ")) #8.95  # moles of gas
    initial_temp_C = float(input("initialTemp: ")) #139  # initial temperature in degrees Celsius
    Q = float(input("Q: ")) * 1000 #3340  # heat added in Joules (3.34 kJ)

    # Constants
    R = 8.314  # ideal gas constant, J/mol·K
    f = 3  # degrees of freedom for a monatomic gas

    # Calculate C_V for a monatomic ideal gas
    C_V = (f / 2) * R  # J/mol·K

    # Calculate the change in temperature (Delta T)
    delta_T = Q / (n * C_V)  # change in temperature in Kelvin

    # Convert initial temperature to Kelvin for addition
    initial_temp_K = initial_temp_C + 273.15  # convert Celsius to Kelvin

    # Calculate final temperature in Kelvin
    final_temp_K = initial_temp_K + delta_T

    # Convert final temperature back to Celsius
    final_temp_C = final_temp_K - 273.15
    result = final_temp_C
    print(result)
    print("")

def method12():
    print("give moles, temperature")
    var1 = float(input("moles: "))
    var2 = float(input("temperature: "))
    result = var1 * 5 * (var2 + 273.5) * 8.314 / 2 / 1000
    print(result)
    print("")

def method13(): 
    print("give t_h, t_c, q_h, q_c")
    t_h = float(input("t_h: "))
    t_c = float(input("t_c: "))
    q_h = float(input("q_h: "))
    q_c = float(input("q_c: "))
    result = (abs(q_h) - abs(q_c)) / q_h
    print("As percent:", result*100)
    print("")

def method14():
    print("give mass, temp, pressure, initATM, molMass, c_p")
    mass = float(input("mass: "))
    temp = float(input("temp: "))
    pressure = float(input("pressure: "))
    initATM = float(input("length: "))
    molMass = float(input("molMass: "))
    C_p = float(input("c_p: "))
    # Constants
    R = 8.314  # J/(mol*K)

    # Problem 1: Entropy Change for Isochoric Heating of an Ideal Diatomic Gas
    m = mass  # grams
    T_i = temp + 273.15  # Convert Celsius to Kelvin
    P_i = pressure  # atm
    P_f = initATM  # atm
    M = molMass  # g/mol
    C_v = C_p - R  # Calculate C_v

    # Calculations
    n = m / M  # number of moles
    T_f = T_i * (P_f / P_i)  # final temperature using isochoric process
    delta_S_gas = n * C_v * np.log(T_f / T_i)  # entropy change
    result = delta_S_gas
    print(result)
    print("")

def method15():
    print("give d, lambda_light, I_0, theta ")
    d = float(input("d: "))
    lambda_light = float(input("lambda_light: "))
    I_0 = float(input("I_0: "))
    theta = float(input("theta: "))

    # Given values
    d = d * 10**-6  # distance between the slits in meters
    lambda_light = lambda_light * 10**-9  # wavelength of the light in meters

    # Convert theta to radians for calculation
    theta_rad = theta * (pi / 180)

    # Calculate beta
    beta = (math.pi * d * sin(theta_rad)) / lambda_light

    I_corrected = I_0 * (cos(pi * d * sin(theta_rad) / lambda_light)) ** 2

    result = I_corrected
    print(result)
    print("")

def method16():
    print("give lambda, angle_third, angle_second")
    lambda_1 = float(input("lambda: "))
    theta_1 = float(input("angle_third: "))
    theta_2 = float(input("angle_second: "))

    # Given values
    lambda_1 = lambda_1  # wavelength in nm for the first light
    theta_1 = radians(theta_1)  # angle in radians for the first light
    m_1 = 3  # order of maximum for the first light

    theta_2 = radians(theta_2)  # angle in radians for the second light
    m_2 = 2  # order of maximum for the second light

    # Calculate lambda_2 using the division of the two equations
    lambda_2 = (sin(theta_2) / sin(theta_1)) * (m_1 / m_2) * lambda_1


    result = lambda_2
    print(result)
    print("")

def method17():
    print("give n1, n2, normal_incident")
    n_f = float(input("n1: "))
    n_ref = float(input("n2: "))
    lambda_0 = float(input("normal_incident: "))
    m = 0  # order of the minimum for the minimum nonzero thickness

    # Calculate the minimum nonzero thickness of the film
    t_min = ((m + 0.5) * lambda_0) / (2 * n_f)

    result = t_min
    print(result)
    print("")

def method18():
    print("give placed, mag")
    placed = float(input("placed: "))
    mag = float(input("mag: "))
    u = placed  # cm (object distance)
    M_image = mag  # magnification
    v = -M_image * u  # image distance
    result = v
    print(result)
    print("")

def method19():
    print("give front, magnification")
    # Given values
    d_o = float(input("front: "))
    M = float(input("magnification: "))

    # Calculate image distance using magnification formula
    d_i = -M * d_o

    # Calculate focal length using mirror equation
    f = 1 / (1/d_o + 1/d_i)

    result = f

    print(result)
    print("")

def method20():
    print("give tall, located, distance")
    tall = float(input("tall: "))
    located = float(input("located: "))
    distance = float(input("distance: "))
    d_o_3 = located  # Object distance in cm
    d_i_3 = -1*distance  # Image distance (negative for virtual image)
    focal_length_lens = 1 / (1/d_o_3 + 1/d_i_3)
    result = focal_length_lens
    print(result)
    print("")

def method21():
    print("give index_refraction")
    i_ref = float(input("index of refraction: "))
    r_1 = math.asin((1 / i_ref) * math.sin(degreeToRadian(30)))
    i2 = 60 - radianToDegree(r_1)
    r2 = math.asin(i_ref * math.sin(degreeToRadian(i2)))
    result = radianToDegree(r2)
    print(result)
    print("")

def method22():
    print("give height, distance, f_1focal, distance2, f_2focal")
    height = float(input("height: "))
    distance = float(input("distance: "))
    f_1focal = float(input("f_1focal: "))
    distance2 = float(input("distance2: "))
    f_2focal = float(input("f_2focal: "))

    d_i1 = 1 / (1/f_1focal - 1/distance)
    d_o2 = math.fabs(d_i1) + distance2
    d_i2 = 1 / (1/f_2focal - 1/d_o2)

    result = d_i1 / distance * height * -d_i2 / d_o2
    print(result)
    print("")

def method23():
    print("give left_speed, right_speed, A_emit")
    u_A = float(input("left_speed: "))
    v_B = float(input("right_speed: "))
    lambda_A = float(input("A_emit: "))

    # Constants and given values
    c = 1  # Speed of light normalized to 1 for calculation purposes

    # Relative velocity u' calculation
    u_prime = (u_A + v_B) / (1 + u_A * v_B / c**2)

    # Applying the relativistic Doppler effect formula for wavelength
    lambda_observed = lambda_A * ((1 - u_prime / c) / (1 + u_prime / c))**0.5

    result = lambda_observed
    print(result)
    print("")

def method24():
    print("give proton_speed")
    v_proton = float(input("proton_speed: "))

    # Constants
    h = 6.62607015e-34  # Planck's constant in J*s
    m_proton = 1.67262192369e-27  # Proton mass in kg
    c = 3e8  # Speed of light in m/s
    eV_to_J = 1.60218e-19  # Conversion factor from eV to Joules

    # Proton velocity in m/s
    v_proton_m_s = v_proton * 1000  # Convert km/s to m/s

    # Calculate the proton's momentum
    p_proton = m_proton * v_proton_m_s

    # Calculate the de Broglie wavelength of the proton
    lambda_proton = h / p_proton

    # Calculate the energy of the photon with the same wavelength
    E_photon = (h * c) / lambda_proton

    # Convert energy from Joules to keV
    E_photon_keV = E_photon / eV_to_J / 1000  # Convert to keV
    result = E_photon_keV
    print(result)
    print("")

def method25():
    print("give n, degrees")
    n = float(input("n: "))
    degrees = float(input("degrees: "))
    theta_b = degrees * pi / 180  # Convert degrees to radians
    n_water = n  # Refractive index of water
    n_plastic = n_water * np.tan(theta_b)  # Refractive index of plastic
    result = n_plastic
    print(result)
    print("")

def method26():
    print("give kg, temp, temp2, spec_heat")
    # Given values
    mass_lead1 = float(input("kg: ")) # kg
    initial_temp_lead1 = float(input("temp: "))  # K
    final_temp_lead = float(input("temp2: "))  # K
    specific_heat_lead1 = float(input("spec_heat: "))  # J/kgK

    # Let's re-calculate the total entropy change in a way that considers different parameters or corrects potential oversights.

    # Constants for the calculations
    specific_heat_lead = specific_heat_lead1  # J/kgK
    mass_lead = mass_lead1  # kg
    initial_temp_lead = initial_temp_lead1  # degrees Celsius
    final_temp_lake = final_temp_lead  # degrees Celsius
    initial_temp_lead_K = initial_temp_lead + 273.15  # Convert to Kelvin
    final_temp_lake_K = final_temp_lake + 273.15  # Convert to Kelvin

    # Calculating the change in entropy for the lead
    delta_temp_lead = final_temp_lake - initial_temp_lead
    delta_entropy_lead = mass_lead * specific_heat_lead * np.log(final_temp_lake_K / initial_temp_lead_K)

    # Assume lake has large heat capacity so its change in temperature is negligible
    # Calculating the heat transferred from lead to lake
    q_lead = mass_lead * specific_heat_lead * (final_temp_lake_K - initial_temp_lead_K)  # Negative, heat lost by lead

    # Entropy change for the lake
    # Assume heat gained by lake is absorbed at a nearly constant temperature (large body of water)
    delta_entropy_lake = -q_lead / final_temp_lake_K  # Negative of heat lost by lead to calculate gain by lake

    # Total entropy change of the system
    total_entropy_change_revised = delta_entropy_lead + delta_entropy_lake

    result = total_entropy_change_revised
    print(result)
    print("")

def method27():
    print("give M_molMass, temp1, steel_mass, steel_temp, final_temp")
    M_molMass = float(input("M_molMass: "))
    temp1 = float(input("temp1: "))
    steel_mass = float(input("steel_mass: "))
    steel_temp = float(input("steel_temp: "))
    f_temp = float(input("final_temp: "))

    # Constants for neon gas mass calculation
    mass_steel = steel_mass / 1000  # Convert to kg
    initial_temp_neon = temp1 + 273.15  # Convert to Kelvin
    initial_temp_steel = steel_temp + 273.15  # Convert to Kelvin
    final_temp = f_temp + 273.15  # Convert to Kelvin

    
    specific_heat_steel = 502.4  # J/(kg*K)
    R = 8.31446  # J/(K*mol)

    molar_mass_neon = M_molMass / 1000
    C_v_neon = (3 / 2) * R
    Q_steel = mass_steel * specific_heat_steel * (final_temp - initial_temp_steel)
    # Calculate number of moles of neon
    n_neon = Q_steel / (C_v_neon * (final_temp - initial_temp_neon))
    # Convert moles to mass
    mass_neon = n_neon * molar_mass_neon * 1000  # Convert to grams
    result = mass_neon*-1

    print(result)
    print("")

def method28():
    print("give ice_grams, alum_gram, celcius, unknown_grams, final_temp")
    ice_grams = float(input("ice_grams: "))
    alum_gram = float(input("alum_gram: "))
    celcius = float(input("celcius: "))
    unknown_grams = float(input("unknown_grams: "))
    final_temp = float(input("final_temp: "))

    mass_ice = ice_grams / 1000  # convert to kg
    temp_initial_ice = 0 + 273.15  # melting point of ice in K
    mass_aluminum = alum_gram / 1000  # convert to kg
    temp_initial_aluminum = celcius + 273.15  # convert to K
    mass_liquid = unknown_grams / 1000  # convert to kg
    temp_final_system = final_temp + 273.15  # convert to K

    c_aluminum = 900  # J/kg*K
    c_water = 4186  # J/kg*K
    latent_heat_fusion_water = 334000  # J/kg

    c_liquid = (mass_aluminum * c_aluminum * (temp_final_system - temp_initial_aluminum) + mass_ice * latent_heat_fusion_water + mass_ice * c_water * (temp_final_system - temp_initial_ice)) / (mass_liquid * (temp_final_system - temp_initial_aluminum))
    result = c_liquid*-1
    print(result)
    print("")

def method29():#$###############
    print("give atomic_num")
    atomic_num = float(input("atomic_num: "))

    # Given values
    n = 4  # Principal quantum number for the 3rd excited state
    Z = atomic_num  # Atomic number for the ion

    # Calculating the radius ratio r_n / a_0
    radius_ratio = n**2 / Z
    result = radius_ratio / 2 * 1.125

    print(result)
    print("")

def method30():
    print("give maximum, degree")
    maximum = float(input("maximum: "))
    degree = float(input("degree: "))
    lambda_nm = maximum  # wavelength in nm
    theta_deg = degree  # angle in degrees
    theta_rad = math.radians(theta_deg)  # convert degrees to radians
    m = 4  # order of maximum
    d = m * lambda_nm * 1e-9 / math.sin(theta_rad)  # grating spacing in meters
    lines_per_cm = 1 / (d * 100)  # number of lines per cm
    result = lines_per_cm
    print(result)
    print("")

def method31():
    print("give mass, speed")
    mass = float(input("mass: "))
    speed = float(input("speed: "))
    helium_mass = mass*10**-27  # in kg
    helium_speed = speed * c  # 0.608 times the speed of light
    helium_momentum = helium_mass * helium_speed / np.sqrt(1 - (helium_speed / c)**2)  # Relativistic momentum
    result = helium_momentum * c / (1.60218e-13) 
    print(result)
    print("")

def method32():
    print("give tall, located, mag")
    tall = float(input("tall: "))
    located = float(input("located: "))
    mag = float(input("mag: "))
    magnification = mag
    d_i = -1*located  # cm (negative for virtual image)
    # From magnification relation, d_o = -d_i / M
    d_o = -d_i / magnification
    focal_length = 1 / (1/d_o + 1/d_i)
    result = focal_length
    print(result)
    print("")



def default():
    print("Invalid choice")

def generate_switch_dict():
    switch_dict = {}
    for i in range(1, 33):
        switch_dict[i] = globals().get(f"method{i}", default)
    return switch_dict

def switch_case(choice):
    switch_dict = generate_switch_dict()

    if choice == 0:
        print("Exiting the program. Goodbye!")
        exit()

    # Use get() method to handle default case
    selected_method = switch_dict.get(choice, default)
    selected_method()

def main():
    while True:
        print("Select a method (1-32) or enter 0 to quit: ")
        try:
            choice = int(input())
            if 0 <= choice <= 32:
                switch_case(choice)
            else:
                print("Invalid choice. Please enter a number between 0 and 32.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
