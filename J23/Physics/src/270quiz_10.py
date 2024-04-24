import math
from math import cos, sin, pi, radians
from sympy import symbols, Eq, solve

c = 1

def method1():
    print("give proton_speed")
    v = float(input("proton speed: "))

    # Given values
    c = 1  # speed of light in units of c (normalized to 1)
    v = v * c  # speed of proton in units of c
    m0 = 938.272  # rest mass of proton in MeV/c^2

    # Calculating the Lorentz factor gamma
    gamma = 1 / ((1 - v**2 / c**2)**0.5)

    # Calculating the total energy E in MeV
    E = gamma * m0

    result = E
    print(result)

def method2():
    print("give total_energy_scalar")
    scalar = float(input("total_energy_scalar: "))


    # Defining symbols
    p = symbols('p')

    # Given rest mass energy in MeV
    m0c2 = 938.272  # MeV

    # Total energy
    E = scalar * m0c2  # 2 times rest mass energy

    # Equation to solve: E^2 = (pc)^2 + (m0c2)^2
    equation = Eq(E**2, p**2 + m0c2**2)

    # Solve for p (momentum)
    momentum_p = solve(equation, p)

    result = momentum_p
    print(result)

def method3():
    print("give speed_east, speed_north, time_north")
    u = float(input("speed_east: "))
    v = float(input("speed_north: "))
    d = float(input("time_north: "))

    # Re-evaluating the calculation using the simplified version of the formula for perpendicular velocities

    # Using the correct expression to calculate the relative speed (no denominator)
    relative_speed_simple = ((u**2 + v**2 - (u*v/c)**2)**0.5)

    print(relative_speed_simple)

def method4():
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

def method5():
    print("give A_speed, B_speed")
    A_speed = float(input("A_speed: "))
    B_speed = float(input("B_speed: "))

    # Given values
    u_A = A_speed  # velocity of object A with respect to Earth
    v_B_A = B_speed*-1  # velocity of object B with respect to object A (negative for leftward)

    # Relative velocity u' calculation using the formula for velocities in opposite directions
    u_prime_earth = (u_A + v_B_A) / (1 + u_A * v_B_A / c**2)

    result = u_prime_earth
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
