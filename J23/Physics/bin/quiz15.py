import math

def method1():
    print("give dist, wavelength, intensity, rectArea, and timeInterval")
    dist = float(input("dist: "))
    wavelength = float(input("wavelength: "))
    intensity = float(input("intensity: "))
    rectArea = float(input("rectArea: "))
    timeInterval = float(input("timeInterval: "))
    result = 2 * intensity / 3 * rectArea * timeInterval / (math.pow(10, 5))
    print(result)

def method2():
    print("give power, wavelength, distance")
    power = float(input("power: "))
    wavelength = float(input("wavelength: "))
    distance = float(input("distance: "))
    result = power / (4 * math.pi * (distance) ** 2) / 300
    print(result)

def method3():
    print("give beam")
    beam = float(input("beam: "))
    result = math.sqrt(2 * beam * 3 * 4 * math.pi * 10)
    print(result)

def method4():
    print("give energyFlow, rect1, rect2, minutes")
    energyFlow = float(input("energyFlow: "))
    rect1 = float(input("rect1: "))
    rect2 = float(input("rect2: "))
    minutes = float(input("minutes: "))
    result = energyFlow * rect1 * rect2 * minutes * 60 / 10000
    print(result)

def method5():
    print("give operatingMHz")
    operatingMHz = float(input("operating Mhz: "))
    result = 3*10000/operatingMHz
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
