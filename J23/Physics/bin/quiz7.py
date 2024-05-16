import math

def method1():
    print("give r_a, r_b, k, L, V")
    r_a = float(input("r_a: "))
    r_b = float(input("r_b: "))
    k = float(input("k: "))
    L = float(input("L: "))
    V = float(input("V: "))
    result = (2*math.pi*L*k*8.85*(10**-12) / (math.log(r_b/r_a))) * 0.5 * V**2 * 10**9
    print(result)

def method2():
    print("give c, voltage, percent")
    c = float(input("c: "))
    voltage = float(input("voltage: "))
    percent = float(input("percent: "))
    u = c * voltage**2 / 2
    c1 = c / ((100 + percent)/100)
    u1 = c1 * voltage**2 / 2
    result = u1 - u
    print(result)

def method3():
    print("give cap1, cap2, cap3, v")
    c1 = float(input("cap1: "))
    c2 = float(input("cap2: "))
    c3 = float(input("cap3: "))
    v = float(input("v: "))
    x = c1*v / (c1 + c2 + c3)
    result = c2 * x
    print(result)

def method4():
    print("give c, v")
    c = float(input("c: "))
    v = float(input("v: "))
    ctemp = c * c / (2*c)
    ctemp2 = ctemp + c
    result = c * ctemp2 / (c + ctemp2)
    print(result)

def method5():
    print("give v, r_a, r_b, r")
    v = float(input("v: "))
    r_a = float(input("r_a: "))
    r_b = float(input("r_b: "))
    r = float(input("r: "))
    result = 0.5 * 8.84 * (10**-12) * ( ( v / ((1/r_a/(10**-3)) - (1/r_b/(10**-3))) ) * 1/((r * (10**-3)) ** 2)) ** 2
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
