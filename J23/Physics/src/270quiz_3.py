import math

def method1():
    print("give moles, temperature")
    var1 = float(input("moles: "))
    var2 = float(input("temperature: "))
    result = var1 * 5 * (var2 + 273.5) * 8.314 / 2 / 1000
    print(result)

def method2():
    print("give moles, volume1, volume2, work_done (ANSWER)")
    var1 = float(input("moles: "))
    var2 = float(input("volume1: "))
    var3 = float(input("volume2: "))
    var4 = float(input("work_done: "))
    result = var4
    print(result)

def method3():
    print("give moles, atm, pressure_vol1, pressure_vol2, cooling_pressure, final_vol, heating_vol") 
    var1 = float(input("moles: "))
    var2 = float(input("atm: "))
    var3 = float(input("pressure_vol1: "))
    var4 = float(input("pressure_vol2: "))
    var5 = float(input("cooling_pressure: "))
    var6 = float(input("final_vol: "))
    var6 = float(input("heating_vol: "))
    atmVAR = 1.013 * (10 ** 5)
    w1 = var1 * atmVAR * (pressure_vol2 - pressure_vol1)
    w2 = 0
    w3 = final_vol * atmVAR * (pressure_vol1 - pressure_vol2) 
    w4 = 0
    result = w1 + w2 + w3 + w4
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
