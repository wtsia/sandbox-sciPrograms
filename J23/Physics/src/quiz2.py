import math

def method1():
    print("give field, separation, init_velocity")
    field1 = float(input("field: "))
    separation1 = float(input("separation: "))
    init_velocity = float(input("init_vel: "))
    force_temp = field1*separation1*2*1.6/9.11
    print(force_temp)
    v_num = (init_velocity**2 - force_temp)*10**12
    print(math.sqrt(v_num)/(10**6))

def method2():
    print("give elec_field_len, dist_plate, horizSpeed")
    elec_field_len2 = float(input("elec_field_len: "))
    dist_plate2 = float(input("dist_plate: "))
    horizSpeed2 = float(input("horizSpeed: "))
    time_taken = elec_field_len2/horizSpeed2
    print(dist_plate2*1.67/(1.6*time_taken**2)*10)

def method3():
    print("negative x direction")

def method4():
    print("magnitude!!!")

def method5():
    print("give charge1, charge2, distance")
    charge15 = float(input("charge15: "))
    charge25 = float(input("charge25: "))
    distance5 = float(input("distance5: "))
    result5 = charge15 * 9 * 10**3 / (distance5/2)**2 + charge25*9 / (distance5/2)**2
    print(result5)

# Input from the user
choice = input("Enter a method to execute (elec_velocity, mag_maxField, direcXField, halfway_btwn, mag_btwn_charge): ")

# Check the user's choice and call the corresponding method
if choice == 'elec_velocity':
    method1()
elif choice == 'mag_maxField':
    method2()
elif choice == 'direcXField':
    method3()
elif choice == 'halfway_btwn':
    method4()
elif choice == 'mag_btwn_charge': ## TODOOOO
    method5()
elif choice == 'q':
    exit()
else:
    print("Invalid choice. Please enter 1, 2, or 3.")
