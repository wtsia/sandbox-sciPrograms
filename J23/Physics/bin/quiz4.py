import math

def method1():
    print("give radiusA, surface_density, radiusB, outRadius")
    radiusA = float(input("radiusA: "))
    surface_density = float(input("surface_density: "))
    radiusB = float(input("radiusB: "))
    outRadius = float(input("outRadius: "))
    result = -surface_density * (radiusA / 100) ** 2 / (radiusB / 100) ** 2
    print(result)

def method2():
    print("give radiusA, radiusB, lambda1, lambda2, point")
    radiusA = float(input("radiusA: "))
    radiusB = float(input("radiusB: "))
    lambda1 = float(input("lambda1: "))
    lambda2 = float(input("lambda2: "))
    point = float(input("point: "))
    result = 2 * 9 * -lambda2 / point * 1000
    print(result)

def method3():
    print("give outerRad, innerRad, netDensity, chgDensity")
    outerRad = float(input("outerRad: "))
    innerRad = float(input("innerRad: "))
    netDensity = float(input("netDensity: "))
    chgDensity = float(input("chgDensity: "))
    tempResult = abs(chgDensity * 4 * math.pi * (innerRad / 100) ** 2)
    result = netDensity * 4 * math.pi * (outerRad / 100) ** 2 - tempResult
    print(result)

def method4():
    print("give valueE, radius")
    valueE = float(input("valueE: "))
    radius = float(input("radius: "))
    result = valueE / (radius ** 3)
    print(result)

def method5():
    print("give lambda1, lambda2, separation")
    lambda1 = float(input("lambda1: "))
    lambda2 = float(input("lambda2: "))
    separation = float(input("separation: "))
    separation = separation / 200
    tmp1 = 2 * lambda1 * 9 / separation
    tmp2 = 2 * lambda2 * 9 / separation
    print(tmp1 - tmp2)


# Input array from the user
inputChoice = ["chg_density", "elec_field", "chgQb", "elecField", "mag_elecField"]
formatted_string = ", ".join([str(element) for element in inputChoice])

choice = "y"

# Check the user's choice and call the corresponding method
while (choice != "q"):
    print(f"Enter a method to execute ({formatted_string})")
    choice = input("choice: ")
    if choice == 'chg_density':
        method1()
        print("\n")
    elif choice == 'elec_field':
        method2()
        print("\n")
    elif choice == 'chgQb':
        method3()
        print("\n")
    elif choice == 'elecField':
        method4()
        print("\n")
    elif choice == 'mag_elecField':
        method5()
        print("\n")
    elif choice == 'q':
        exit()
    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, and 5.")
        print("\n")
