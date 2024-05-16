import math
from math import cos, sin, pi, radians

def method1():
    print("give long, c")
    long = float(input("long: "))
    cmes = float(input("c: "))
    # Constants
    L = long  # Rest length of the particle accelerator in meters
    v_fraction_of_c = cmes  # Velocity as a fraction of the speed of light
    c = 3.00e8  # Speed of light in m/s

    # Calculate the velocity of the particle
    v = v_fraction_of_c * c

    # Calculate the contracted length
    L_prime = L * ((1 - v**2 / c**2) ** 0.5)
    result = L_prime
    print(result)

def method2():
    print("give init_speed, c")
    init_speed = float(input("init_speed: "))
    cmes = float(input("c: "))

    # Redefining the constants and variables to re-attempt the calculation

    m0 = 1.6726219e-27  # Rest mass of a proton in kg, redefined due to previous cell error
    c = 3.00e8  # Speed of light in m/s, redefined
    v_initial = init_speed * c  # Initial speed of the proton, redefined
    v_final = cmes * c  # Final speed of the proton, redefined
    joule_to_mev = 6.242e12  # Conversion factor from joules to MeV, redefined

    # Calculate the initial and final kinetic energy
    KE_initial = (m0 * c**2) / ((1 - v_initial**2 / c**2)**0.5) - m0 * c**2
    KE_final = (m0 * c**2) / ((1 - v_final**2 / c**2)**0.5) - m0 * c**2

    # Calculate the energy difference in MeV
    delta_KE_MeV = (KE_final - KE_initial) * joule_to_mev

    result = delta_KE_MeV
    print(result)

def method3():
    print("give years, c")
    years = float(input("years: "))
    cmes = float(input("c: "))

    # Re-defining constants and performing the calculation again after reset
    t0 = years  # Proper time in years
    v_fraction_of_c = cmes  # Velocity as a fraction of the speed of light

    # Calculate the time elapsed on Earth
    t = t0 / ((1 - v_fraction_of_c**2) ** 0.5)
    result = t

    print(result)

def method4():
    print("give speed, microseconds")
    speed = float(input("speed: "))
    ms = float(input("microseconds: "))

    # Constants
    t = ms*10**-6  # Dilated time in seconds
    v = speed*10**8  # Velocity of the particle in m/s
    c = 3.00e8  # Speed of light in m/s

    # Calculate the proper time (lifetime in the particle's rest frame)
    t0 = t * ((1 - v**2 / c**2) ** 0.5)

    # Convert the time back to microseconds for the result
    t0_microseconds = t0 * 1e6
    result = t0_microseconds
    print(result)

def method5():
    print("give percent")
    percent = float(input("percent: "))

    # Given
    L_L0_ratio = percent/100  # L / L0 ratio

    # Calculate v^2 / c^2
    v_squared_over_c_squared = 1 - L_L0_ratio**2

    # Solve for v/c
    v_over_c = v_squared_over_c_squared ** 0.5
    result = v_over_c
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
