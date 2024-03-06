import math

def method1():
    print("give molar_mass, thermal_speed")
    molar_mass = float(input("molar_mass: "))
    thermal_speed = float(input("thermal_speed: "))
    temp1 = (molar_mass * thermal_speed * thermal_speed / 3 / 8.314) / 1000
    result = temp1 - 273.15
    print(result)

def method2():
    print("give temp1, speed, temp2")
    temp1 = float(input("temp1: "))
    speed = float(input("speed: "))
    temp2 = float(input("temp2: "))
    result = speed / math.sqrt((temp1 + 273)/(temp2 + 273))
    print(result)

def method3():
    print("give length, width, height, pressure, temp, molar_weight")
    length = float(input("length: "))
    width = float(input("width: "))
    height = float(input("height: "))
    pressure = float(input("pressure: "))
    temp = float(input("temp: "))
    molar = float(input("molar: "))
    result = 3/2 * pressure * 1.013 * length/100 * width/100 * height
    print(result)

def method4():
    print("give i, j, and k for all 3 vectors with signs")
    i1 = float(input("i1: "))
    j1 = float(input("j1: "))
    k1 = float(input("k1: "))
    i2 = float(input("i2: "))
    j2 = float(input("j2: "))
    k2 = float(input("k2: "))
    i3 = float(input("i3: "))
    j3 = float(input("j3: "))
    k3 = float(input("k3: "))
    v1 = math.sqrt(i1 ** 2 + j1 ** 2 + k1 ** 2)
    v2 = math.sqrt(i2 ** 2 + j2 ** 2 + k2 ** 2)
    v3 = math.sqrt(i3 ** 2 + j3 ** 2 + k3 ** 2)
    result = math.sqrt((v1 ** 2 + v2 ** 2 + v3 ** 2)/3)
    print(result)

def method5():
    print("give moles, temp, mass")
    moles = float(input("moles: "))
    temp = float(input("temp: "))
    mass = float(input("mass: "))
    r = 8.314/mass/1000
    result = 3/2 * (1.38064852) * (temp + 273.15) * 10
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
