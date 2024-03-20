import math

def method1():
    print("give N, d, l, and B")
    var1 = float(input("N: "))
    var2 = float(input("d: "))
    var3 = float(input("l: "))
    var4 = float(input("B: "))
    result = var4 / 1000 * var3 / 100 / (4*math.pi * var1) * 10**7
    print(result)

def method2():
    print("give curr, arc_radius")
    curr = float(input("curr: "))
    arc_radius = float(input("arc_radius: "))
    result = 4*math.pi * curr / (8 * arc_radius/100) / 10
    print(result)

def method3():
    print("give curr, arc_rad, yaxis")
    curr = float(input("curr: "))
    arc_rad = float(input("arc_rad: "))
    yaxis = float(input("yaxis: "))
    result = 100 * 4*math.pi * curr * (arc_rad/100)**2 / 2 / ((yaxis/100)**2 + (arc_rad/100)**2)**(3/2)
    print(result)

def method4():
    print("give d, i1, i2 i3")
    d = float(input("d: "))
    i1 = float(input("i1: "))
    i2 = float(input("i2: "))
    i3 = float(input("i3: "))
    d = d/100
    b1 = 4 * 10 ** -7 * i1 / (d)
    b2 = 4 * 10 ** -7 * i2 / (d)
    b3 = 4 * 10 ** -7 * i3 / (d * 3)
    result =  - b1 + b2 - b3
    print(math.fabs(result))

def method5():
    print("give a, n, i, b, theta")
    a = float(input("a: "))
    n = float(input("n: "))
    i = float(input("i: "))
    b = float(input("b: "))
    theta = float(input("theta: "))
    result = n * b * i * a * math.cos((90 - theta) * math.pi / 180) * -1
    print(result / 10000)


# Input array from the user
inputChoice = ["1", "2", "3", "4", "5"]
formatted_string = ", ".join([str(element) for element in inputChoice])

# Printing the formatted string
print(f"Enter a method to execute ({formatted_string})")
choice = input("choice: ")

# Check the user's choice and call the corresponding method
if choice == '1':
    method1()
elif choice == '2':
    method2()
elif choice == '3':
    method3()
elif choice == '4':
    method4()
elif choice == '5':
    method5()
elif choice == 'q':
    exit()
else:
    print("Invalid choice. Please enter 1, 2, 3, 4, and 5.")
