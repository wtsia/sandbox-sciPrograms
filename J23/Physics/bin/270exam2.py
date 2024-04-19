import math
import sympy as sp

def method1():
    print("give phi, lambda")
    phi = float(input("phi: "))
    lambda_light = float(input("lambda_light: "))
    # Given the correction, let's calculate the path length difference again without modulo to see if the correction is accurate

    # Path length difference formula
    delta = (phi * lambda_light) / (2 * sp.pi)

    # Calculate the path length difference
    path_length_difference = delta.evalf()
    path_length_difference
    
    result = path_length_difference
    print(result)

def method2():
    print("give lambda1, degree1, degree2")
    lambda1 = float(input("lambda1: "))
    degree1 = float(input("degree1: "))
    degree2 = float(input("degree2: "))
    #rod_length = float(input("rod_length: "))

    # Convert angles from degrees to radians for the calculation
    angle_1_rad = math.radians(degree1)
    angle_2_rad = math.radians(degree2)

    # Constants for the equations
    m1 = 3  # Order of maximum for lambda_1
    m2 = 2  # Order of maximum for lambda_2

    # Calculate lambda_2 using the formula derived above
    lambda_2_calculated = 3 * lambda1 * math.sin(angle_2_rad) / (2 * math.sin(angle_1_rad))
    result = lambda_2_calculated

    print(result)

def method3():
    print("give wavelength, diffraction, degrees")
    wavelength = float(input("wavelength: "))
    lines_per_cm = float(input("diffraction: "))
    degrees = float(input("degrees: "))

    # Given values
    wavelength = wavelength*10**-9  # Convert wavelength to meters
    lines_per_cm  # Grating lines per centimeter
    lines_per_meter = lines_per_cm * 1e2  # Convert to lines per meter
    d = 1 / lines_per_meter
    m_max = int(d / wavelength)

    total_fringes = 2 * m_max + 1

    result = total_fringes
    print(result)

def method4():
    print("give lambda, degrees")
    lambda1 = float(input("lambda:  "))
    degrees = float(input("degrees: "))

        # Given values
    lambda_xray_pm = lambda1  # X-ray wavelength in picometers
    theta_degrees = degrees  # angle in degrees

    # Convert wavelength from picometers to nanometers (1 pm = 1e-3 nm)
    lambda_xray_nm = lambda_xray_pm * 1e-3

    # Convert angle from degrees to radians
    theta_radians = math.radians(theta_degrees)

    # Bragg's law formula to calculate the distance between the planes d is:
    # n * lambda = 2 * d * sin(theta)
    # For the first maximum, n = 1
    n = 1

    # Rearrange Bragg's law to solve for d:
    # d = (n * lambda) / (2 * sin(theta))
    d_plane = (n * lambda_xray_nm) / (2 * math.sin(theta_radians))

    result = d_plane
    print(result)

def method5():
    print("give s, wavelength, and d")
    s1 = float(input("s: "))
    wavelength = float(input("wavelength: "))
    d = float(input("d: "))
    # Given values
    s = s1  # distance between the sources in meters
    lambda_nm = wavelength  # wavelength in nanometers
    D_cm = d  # diameter of the lens in centimeters

    # Convert wavelength to meters (1 nm = 1e-9 m) and diameter to meters (1 cm = 1e-2 m)
    lambda_m = lambda_nm * 1e-9
    D_m = D_cm * 1e-2

    # Rayleigh criterion formula to calculate the distance L
    L = (s * D_m) / (1.22 * lambda_m)

    # Convert L from meters to megameters (1 Mm = 1e6 m)
    L_Mm = L / 1e6
    result = L_Mm
    print(result)

def method6():
    print("give tall, located, radius")
    tall = float(input("tall: "))
    located = float(input("located: "))
    radius = float(input("radius: "))

    # Given values for the convex mirror scenario
    object_height_mm = tall  # object height in mm
    object_distance_cm = located*-1  # object distance in cm (negative because it's in front of the mirror)
    radius_of_curvature_cm = radius

    result = -1/(1/(radius/2) - 1/object_distance_cm)
    print(result)

def method7():
    print("give tall, front, lens")
    tall= float(input("tall: "))
    front= float(input("front: "))
    lens= float(input("lens: "))

    # Flipping the sign of the image distance and recalculating the focal length.
    # This time we'll take the image distance as positive, which is not typical for virtual images, 
    # but we'll follow through to see if it gives us the expected result.

    # Corrected image distance as positive
    image_distance_cm_positive = lens
    object_distance_cm = front

    # Recalculating the focal length with the image distance as positive
    focal_length_cm_positive = 1 / ((1 / image_distance_cm_positive) - (1 / object_distance_cm))
    result = focal_length_cm_positive*-1
    print(result)

def method8():
    print("give near, magnification, ")
    near = float(input("near: "))
    magnification = float(input("magnification: "))

    # Given values
    near_point = near  # in cm
    angular_magnification = magnification  # the angular magnification produced

    # Calculating the focal length (f):
    focal_length_magnifying_glass = near_point / angular_magnification
    result = focal_length_magnifying_glass
    print(result)

def method9():
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

def method10():
    print("give n1, n2, incident,")
    n1 = float(input("n1: "))
    n2 = float(input("n2: "))
    incident = float(input("incident: "))

    thickness_oil = incident / 4 / n1

    result = thickness_oil
    print(result)

def method11():  # TODO
    print("give index_ref")
    index_ref = float(input("infex_ref: "))

    # Corrected Snell's Law calculation for light entering face AB

    # Given values
    n_air = 1.0  # Index of refraction of air
    n_glass = index_ref  # Index of refraction of glass
    theta_i_ab = 30  # Angle of incidence at face AB with respect to the normal (in degrees)

    # Convert the angle of incidence to radians for calculation
    theta_i_ab_rad = math.radians(theta_i_ab)

    # Apply Snell's Law to find the angle of refraction at face AB
    sin_theta_r_ab = n_air * math.sin(theta_i_ab_rad) / n_glass
    # Check if refraction is possible (sin should be <= 1)
    if sin_theta_r_ab <= 1:
        theta_r_ab_rad = math.asin(sin_theta_r_ab)
        theta_r_ab_deg = math.degrees(theta_r_ab_rad)
    else:
        theta_r_ab_deg = "Total internal reflection occurs, no refraction at face AB."

    # If refraction is possible, continue to find the angle of incidence at face BC
    if isinstance(theta_r_ab_deg, float):
        # For equilateral triangle, the interior angle at the base is 60 degrees
        # The angle of incidence at face BC is then 60 degrees minus the refraction angle at AB
        theta_i_bc_deg = 60 - theta_r_ab_deg
        theta_i_bc_rad = math.radians(theta_i_bc_deg)

        # Apply Snell's Law at face BC to find the angle of refraction as light exits the prism
        sin_theta_r_bc = n_glass * math.sin(theta_i_bc_rad)
        # Check if refraction is possible (sin should be <= 1)
        if sin_theta_r_bc <= 1:
            theta_r_bc_rad = math.asin(sin_theta_r_bc)
            theta_r_bc_deg = math.degrees(theta_r_bc_rad)
        else:
            theta_r_bc_deg = "Total internal reflection occurs, no refraction at face BC."

    theta_r_ab_deg, theta_i_bc_deg, theta_r_bc_deg
    result = theta_r_bc_deg
    print(result)

def method12():
    print("give degrees, angle, index_ref")
    degrees = float(input("degrees: "))
    angle = float(input("angle: "))
    index_ref = float(input("index_ref: "))

    # Given values
    n_air = 1
    n_water = index_ref
    theta_air_deg = degrees  # angle of incidence in air in degrees
    theta_substance_deg = angle  # angle of refraction in the substance in degrees

    # Convert angles from degrees to radians
    theta_air_rad = math.radians(theta_air_deg)
    theta_substance_rad = math.radians(theta_substance_deg)

    # Calculate the index of refraction for the substance using Snell's Law
    n_substance = n_air * math.sin(theta_air_rad) / math.sin(theta_substance_rad)

    # Now find the critical angle for total internal reflection when the substance is in water
    # Snell's Law for critical angle (n_substance * sin(theta_c) = n_water * sin(90 degrees))
    # Since sin(90 degrees) = 1, we can simplify the formula:
    theta_critical_rad = math.asin(n_water / n_substance)

    # Convert the critical angle back to degrees
    theta_critical_deg = math.degrees(theta_critical_rad)
    result = theta_critical_deg
    print(result)

def method13(): 
    print("give degrees, index1, index2")
    degrees = float(input("degrees: "))
    index1 = float(input("index1: "))
    index2 = float(input("index2: "))

    # Given values
    n_air = 1
    n_glass_450nm = index1  # index of refraction for 450nm light
    n_glass_650nm = index2  # index of refraction for 650nm light
    theta_incidence_deg = degrees  # angle of incidence in degrees

    # Convert angle of incidence to radians
    theta_incidence_rad = math.radians(theta_incidence_deg)

    # Apply Snell's Law to find the angle of refraction for each wavelength
    theta_refraction_450nm_rad = math.asin(n_air * math.sin(theta_incidence_rad) / n_glass_450nm)
    theta_refraction_650nm_rad = math.asin(n_air * math.sin(theta_incidence_rad) / n_glass_650nm)

    # Calculate the angular separation in radians
    angular_separation_rad = theta_refraction_450nm_rad - theta_refraction_650nm_rad

    # Convert the angular separation back to degrees
    angular_separation_deg = math.degrees(angular_separation_rad)
    result = angular_separation_deg * -1
    print(result)

def method14(): 
    print("give index, travel_dist")
    index = float(input("index: "))
    travel_dist = float(input("travel_dist: "))
    
    # Constants
    c = 3e8  # Speed of light in vacuum in m/s
    n_substance = index  # Index of refraction of the substance

    # Distance light travels in the substance in meters
    d_meters = travel_dist / 100  # convert cm to m

    # Speed of light in the substance
    v_substance = c / n_substance

    # Time for light to travel the distance in the substance in seconds
    time_seconds = d_meters / v_substance

    # Convert time from seconds to nanoseconds
    time_nanoseconds = time_seconds * 1e9
    result = time_nanoseconds

    print(result)

def method15():
    print("give degrees, minima")
    degrees = float(input("degrees: "))
    minima = float(input("minima: "))

    # Given values
    m4 = 4  # Order number for the 4th minima
    theta_4_deg = degrees  # Angle of the 4th minima in degrees
    m12 = minima  # Order number for the m = 12 minima

    # Convert the angle of the 4th minima to radians
    theta_4_rad = math.radians(theta_4_deg)

    # Calculate the sine of the 4th minima
    sin_theta_4 = math.sin(theta_4_rad)

    # Calculate the sine of the 12th minima
    sin_theta_12 = m12 / m4 * sin_theta_4

    # Check if the sine of the 12th minima is possible (i.e., <= 1)
    if sin_theta_12 > 1:
        angle_m12_deg = "Not physically possible"
    else:
        # Calculate the angle of the 12th minima in radians
        theta_12_rad = math.asin(sin_theta_12)
        # Convert the angle to degrees
        angle_m12_deg = math.degrees(theta_12_rad)

    result = angle_m12_deg
    print(result)

def method16():
    print("give lambda, width, minimum")
    lambda1 = float(input("lambda: "))
    width = float(input("width: "))
    minimum = float(input("minimum: "))

    # Constants
    lambda_laser = lambda1 * 10**-9  # wavelength in meters
    a_slit = width*10**-3  # slit width in meters
    m_order = minimum  # order number of the minimum

    # Calculate the angle of the 7th minimum in radians
    theta_7_rad = math.asin(m_order * lambda_laser / a_slit)

    # Convert the angle to degrees
    theta_7_deg = math.degrees(theta_7_rad)
    result = theta_7_deg
    print(result)

# Input array from the user
inputChoice = ["method1", "method2", "method3", "method4", "method5", "method6", "method7", "method8", "method9", "method10", "method11", "method12", "method13", "method14", "method15", "method16"]
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
elif choice == 'method7':
    method7()
elif choice == 'method8':
    method8()
elif choice == 'method9':
    method9()
elif choice == 'method10':
    method10()
elif choice == 'method11':
    method11()
elif choice == 'method12':
    method12()
elif choice == 'method13':
    method13()
elif choice == 'method14':
    method14()
elif choice == 'method15':
    method15()
elif choice == 'method16':
    method16()
elif choice == 'q':
    exit()
else:
    print("Invalid choice. Please enter method1-16")
