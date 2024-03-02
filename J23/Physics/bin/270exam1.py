import math

def method1():
    print("give ice_mass, init_temp, water_temp, spec_heat, latent_heat")
    ice_mass = float(input("ice_mass: "))/1000
    init_temp = float(input("init_temp: "))
    water_temp = float(input("water_temp: "))
    spec_heat = float(input("spec_heat: "))/1000
    latent_heat = float(input("latent_heat: "))
    result = ice_mass*latent_heat + ice_mass*spec_heat*(water_temp - init_temp)
    print(result)

def method2():
    print("give rod_length, tempp_init, percent_inc, lin_coeff")
    rod_length = float(input("rod_length: "))
    temp_init = float(input("temp_init: "))
    percent_inc = float(input("percent_inc: ")) / 100
    lin_coeff = float(input("lin_coeff: ")) / 1000000
    result = percent_inc / (lin_coeff) + temp_init
    print(result)

def method3():
    print("give mass, c_Cu, init_temp, m_ice, init_temp2, c_ice, L_f")
    mass = float(input("mass: "))
    c_Cu = float(input("c_Cu: "))
    init_temp = float(input("init_temp: "))
    m_ice = float(input("m_ice: "))
    init_temp2 = float(input("init_temp2: "))
    c_ice = float(input("c_ice: "))
    L_f = float(input("L_f: "))
    Q_Cu = mass/1000*c_Cu * (init_temp - 0)
    Q_icewarm = m_ice * c_ice * abs(init_temp2)
    result = m_ice - (Q_Cu - Q_icewarm)/(L_f*1000)
    print(result)

def method4():
    print("give mass, temp_init, temp_fin, spec_heat")
    mass = float(input("mass: "))
    temp_init = float(input("temp_init: "))
    temp_fin = float(input("temp_fin: "))
    spec_heat = float(input("spec_heat: "))
    result = (mass/1000 * spec_heat * (temp_fin - (temp_init))) / 1000
    print(result)

def method5():
    print("give temp_init, gas_press, temp_final")
    temp_init = float(input("temp_init: "))
    gas_press = float(input("gas_press: "))
    temp_final = float(input("temp_final: "))
    result = gas_press * (temp_final + 273.15) / (temp_init + 273.15)
    print(result)

def method6():
    print("give init_temp, atm, volume, atm2, volume2")
    init_temp = float(input("init_temp: "))
    atm = float(input("atm: "))
    volume = float(input("volume: "))
    atm2 = float(input("atm2: "))
    volume2 = float(input("volume2: "))
    result = ((init_temp + 273.15) * atm2 * (volume2/1000) / atm / (volume/1000)) - 273.15
    print(result)

def method7():
    print("give moles, temp, mol_mass")
    moles= float(input("moles: "))
    temp = float(input("temp: "))
    mol_mass = float(input("mol_mass: "))
    result = 3/2 * (1.380649 * (10 ** -23)) * (temp + 273.15) * (10**24)
    print(result)

def method8():
    print("give pressure_atm, celcius, volume")
    pressure_atm = float(input("pressure: "))
    celcius = float(input("celcius: "))
    volume = float(input("volume: "))
    result = pressure_atm*101325*volume/(1.380649 * (10 ** -23) * (celcius + 273.15)) / (10 ** 26)
    print(result)

def method9():
    print("give init_atm, init_L, fin_atm")
    init_atm = float(input("init_atm: "))
    init_L = float(input("init_L: "))
    fin_atm = float(input("fin_atm: "))
    v_2 = (init_atm / fin_atm)**(1/1.2) * init_L
    result = -(fin_atm*v_2 - init_L*init_atm)/(1.2 - 1) * 100
    print(result)

def method10():
    print("give mass, temp, atm_init, atm_fin, mol_mass, C_p")
    mass = float(input("mass: "))
    temp = float(input("temp: "))
    atm_init = float(input("atm_init: "))
    atm_fin = float(input("atm_fin: "))
    mol_mass = float(input("mol_mass: "))
    C_p = float(input("C_p: "))
    result = mass/mol_mass * (C_p - 8.314) * math.log(atm_fin/atm_init) 
    print(result)

def method11(): 
    print("give t_h, t_c, kJ_taken, kJ_rejected, taken_hypo")
    t_h = float(input("t_h: "))
    t_c = float(input("t_c: "))
    kJ_taken = float(input("kJ_taken: "))
    kJ_rejected = float(input("kJ_rejected: "))
    taken_hypo = float(input("taken_hypo: "))
    result = kJ_taken*1000 * (1 - (t_c+273.15)/(t_h+273.15)) / 1000
    print(result)

def method12():
    print("give q, m, celcius")
    q = float(input("q: ")) * 1000
    m = float(input("m: "))
    celcius = float(input("celcius: "))
    q_1= m*334
    q_2 = q - q_1
    t1 = q_2/(4186 * m * 1000)
    t2 = t1 + 273.15
    deltaS1 = q_1/(celcius + 273.15)
    print(deltaS1)
    deltaS2 = m*4186*math.log(t2/(celcius+273.15))
    print(deltaS2)
    result = deltaS1 + deltaS2
    print(result)

def method13(): 
    print("give electrons (in 10^15)")
    result = float(input())
    result = 1
    print(result)

def method14(): 
    print("give electrons (in 10^15)")
    result = float(input())
    result = 1
    print(result)

def method15():
    print("give electrons (in 10^15)")
    result = float(input())
    result = 1
    print(result)

def method16():
    print("give electrons (in 10^15)")
    result = float(input())
    result = 1
    print(result)

# Input array from the user
inputChoice = ["method1", "method2", "method3", "method4", "method5", "method6", "method7", "method8", "method9", "method10", "method11", "method12", "method13", "method14", "method15", "method16"]
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
elif choice == 'method6':
    method6()
elif choice == 'method7':
    method7()
elif choice == 'method8':
    method8()
elif choice == 'method9':
    method9()
elif choice == 'method10':
    method10()
elif choice == 'method11':
    method11()
elif choice == 'method12':
    method12()
elif choice == 'method13':
    method13()
elif choice == 'method14':
    method14()
elif choice == 'method15':
    method15()
elif choice == 'method16':
    method16()
elif choice == 'q':
    exit()
else:
    print("Invalid choice. Please enter method1-16")
