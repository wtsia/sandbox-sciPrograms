import math

def method1():
    print("give length, omega, bHat")
    length = float(input("length: "))
    omega = float(input("omega: "))
    bHat = float(input("bHat: "))
    result = 0.5*bHat*omega* (length*0.001) ** 2 * 100
    print(result)

def method2():
    print("give crossSection, turns, (with sign!) coefficientT1, coefficientT2, and time")
    crossSection = float(input("crossSection: "))
    turns = float(input("turns: "))
    coefficientT1 = float(input("coefficientT1: "))
    coefficientT2 = float(input("coefficientT2: "))
    time = float(input("time: "))
    result = -turns* (coefficientT1 + time*coefficientT2*2) * (crossSection * (10 ** -4))
    print(result)

def method3():
    print("give R, N, A, rotateRate, B")
    resist = float(input("R: "))
    nNum = float(input("N: "))
    area = float(input("A: "))
    rotateRate = float(input("rotateRate: "))
    magField = float(input("B: "))
    result = nNum * area * magField * rotateRate * 2 * math.pi / resist
    print(result)

def method4():
    print("Give length, resistance, strength, speed")
    length = float(input("length: "))
    resistance = float(input("resistance: "))
    strength = float(input("strength: "))
    speed = float(input("speed: "))
    result = (length * strength * speed * (10 ** -2)) ** 2 / resistance
    print(result)

def method5():
    print("give turns, magFlux, coilRadius, angle, time")
    turns = float(input("turns: "))
    magFlux = float(input("magFlux: "))
    coilRadius = float(input("coilRadius: "))
    angle = float(input("angle: "))
    time = float(input("time: "))
    result = -turns * (magFlux * (10 ** -6)) * math.pi * ((coilRadius * 10 ** -2) ** 2) * (math.cos(angle * math.pi / 180) - math.cos(0)) / (time * (10 ** -3))
    print(result * 1000)


# Input array from the user
inputChoice = ["magnitudeEMF", "magEMF2", "inducedCurr", "magBulb", "avgEMF"]
formatted_string = ", ".join([str(element) for element in inputChoice])

# Printing the formatted string
print(f"Enter a method to execute ({formatted_string})")
choice = input("choice: ")

# Check the user's choice and call the corresponding method
if choice == 'magnitudeEMF':
    method1()
elif choice == 'magEMF2':
    method2()
elif choice == 'inducedCurr':
    method3()
elif choice == 'magBulb':
    method4()
elif choice == 'avgEMF':
    method5()
elif choice == 'q':
    exit()
else:
    print("Invalid choice. Please enter 1, 2, 3, 4, and 5.")
