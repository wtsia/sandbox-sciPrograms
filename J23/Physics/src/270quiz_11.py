import math
from math import cos, sin, pi, radians
from sympy import symbols, Eq, solve

# Constants
h = 4.135667696e-15  # Planck's constant in eV·s
c = 3e8  # Speed of light in m/s
m_e = 9.10938356e-31  # Electron rest mass in kg
m_p = 1.6726219e-27  # Proton mass in kg
c_nm = 3e17  # Speed of light in nm/s

def method1():
    print("give lambda, kinetic")
    lambda1 = float(input("lambda: "))
    kinetic = float(input("kinetic: "))

    lambda_1 = lambda1  # nm
    KE_max = kinetic  # eV
    nu_1 = c_nm / lambda_1  # Frequency in s^-1
    E_photon = h * nu_1  # Photon energy in eV
    work_function = E_photon - KE_max  # Work function in eV

    result = work_function
    print(result)

def method2():
    print("give energy")
    energy = float(input("energy: "))


    ionization_energy = energy  # eV
    lambda_2 = (c_nm * h) / ionization_energy 

    result = lambda_2
    print(result)

def method3():
    print("give temp, temp2")
    temp = float(input("temp: "))
    temp2 = float(input("temp2: "))

    T1 = temp  # Initial temperature in K
    T2 = temp+temp2  # Final temperature in K
    # Wien's Displacement Law
    wien_constant = 2.898e-3  # m·K
    lambda_max_1 = wien_constant / T1  # m
    lambda_max_2 = wien_constant / T2  # m
    delta_lambda_max = (lambda_max_2 - lambda_max_1) * 1e6

    result = delta_lambda_max
    print(result)

def method4():
    print("give degrees")
    degrees = float(input("degrees: "))

    # Constants
    h = 6.62607015e-34  # Planck's constant in J*s
    m_e = 9.10938356e-31  # Electron mass in kg
    c = 3e8  # Speed of light in m/s

    # Angle in degrees
    theta_degrees = degrees
    # Convert angle to radians
    theta_radians = math.radians(theta_degrees)

    # Compton shift formula
    compton_shift = (h / (m_e * c)) * (1 - math.cos(theta_radians))

    # Convert from meters to picometers
    compton_shift_pm = compton_shift * 1e12  # 1 picometer = 10^-12 meters
    result = compton_shift_pm
    print(result)

def method5():
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

# Input array from the user
inputChoice = ["method1", "method2", "method3", "method4", "method5"]
formatted_string = ", ".join([str(element) for element in inputChoice])

# Printing the formatted string
print(f"Enter a method to execute ({formatted_string})")
choice = input("choice: ")

# Check the user's choice and call the corresponding method
if choice == 'method1':
    method1()
elif choice == 'method2':
    method2()
elif choice == 'method3':
    method3()
elif choice == 'method4':
    method4()
elif choice == 'method5':
    method5()
elif choice == 'q':
    exit()
else:
    print("Invalid choice. Please enter 1, 2, 3, 4, and 5.")
