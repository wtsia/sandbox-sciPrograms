import math

def method1():
    print("give mass, threadLength, magnitude, degree")
    mass = float(input("mass: "))
    threadLength = float(input("threadLength: "))
    magnitude = float(input("magnitude: "))
    degree = float(input("degree: "))
    result = mass * 9.8 / (magnitude * math.tan(degree * math.pi / 180)) * 1000
    print(result)
    print("")

def method2():
    print("give masses, q1, q2, separation")
    masses = float(input("masses: "))
    q1 = float(input("q1: "))
    q2 = abs(float(input("q2: ")))
    separation = float(input("separation: "))
    result = 9 * q1 * q2 / 1000 / ((separation / 100) ** 2) - (masses / 1000 * 9.8)
    print(result)
    print("")

def method3():
    print("give charge, radius")
    charge = float(input("charge: "))
    radius = float(input("radius: "))
    radian90 = math.radians(90)
    result = 4 * 9 * charge / math.pi / (radius/100) ** 2 * math.sin(radian90/2) 
    print(result)
    print("")

def method4():
    print("give elec_field_len, dist_plate, horizSpeed")
    elec_field_len2 = float(input("elec_field_len: "))
    dist_plate2 = float(input("dist_plate: "))
    horizSpeed2 = float(input("horizSpeed: "))
    time_taken = elec_field_len2/horizSpeed2
    print(dist_plate2*1.67/(1.6*time_taken**2)*10)
    print("")


def method5():
    print("give dipole, orient, elecField")
    dipole = float(input("dipole: "))
    orient = float(input("orient: "))
    elecField = float(input("elecField: "))
    orientRad = math.radians(orient)
    piRad = math.radians(180)
    result = dipole * elecField * (math.cos(orientRad) - math.cos(piRad))
    print(result)
    print("")

def method6():
    print("give radiusA, surface_density, radiusB, outRadius")
    radiusA = float(input("radiusA: "))
    surface_density = float(input("surface_density: "))
    radiusB = float(input("radiusB: "))
    outRadius = float(input("outRadius: "))
    result = -surface_density * (radiusA / 100) ** 2 / (radiusB / 100) ** 2
    print(result)
    print("")

def method7():
    print("give radiusA, radiusB, lambda1, lambda2, point")
    radiusA = float(input("radiusA: "))
    radiusB = float(input("radiusB: "))
    lambda1 = float(input("lambda1: "))
    lambda2 = float(input("lambda2: "))
    point = float(input("point: "))
    result = 2 * 9 * -lambda2 / point * 1000
    print(result)
    print("")

def method8():
    print("give v0 and vf")
    var1 = float(input("v0: "))
    var2 = float(input("vf: "))
    result = ( var2**2 - var1**2 ) * 1.67 / (2 * 1.6) / 10
    print(result)
    print("")

def method9():
    print("give q, m, v_0, lambda, and r_0")
    q = float(input("q: "))
    m = float(input("m: "))
    v_0 = float(input("v_0: "))
    lambda0 = float(input("lambda0: "))
    r_0 = float(input("r_0: "))
    result = r_0 * math.e**(-1 * m * v_0**2 * 2*math.pi * 8.85/(2 * q * lambda0) / 1000)
    print(result)
    print("")

def method10():
    print("give cap1, cap2, cap3, v")
    c1 = float(input("cap1: "))
    c2 = float(input("cap2: "))
    c3 = float(input("cap3: "))
    v = float(input("v: "))
    x = c1*v / (c1 + c2 + c3)
    result = c2 * x
    print(result)

def method11():
    print("give c, voltage, percent")
    c = float(input("c: "))
    voltage = float(input("voltage: "))
    percent = float(input("percent: "))
    u = c * voltage**2 / 2
    c1 = c / ((100 + percent)/100)
    u1 = c1 * voltage**2 / 2
    result = u1 - u
    print(result)
    print("")

def method12():
    print("give v, r_a, r_b, r")
    v = float(input("v: "))
    r_a = float(input("r_a: "))
    r_b = float(input("r_b: "))
    r = float(input("r: "))
    result = 0.5 * 8.84 * (10**-12) * ( ( v / ((1/r_a/(10**-3)) - (1/r_b/(10**-3))) ) * 1/((r * (10**-3)) ** 2)) ** 2
    print(result)
    print("")

def method13(): 
    print("give mass, massDensity, diameter, current, freeElectron")
    mass = float(input("mass: "))
    massDensity = float(input("massDensity: "))
    diameter = float(input("diameter: "))
    current = float(input("current: "))
    freeElectron = float(input("freeElectron: "))
    nCurve = freeElectron * 6.02 / mass * massDensity
    bigA = math.pi / 4 * (diameter ** 2)
    result = current / (nCurve * bigA * 1.6) * 100000
    print(result)
    print("")

def method14(): # QUIZ 4.2
    print("give radiusA, radiusB, lambda1, lambda2, point")
    radiusA = float(input("radiusA: "))
    radiusB = float(input("radiusB: "))
    lambda1 = float(input("lambda1: "))
    lambda2 = float(input("lambda2: "))
    point = float(input("point: "))
    result = 2 * 9 * -lambda2 / point * 1000
    print(result)
    print("")

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
    print("")

def method16():
    print("give q_a, dist")
    q_a = float(input("q_a: "))
    dist = float(input("dist: "))
    tmp1 = 4 * math.pi * (dist * dist) / 100
    result = q_a * 1000 / (tmp1 * 8.854) * 100
    print(result)
    print("")


def method17():
    print("give electrons (in 10^15)")
    electron = float(input("electron: "))
    result = electron*1.602*100
    print(result)
    print("")

def method18():
    print("give field, separation, init_velocity")
    field1 = float(input("field: "))
    separation1 = float(input("separation: "))
    init_velocity = float(input("init_vel: "))
    force_temp = field1*separation1*2*1.6/9.11
    v_num = (init_velocity**2 - force_temp)*10**12
    print(math.sqrt(v_num)/(10**6))
    print("")

def method19():
    print("give charge, radius")
    charge = float(input("charge: "))
    radius = float(input("radius: "))
    radian90 = math.radians(90)
    result = 4 * 9 * charge / math.pi / (radius/100) ** 2 * math.sin(radian90/2) 
    print(result)
    print("")

def method20():
    print("give elec_field_len, dist_plate, horizSpeed")
    elec_field_len2 = float(input("elec_field_len: "))
    dist_plate2 = float(input("dist_plate: "))
    horizSpeed2 = float(input("horizSpeed: "))
    time_taken = elec_field_len2/horizSpeed2
    print(dist_plate2*1.67/(1.6*time_taken**2)*10)
    print("")

def method21():
    print("give radius, charge, point")
    radius = float(input("radius: "))
    charge = float(input("charge: "))
    point = float(input("point: "))
    sigma = charge/(math.pi*(radius/100)**2)
    result = sigma / 2 / 8.85 
    result = result * (1 - (point/100/math.sqrt((radius/100)**2 + (point/100)**2)))
    print(abs(result))
    print("")

def method22():
    print("give dipole, orient, elecField")
    dipole = float(input("dipole: "))
    orient = float(input("orient: "))
    elecField = float(input("elecField: "))
    orientRad = math.radians(orient)
    piRad = math.radians(180)
    result = dipole * elecField * (math.cos(orientRad) - math.cos(piRad))
    print(result)
    print("")

def method23():
    print("give mass, thread, field_mag")
    mass = float(input("mass: "))
    thread = float(input("thread: "))
    field_mag = float(input("field_mag: "))
    result = mass*9.8/field_mag/math.tan(math.radians(60))*1000
    print(result)
    print("")

def method24():
    print("give id_chg")
    id_chg = float(input("id_chg: "))
    f_1 = round(9*id_chg*id_chg/1.5/1.5/1000, 3)
    f_3 = round(9*id_chg*id_chg/(2*1.5*1.5)/1000, 3)
    f_tmp = f_3*math.cos(math.radians(45))
    f_fin = round(f_1 + f_tmp, 3)
    result = math.sqrt(2*f_fin*f_fin)*1000
    print(round(result, 2))
    print("")

def method25():
    print("give charge1, dist, charge2, degree")
    charge1 = float(input("charge1: "))
    dist = float(input("dist: "))
    charge2 = float(input("charge2: "))
    degree = float(input("degree: "))
    result = 9 * charge1 * charge2 / (dist * dist) * 10;
    print(result)
    print("")

def method26():
    print("give mass, mag (+-), vert_cep")
    mass = float(input("mass: "))
    mag = float(input("mag: "))
    vert_cep = float(input("vert_cep: "))/100
    result = (9*mag*mag/vert_cep/vert_cep/1000) - (mass*9.8/1000)
    print(round(result, 2))
    print("")

def method27(): # QUIZ 4.3
    print("give outerRad, innerRad, netDensity, chgDensity")
    outerRad = float(input("outerRad: "))
    innerRad = float(input("innerRad: "))
    netDensity = float(input("netDensity: "))
    chgDensity = float(input("chgDensity: "))
    tempResult = abs(chgDensity * 4 * math.pi * (innerRad / 100) ** 2)
    result = netDensity * 4 * math.pi * (outerRad / 100) ** 2 - tempResult
    print(result)
    print("")

def method28():
    print("ITS PHI_0!")
    #r_0 = float(input("var1: "))
    #phi_0 = float(input("varr2: "))
    #bigR = float(input("varr2: "))
    #result = phi_0
    #print(result)
    print("")

def method29(): # QUIZ 4.5
    print("give lambda1, lambda2, separation")
    lambda1 = float(input("lambda1: "))
    lambda2 = float(input("lambda2: "))
    separation = float(input("separation: "))
    separation = separation / 200
    tmp1 = 2 * lambda1 * 9 / separation
    tmp2 = 2 * lambda2 * 9 / separation
    print(tmp1 - tmp2)
    print("")

def method30(): # QUIZ 4.2
    print("give radiusA, radiusB, lambda1, lambda2, point")
    radiusA = float(input("radiusA: "))
    radiusB = float(input("radiusB: "))
    lambda1 = float(input("lambda1: "))
    lambda2 = float(input("lambda2: "))
    point = float(input("point: "))
    result = 2 * 9 * -lambda2 / point * 1000
    print(result)
    print("")

def method31():
    print("give q1, q2, a2, b2, dist")
    q1 = float(input("q1: "))
    q2 = float(input("q2: "))
    a2 = float(input("a2: "))
    b2 = float(input("b2: "))
    dist = float(input("dist: "))
    q = q1 + q2 * (dist ** 3 - a2 ** 3)/(b2 ** 3 - a2 ** 3)
    result = 9*abs(q)/(dist/100*dist/100)
    print(result)
    print("")

def method32():
    print("give q_a, dist")
    q_a = float(input("q_a: "))
    dist = float(input("dist: "))
    tmp1 = 4 * math.pi * (dist * dist) / 100
    result = q_a * 1000 / (tmp1 * 8.854) * 100
    print(result)
    print("")



def default():
    print("Invalid choice")

def generate_switch_dict():
    switch_dict = {}
    for i in range(1, 32):
        switch_dict[i] = globals().get(f"method{i}", default)
    return switch_dict

def switch_case(choice):
    switch_dict = generate_switch_dict()

    if choice == 0:
        print("Exiting the program. Goodbye!")
        exit()

    # Use get() method to handle default case
    selected_method = switch_dict.get(choice, default)
    selected_method()

def main():
    while True:
        print("Select a method (1-32) or enter 0 to quit: ")
        try:
            choice = int(input())
            if 0 <= choice <= 32:
                switch_case(choice)
            else:
                print("Invalid choice. Please enter a number between 0 and 32.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
