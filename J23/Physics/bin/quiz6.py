import math

def method1():
    print("give dist, strength, energy")
    distm = float(input("dist: "))
    strength = float(input("strength: "))
    energy = float(input("energy: "))
    result = energy/strength*1000
    print(result)

def method2():
    print("give radius, charge, p_a, p_b (in cm)")
    radius = float(input("radius: "))
    charge = float(input("charge: "))
    p_a = float(input("p_a: "))
    p_b = float(input("p_b: "))
    result = 9*charge*(1/math.sqrt(radius**2 + p_b**2) - 1/math.sqrt(radius**2 + p_a**2))*100
    print(result)

def method3():
    print("The electric potential is a non zero constant everywhere inside the sphere")

def method4():
    print("give q, m, v_0, lambda, and r_0")
    q = float(input("q: "))
    m = float(input("m: "))
    v_0 = float(input("v_0: "))
    lambda0 = float(input("lambda0: "))
    r_0 = float(input("r_0: "))
    result = r_0 * math.e**(-1 * m * v_0**2 * 2*math.pi * 8.85/(2 * q * lambda0) / 1000)
    print(result)

def method5():
    print("give strength, dist")
    strength = float(input("strength: "))
    dist = float(input("dist: "))
    result = strength*dist*1000
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
