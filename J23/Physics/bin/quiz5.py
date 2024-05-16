import math

def method1():
    print("give v0 and vf")
    var1 = float(input("v0: "))
    var2 = float(input("vf: "))
    result = ( var2**2 - var1**2 ) * 1.67 / (2 * 1.6) / 10
    print(result)

def method2():
    print("electron moving in opp direction to elec field has pot energy decrease and electric pot increase")

def method3():
    print("give q_a, q_b, r_0, r_f")
    q_a = float(input("q_a: "))
    q_b = float(input("q_b: "))
    r_0 = float(input("r_0: "))
    r_f = float(input("r_f: "))
    result = 9 * q_a * q_b * (1 / r_0 - 1 / r_f) / 10
    print(result)

def method4():
    print("give q1, m1, r0, d")
    q1 = float(input("q1: "))
    m1 = float(input("m1: "))
    r0 = float(input("r0: "))
    d = float(input("d: "))
    leftSide = (9 * q1 * -1.6 / r0) / 10
    rightSide = (9 * q1 * -1.6 / ( r0 + d/100)) / 10
    result = (leftSide - rightSide) * 2 / 9.11 * 100 * 10 ** 11
    print(math.sqrt(result)/1000)

def method5():
    print("give var1, var2")
    var1 = float(input("var1: "))
    var2 = float(input("varr2: "))
    force_temp = var1*var2
    print(result)


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
