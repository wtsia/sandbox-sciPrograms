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

def method14(): #####################################
    print("give resivity, current, radius, length")
    resivity = float(input("resivity: "))
    current = float(input("current: "))
    radius = float(input("radius: "))
    length = float(input("length: "))
    resistance = (resivity * (10 ** -9) * length) / (math.pi * (radius / 100) ** 2)
    result = current * resistance * 1000000
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

def method18(): ######################################
    print("give protonVel, b_x, b_y, b_z")
    protonVel = float(input("protonVel: "))
    b_x = float(input("b_x: "))
    b_y = float(input("b_y: "))
    b_z = float(input("b_z: "))
    new_y = protonVel*b_x*1.6/1000
    new_x = protonVel*b_y*-1.6/1000
    result = 180 + (math.atan(new_y/new_x) * 180 / math.pi)
    print(result)
    print("")

def method19(): ################################
    print("give current, arcRadius, uniformField")
    current = float(input("current: "))
    arcRadius = float(input("arcRadius: "))
    uniformField = float(input("uniformField: "))
    h = math.sqrt(2 * ((arcRadius/100) ** 2))
    result = current * h * uniformField
    print(result)
    print("")

def method20():####################################
    print("give radius, distance, and centralAxisMagField")
    radius = float(input("radius: "))
    distance = float(input("distance: "))
    centralAxisMagField = float(input("centralAxisMagField: "))
    tmpcurr = math.pi / 1000000 * distance**2
    result = (centralAxisMagField / 1000000) * (2 * math.pi * distance / 1000) / ((4*math.pi / 10000000) * (tmpcurr)) 
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

def method25(): ###################################################
    print("give a, b, i")
    a = float(input("a: "))
    b = float(input("b: "))
    i = float(input("i: "))
    result = 4 * math.pi * (10 ** -7) * i / 8 * (1/a - 1/b) * 1000000
    print(result)
    print("")

def method26(): #########################################
    print("give turns, curr, radius, bx, by, bz")
    turns = float(input("turns: "))
    curr = float(input("curr: "))
    radius = float(input("radius: "))
    bx = abs(float(input("bx: ")))
    by = abs(float(input("by: ")))
    bz = abs(float(input("bz: ")))
    area = math.pi*((radius/100) ** 2)
    i = curr * turns * area * bx
    j = curr * turns * area * by
    torque =  (i ** 2) +  (j ** 2)
    result = math.sqrt(torque)
    print(result)
    print("")

def method27(): #$###############
    print("give hz, mh, percent")
    hz = float(input("hz: "))
    mh = float(input("mh: "))
    percent = float(input("percent: "))
    result = 10000000/(4*(math.pi**2)*(hz**2)*mh)*percent
    print(result)
    print("")

def method28():#$###############
    print("give turns, length, radius, turns2, length2, radius2")
    turns = float(input("turns: "))
    length = float(input("length: "))
    radius = float(input("radius: "))
    turns2 = float(input("turns2: "))
    length2 = float(input("length2: "))
    radius2 = float(input("radius2: "))
    area2 = math.pi * ((radius2/100) ** 2)
    result = mu_0 * turns * turns2 * area2 / (length / 100) * 1000
    print(result)
    print("")

def method29():#$###############
    print("give turnCoil, diameter, magField, degree, percent, seconds")
    turnCoil = float(input("turnCoil: "))
    diameter = float(input("diameter: "))
    magField = float(input("magField: "))
    degree = float(input("degree: "))
    percent = float(input("percent: "))/100
    seconds = float(input("seconds: "))
    result = abs(turnCoil*math.pi*((diameter/2)**2) * (percent*magField - magField) * math.cos((90-degree)/180*math.pi) / (seconds) / 10000)
    print(result)
    print("")

def method30():#$###############
    print("give ohm1, ohm2, ohm3")
    ohm1 = float(input("ohm1: "))
    ohm2 = float(input("ohm2: "))
    ohm3 = float(input("ohm3: "))
    result = 1/(1/ohm1 + 1/ohm2 + 1/ohm3)
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

def method32(): #$###############
    print("give rate, distance")
    rate = float(input("rate: "))
    distance = float(input("distance: "))
    result = 2*rate/distance*10
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
