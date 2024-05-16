import math

def method1():
    print("give electrons (in 10^15)")
    electron = float(input("electron: "))
    result = electron*1.602*100
    print(result)

def method2():
    print("give field, separation, init_velocity")
    field1 = float(input("field: "))
    separation1 = float(input("separation: "))
    init_velocity = float(input("init_vel: "))
    force_temp = field1*separation1*2*1.6/9.11
    v_num = (init_velocity**2 - force_temp)*10**12
    print(math.sqrt(v_num)/(10**6))

def method3():
    print("give charge, radius")
    charge = float(input("charge: "))
    radius = float(input("radius: "))
    radian90 = math.radians(90)
    result = 4 * 9 * charge / math.pi / (radius/100) ** 2 * math.sin(radian90/2) 
    print(result)

def method4():
    print("give elec_field_len, dist_plate, horizSpeed")
    elec_field_len2 = float(input("elec_field_len: "))
    dist_plate2 = float(input("dist_plate: "))
    horizSpeed2 = float(input("horizSpeed: "))
    time_taken = elec_field_len2/horizSpeed2
    print(dist_plate2*1.67/(1.6*time_taken**2)*10)

def method5():
    print("give radius, charge, point")
    radius = float(input("radius: "))
    charge = float(input("charge: "))
    point = float(input("point: "))
    sigma = charge/(math.pi*(radius/100)**2)
    result = sigma / 2 / 8.85 
    result = result * (1 - (point/100/math.sqrt((radius/100)**2 + (point/100)**2)))
    print(abs(result))

def method6():
    print("give dipole, orient, elecField")
    dipole = float(input("dipole: "))
    orient = float(input("orient: "))
    elecField = float(input("elecField: "))
    orientRad = math.radians(orient)
    piRad = math.radians(180)
    result = dipole * elecField * (math.cos(orientRad) - math.cos(piRad))
    print(result)

def method7():
    print("give mass, thread, field_mag")
    mass = float(input("mass: "))
    thread = float(input("thread: "))
    field_mag = float(input("field_mag: "))
    result = mass*9.8/field_mag/math.tan(math.radians(60))*1000
    print(result)

def method8():
    print("give id_chg")
    id_chg = float(input("id_chg: "))
    f_1 = round(9*id_chg*id_chg/1.5/1.5/1000, 3)
    f_3 = round(9*id_chg*id_chg/(2*1.5*1.5)/1000, 3)
    f_tmp = f_3*math.cos(math.radians(45))
    f_fin = round(f_1 + f_tmp, 3)
    result = math.sqrt(2*f_fin*f_fin)*1000
    print(round(result, 2))

def method9():
    print("give charge1, dist, charge2, degree")
    charge1 = float(input("charge1: "))
    dist = float(input("dist: "))
    charge2 = float(input("charge2: "))
    degree = float(input("degree: "))
    result = 9 * charge1 * charge2 / (dist * dist) * 10;
    print(result)

def method10():
    print("give mass, mag (+-), vert_cep")
    mass = float(input("mass: "))
    mag = float(input("mag: "))
    vert_cep = float(input("vert_cep: "))/100
    result = (9*mag*mag/vert_cep/vert_cep/1000) - (mass*9.8/1000)
    print(round(result, 2))

def method11(): # QUIZ 4.3
    print("give outerRad, innerRad, netDensity, chgDensity")
    outerRad = float(input("outerRad: "))
    innerRad = float(input("innerRad: "))
    netDensity = float(input("netDensity: "))
    chgDensity = float(input("chgDensity: "))
    tempResult = abs(chgDensity * 4 * math.pi * (innerRad / 100) ** 2)
    result = netDensity * 4 * math.pi * (outerRad / 100) ** 2 - tempResult
    print(result)

def method12():
    print("ITS PHI_0!")
    #r_0 = float(input("var1: "))
    #phi_0 = float(input("varr2: "))
    #bigR = float(input("varr2: "))
    #result = phi_0
    #print(result)

def method13(): # QUIZ 4.5
    print("give lambda1, lambda2, separation")
    lambda1 = float(input("lambda1: "))
    lambda2 = float(input("lambda2: "))
    separation = float(input("separation: "))
    separation = separation / 200
    tmp1 = 2 * lambda1 * 9 / separation
    tmp2 = 2 * lambda2 * 9 / separation
    print(tmp1 - tmp2)

def method14(): # QUIZ 4.2
    print("give radiusA, radiusB, lambda1, lambda2, point")
    radiusA = float(input("radiusA: "))
    radiusB = float(input("radiusB: "))
    lambda1 = float(input("lambda1: "))
    lambda2 = float(input("lambda2: "))
    point = float(input("point: "))
    result = 2 * 9 * -lambda2 / point * 1000
    print(result)

def method15():
    print("give q1, q2, a2, b2, dist")
    q1 = float(input("q1: "))
    q2 = float(input("q2: "))
    a2 = float(input("a2: "))
    b2 = float(input("b2: "))
    dist = float(input("dist: "))
    q = q1 + q2 * (dist ** 3 - a2 ** 3)/(b2 ** 3 - a2 ** 3)
    result = 9*abs(q)/(dist/100*dist/100)
    print(result)

def method16():
    print("give q_a, dist")
    q_a = float(input("q_a: "))
    dist = float(input("dist: "))
    tmp1 = 4 * math.pi * (dist * dist) / 100
    result = q_a * 1000 / (tmp1 * 8.854) * 100
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
