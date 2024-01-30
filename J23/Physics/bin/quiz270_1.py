import math

def method1():
    print("give length, temp, length2, temp2")
    length1 = float(input("length1: "))
    temp1 = float(input("temp1: "))
    length2 = float(input("length2: "))
    temp2 = float(input("temp2: "))
    result = (length2 - length1) / (length1 * (temp2 - temp1))
    print(result)

def method2():
    print("give temp1, temp2, rod_diameter, length, conductivity")
    temp1 = float(input("temp1: "))
    temp2 = float(input("temp2: "))
    rod_diameter = float(input("rod_diameter: "))
    length = float(input("length: "))
    conductivity = float(input("conductivity: "))
    result = conductivity * math.pi * ((rod_diameter / 2) ** 2) * ((temp1 - temp2)/length) / 100
    print(result)

def method3():
    print("give var1, var2")
    var1 = float(input("var1: "))
    var2 = float(input("varr2: "))
    result = var1*var2
    print(result)

def method4():
    print("give var1, var2")
    var1 = float(input("var1: "))
    var2 = float(input("varr2: "))
    result = var1*var2
    print(result)

def method5():
    print("give var1, var2")
    var1 = float(input("var1: "))
    var2 = float(input("varr2: "))
    result = var1*var2
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
