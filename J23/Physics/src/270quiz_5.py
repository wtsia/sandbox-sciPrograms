import math

def method1():
    print("give speedOfLight")
    speedOfLight = float(input("speedOfLight: "))
    result = 3.00 * 10**8 / (speedOfLight * 10**7)
    print(result)

def method2():
    print("give theta1, theta2, n_air")
    theta1 = float(input("theta1: "))
    theta2 = float(input("theta2: "))
    n_air = float(input("n_air: "))
    n2 = n_air * math.sin(degreeToRadian(theta1))/math.sin(degreeToRadian(theta2))
    theta_c = math.asin(n_air/n2)
    result = radianToDegree(theta_c)
    print(result)

def method3():
    print("give index_refraction")
    i_ref = float(input("index of refraction: "))
    r_1 = math.asin((1 / i_ref) * math.sin(degreeToRadian(30)))
    i2 = 60 - radianToDegree(r_1)
    r2 = math.asin(i_ref * math.sin(degreeToRadian(i2)))
    result = radianToDegree(r2)
    print(result)

def method4():
    print("give theta, polarization")
    theta = float(input("theta: "))
    n1 = float(input("polarization: ")) / 100
    n2 = n1* math.tan(degreeToRadian(theta))
    result = math.asin(n1 / n2 * math.sin(degreeToRadian(theta)))
    print(radianToDegree(result))

def method5():
    print("give intensity, theta1, theta2, theta3")
    intens = float(input("intensity: "))
    theta1 = float(input("theta1: "))
    theta2 = float(input("theta2: "))
    theta3 = float(input("theta3: "))
    i1 = intens/2 * math.cos(degreeToRadian(theta1))**2
    i2 = i1 * math.cos(degreeToRadian(theta2 - theta1))**2
    i3 = i2 * math.cos(degreeToRadian(theta3 - theta2))**2
    result = i3
    print(result)

def degreeToRadian(degree):
    return degree * math.pi / 180
def radianToDegree(radian):
    return radian * 180 / math.pi


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
