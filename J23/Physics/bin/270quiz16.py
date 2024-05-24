import math

def method1():
    print("give q_heat, mass, temp_init")
    q_heat = float(input("q_heat: "))
    mass = float(input("mass: "))
    temp_init = float(input("temp_init: "))
    q = mass * 334
    deltaS1 = q / (temp_init + 273)
    t =  (q_heat*1000 - q)/(mass / 1000)/4186
    deltaS2 = (mass / 1000) * (4186) * math.log((t + 273) / (temp_init + 273))
    result = deltaS1 + deltaS2
    print(result)

def method2():
    print("give n1, n2, incident,")
    n1 = float(input("n1: "))
    n2 = float(input("n2: "))
    incident = float(input("incident: "))

    thickness_oil = incident / 4 / n1

    result = thickness_oil
    print(result)

def method3(): ######
    print("give index, index2")
    var1 = float(input("index: "))
    var2 = float(input("index2: "))
    # Given indices of refraction
    n1 = var1  # index of refraction of the substance
    n2 = var2   # index of refraction of water

    # Calculate the critical angle
    theta_c_rad = math.asin(n2 / n1)
    theta_c_deg = math.degrees(theta_c_rad)

    result = theta_c_deg
    print(result)

def method4():
    print("give index, tall, left, right")
    n2 = float(input("index: "))
    tall = float(input("tall: "))
    u = float(input("left: "))
    v = float(input("right: "))

    # Given values
    n1 = 1
    u = -u  # object distance in cm

    # Calculating the radius of curvature (R)
    R = (n2 - n1) / ((n2 / v) - (n1 / u))

    result = R
    print(result)

def method5():
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

def method6():
    print("give n, energy")
    var1 = float(input("n: "))
    var2 = float(input("energy: "))

    # Constants
    E_n = var2 * 1.60218e-13  # convert MeV to Joules
    m_proton = 1.67262e-27    # mass of proton in kg

    # Calculate speed
    v = math.sqrt(2 * E_n / m_proton)

    # Convert speed from m/s to km/s
    v_km_s = v / 1000

    result = v_km_s
    print(result)


# Input array from the user
inputChoice = ["method1", "method2", "method3", "method4", "method5", "method6"]
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
elif choice == 'method6':
    method6()
elif choice == 'q':
    exit()
else:
    print("Invalid choice. Please enter 1, 2, 3, 4, and 5.")
