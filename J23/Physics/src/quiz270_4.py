import math

def method1():
    print("give t_h, t_c, q_h, q_c")
    t_h = float(input("t_h: "))
    t_c = float(input("t_c: "))
    q_h = float(input("q_h: "))
    q_c = float(input("q_c: "))
    result = (abs(q_h) - abs(q_c)) / q_h
    print("As percent:", result*100)

def method2():
    print("give mass, init_temp, pressure_0, pressure_1, mol_mass, const_press")
    mass = float(input("mass: "))
    init_temp = float(input("init_temp: "))
    pressure_0 = float(input("pressure_0: "))
    pressure_1 = float(input("pressure_1: "))
    mol_mass = float(input("mol_mass: "))
    const_press = float(input("const_press: "))
    t_f = (init_temp + 273) * (pressure_1 / pressure_0)
    n = mass/mol_mass
    result = n * const_press * math.log(t_f / (init_temp + 273)) + n * 8.3 * math.log(pressure_0 / pressure_1)
    print(result)

def method3():
    print("give t_h, t_c, take_en, reject_en, init_taking")
    t_h = float(input("t_h: "))
    t_c = float(input("t_c: "))
    take_en = float(input("take_en: "))
    reject_en = float(input("reject_en: "))
    init_taking = float(input("init_taking: "))
    result = take_en * (1 - (t_c + 273)/(t_h + 273))
    print(result)

def method4():
    print("give q_heat, mass, temp_init")
    q_heat = float(input("q_heat: "))
    mass = float(input("mass: "))
    temp_init = float(input("temp_init: "))
    q = mass * 334
    deltaS1 = q / (temp_init + 273)
    t =  (q_heat*1000 - q)/(mass / 1000)/4186
    deltaS2 = (mass / 1000) * (4186) * math.log((t + 273) / (temp_init + 273))
    result = deltaS1 + deltaS2
    print(result)

def method5():
    print("give res_temp1, res_temp2, heat")
    res_temp1 = float(input("res_temp1: "))
    res_temp2 = float(input("res_temp21: "))
    heat = float(input("heat: "))
    deltaS0 = heat * 1000 / (res_temp1 + 273) * -1
    deltaS1 = heat * 1000 / (res_temp2 + 273) * -1
    result = (deltaS1 - deltaS0) * -1
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
