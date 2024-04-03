import math
from math import cos, sin, pi, radians

def method1():
    print("give lambda, lines/cm, degree")
    lambda_m = float(input("lambda: "))
    lines_per_cm = float(input("lines/cm: "))
    degree = float(input("degree: "))

    # Re-calculating with the aim to confirm the analysis leading to 21 total fringes
    # Given values
    lines_per_cm = 1761  # lines per centimeter
    wavelength_nm = lambda_m  # wavelength in nanometers

    # Convert lines per cm to meters (for spacing d)
    lines_per_meter = lines_per_cm * 100  # Convert lines per cm to lines per meter
    d_m = 1 / lines_per_meter  # Calculate d in meters

    # Convert wavelength from nm to meters
    wavelength_m = wavelength_nm * 1e-9  # Convert nm to meters

    # Calculate the maximum order m for theta = 90 degrees, using sin(90) = 1
    m_max = d_m / wavelength_m

    m_max = round(m_max)


    result = 2*m_max + 1
    print(result)

def method2():
    print("give lambda, width")
    lambda2 = float(input("lambda: "))
    width = float(input("width: "))

    # Given values
    lambda_m = lambda2*10**-9  # Wavelength in meters
    a_m = width*10**-3  # Slit width in meters

    # Calculate angular width in radians
    delta_theta_radians = 2 * (lambda_m / a_m)

    # Convert to degrees
    delta_theta_degrees = delta_theta_radians * (180 / math.pi)

    delta_theta_degrees

    result = delta_theta_degrees
    print(result)

def method3():
    print("give s, lambda, and d")
    s = float(input("s: "))
    lambda3 = float(input("lambda: "))
    d = float(input("d: "))
    # Given values in meters
    lambda_m = lambda3*10**-3  # Wavelength in meters
    D_m = d*10**-2  # Diameter of the lens in meters

    # Calculate minimum resolution in radians using the Rayleigh criterion
    theta_radians = 1.22 * (lambda_m / D_m)

    # Convert to degrees
    theta_degrees = theta_radians * (180 / math.pi)

    theta_degrees

    result = theta_degrees
    print(result)

def method4():
    print("give s, lambda, and d")
    s = float(input("s: "))
    lambda4 = float(input("lambda: "))
    d = float(input("d: "))
    # Given values in meters and nanometers
    s_m = s  # Separation between the sources in meters
    lambda_m = lambda4*10**-9  # Wavelength in meters
    D_m = d*10**-2  # Diameter of the lens in meters

    # Calculate theta using the Rayleigh criterion
    theta_radians = 1.22 * (lambda_m / D_m)

    # Calculate the distance L from the lens to the sources in meters
    L_m = s_m / theta_radians

    # Convert L to Megameters (Mm)
    L_Mm = L_m / 1e6  # Convert from meters to Megameters

    L_Mm


    result = L_Mm
    print(result)

def method5():
    print("give lambda, a, dist_to_slit, minimum")
    lambda5 = float(input("lambda: "))
    a = float(input("a: "))
    dist_to_slit = float(input("dist_to_slit: "))
    minimum = float(input("minimum: "))

    # Constants
    lambda_m = lambda5*10**-9  # Wavelength in meters
    a_m = a*10**-3  # Slit width in meters
    L_m = dist_to_slit  # Distance from the slit to the screen in meters
    n = minimum  # Order of the minimum

    # Calculate theta_n using sin(theta) approximation
    theta_n = n * lambda_m / a_m

    # Calculate y_n on the screen
    y_n_m = L_m * theta_n  # For small theta, tan(theta) approx equals sin(theta)

    # Convert y_n to centimeters
    y_n_cm = y_n_m * 100

    y_n_cm


    result = y_n_cm
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
