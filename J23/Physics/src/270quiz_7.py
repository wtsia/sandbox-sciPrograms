import math
from math import cos, sin, pi, radians

def method1():
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

def method2():
    print("give phi, lambda_nm")
    phi = float(input("phi: "))
    lambda_nm = float(input("lambda_nm: "))

    # Calculate the path length difference in nm
    delta_L = (lambda_nm * phi) / (2 * pi)
    result = delta_L
    print(result)

def method3():
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

def method4():
    print("give n1, n2, normal_incident")
    n_f = float(input("n1: "))
    n_ref = float(input("n2: "))
    lambda_0 = float(input("normal_incident: "))
    m = 0  # order of the minimum for the minimum nonzero thickness

    # Calculate the minimum nonzero thickness of the film
    t_min = ((m + 0.5) * lambda_0) / (2 * n_f)

    result = t_min
    print(result)

def method5():
    print("give slit_separation, flat_screen, fringe_detec")
    slit_sep = float(input("slit_separation: "))
    flat_scr = float(input("flat_screen: "))
    y_m = float(input("fringe_detec: "))

    # Given values
    d = slit_sep*10**-5  # slit separation in meters
    L = flat_scr  # distance from the slits to the screen in meters
    y_m = y_m / 100  # position of the 7th bright fringe from the central fringe in meters (converted from cm)
    m = 7  # order of the fringe

    # Calculate the wavelength of the light in meters
    lambda_m = (y_m * d) / (m * L)

    # Convert the wavelength from meters to nanometers
    lambda_nm = lambda_m * 1e9

    result = lambda_nm
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
