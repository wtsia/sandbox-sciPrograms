import math

def method1():
    print("give radius, charge, point")
    radius = float(input("radius: "))
    charge = float(input("charge: "))
    point = float(input("point: "))
    sigma = charge/(math.pi*(radius/100)**2)
    result = sigma / 2 / 8.85 
    result = result * (1 - (point/100/math.sqrt((radius/100)**2 + (point/100)**2)))
    print(abs(result))

def method2():
    print("give dipole, orient, elecField")
    dipole = float(input("dipole: "))
    orient = float(input("orient: "))
    elecField = float(input("elecField: "))
    orientRad = math.radians(orient)
    piRad = math.radians(180)
    result = dipole * elecField * (math.cos(orientRad) - math.cos(piRad))
    print(result)

def method3():
    print("give charge, radius")
    charge = float(input("charge: "))
    radius = float(input("radius: "))
    radian90 = math.radians(90)
    result = 4 * 9 * charge / math.pi / (radius/100) ** 2 * math.sin(radian90/2) 
    print(result)

def method4():
    print("give chargeLocation1, chargeDensity1,  chargeLocation2, chargeDensity2")
    var12 = float(input("chargeLocation1: "))
    var11 = float(input("chargeDensity1: "))
    var22 = float(input("chargeLocation2: "))
    var21 = float(input("chargeDensity2: "))
    result = 2 * 9 / abs(var12 / 100) * (abs(var11) + abs(var21)) / 1000
    print(result)

def method5():
    print("give charge1, x-axis0, x-axis1, charge2, y-axis0, y-axis1, point-x, point-y")
    charge1 = float(input("charge1: "))
    x_axis0 = float(input("x_axis0: "))
    x_axis1 = float(input("x_axis1: "))
    charge2 = float(input("charge2: "))
    y_axis0 = float(input("y_axis0: "))
    y_axis1 = float(input("y_axis1: "))
    point_x = float(input("point_x: "))
    point_y = float(input("point_y: "))

    i_hat = 9 * charge1 / point_x / math.sqrt(point_x ** 2 + point_x ** 2)
    j_hat = 9 * charge2 / point_y / math.sqrt(point_y ** 2 + point_y ** 2)

    result = math.sqrt(i_hat ** 2 + j_hat ** 2)
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
    print("Invalid choice. Please enter method1, method2, method3, method4, and method5.")
