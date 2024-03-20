import math
mu_0 = 4 * math.pi * (10 ** -7)

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
    print("give r_a, r_b, k, L, V")
    r_a = float(input("r_a: "))
    r_b = float(input("r_b: "))
    k = float(input("k: "))
    L = float(input("L: "))
    V = float(input("V: "))
    result = (2*math.pi*L*k*8.85*(10**-12) / (math.log(r_b/r_a))) * 0.5 * V**2 * 10**9
    print(result)
    print("")

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

def method14(): 
    print("give resivity, current, radius, length")
    resivity = float(input("resivity: "))
    current = float(input("current: "))
    radius = float(input("radius: "))
    length = float(input("length: "))
    resistance = (resivity * (10 ** -9) * length) / (math.pi * (radius / 100) ** 2)
    result = current * resistance * 1000000
    print(result)
    print("")

def method15():
    print("give r1, r2, r3, i")
    r1 = float(input("r1: "))
    r2 = float(input("r2: "))
    r3 = float(input("r3: "))
    i = float(input("i: "))
    req = r1*r2*r3 / (r1*r2 + r2*r3 + r3*r1)
    result = req *i / r3
    print(result)
    print("")

def method16():
    print("give r, cap, v, rateDenominator")
    r = float(input("r: "))
    cap = float(input("cap: "))
    v = float(input("v: "))
    rateDenominator = float(input("rateDenominator: "))
    result = v/r * (rateDenominator - 1)/rateDenominator
    print(result)
    print("")

def method17():
    print("give a, n, i, b, theta")
    a = float(input("a: "))
    n = float(input("n: "))
    i = float(input("i: "))
    b = float(input("b: "))
    theta = float(input("theta: "))
    tmpvar6 = 90-theta;
    result = n * b * i * a * math.sin(tmpvar6*math.pi/180)/10000
    print(result)
    print("")

def method18():
    print("give protonVel, b_x, b_y, b_z")
    protonVel = float(input("protonVel: "))
    b_x = float(input("b_x: "))
    b_y = float(input("b_y: "))
    b_z = float(input("b_z: "))
    new_y = protonVel*b_x*1.6/1000
    new_x = protonVel*b_y*-1.6/1000
    result = 180 + (math.atan(new_y/new_x) * 180 / math.pi)
    print(result)
    print("")

def method19():
    print("give current, arcRadius, uniformField")
    current = float(input("current: "))
    arcRadius = float(input("arcRadius: "))
    uniformField = float(input("uniformField: "))
    h = math.sqrt(2 * ((arcRadius/100) ** 2))
    result = current * h * uniformField
    print(result)
    print("")

def method20():
    print("give radius, distance, and centralAxisMagField")
    radius = float(input("radius: "))
    distance = float(input("distance: "))
    centralAxisMagField = float(input("centralAxisMagField: "))
    tmpcurr = math.pi / 1000000 * distance**2
    result = (centralAxisMagField / 1000000) * (2 * math.pi * distance / 1000) / ((4*math.pi / 10000000) * (tmpcurr)) 
    print(result)
    print("")

def method21():
    print("give length, omega, bHat")
    length = float(input("length: "))
    omega = float(input("omega: "))
    bHat = float(input("bHat: "))
    result = 0.5*bHat*omega* (length*0.001) ** 2 * 100
    print(result)
    print("")

def method22():
    print("give distance, current")
    distance = float(input("distance: "))
    current = float(input("current: "))
    tmpvar = 4*math.pi*math.pow(10, -7)*current/(2*math.pi*distance*math.pow(10, -2))
    tmpvar2 = math.pow(tmpvar, 2)/(2*4*math.pi*math.pow(10, -7))
    result = tmpvar2*1000000
    print(result)
    print("")

def method23():
    print("give voltage, inductor, resistor, percent")
    voltage = float(input("voltage: "))
    inductor = float(input("inductor: "))
    resistor = float(input("resistor: "))
    percent = float(input("percent "))
    tmpvar = voltage/resistor
    tmpvar2 = tmpvar*percent/100
    result = 1.0/2.0*inductor*math.pow(tmpvar2, 2)
    print(result)
    print("")

def method24():
    print("give energyFlow, rect1, rect2, minutes")
    energyFlow = float(input("energyFlow: "))
    rect1 = float(input("rect1: "))
    rect2 = float(input("rect2: "))
    minutes = float(input("minutes: "))
    result = energyFlow * rect1 * rect2 * minutes * 60 / 10000
    print(result)
    print("")

def method25():
    print("give a, b, i")
    a = float(input("a: "))
    b = float(input("b: "))
    i = float(input("i: "))
    result = 4 * math.pi * (10 ** -7) * i / 8 * (1/a - 1/b) * 1000000
    print(result)
    print("")

def method26():
    print("give turns, curr, radius, bx, by, bz")
    turns = float(input("turns: "))
    curr = float(input("curr: "))
    radius = float(input("radius: "))
    bx = abs(float(input("bx: ")))
    by = abs(float(input("by: ")))
    bz = abs(float(input("bz: ")))
    area = math.pi*((radius/100) ** 2)
    i = curr * turns * area * bx
    j = curr * turns * area * by
    torque =  (i ** 2) +  (j ** 2)
    result = math.sqrt(torque)
    print(result)
    print("")

def method27(): 
    print("give hz, mh, percent")
    hz = float(input("hz: "))
    mh = float(input("mh: "))
    percent = float(input("percent: "))
    result = 10000000/(4*(math.pi**2)*(hz**2)*mh)*percent
    print(result)
    print("")

def method28():
    print("give turns, length, radius, turns2, length2, radius2")
    turns = float(input("turns: "))
    length = float(input("length: "))
    radius = float(input("radius: "))
    turns2 = float(input("turns2: "))
    length2 = float(input("length2: "))
    radius2 = float(input("radius2: "))
    area2 = math.pi * ((radius2/100) ** 2)
    result = mu_0 * turns * turns2 * area2 / (length / 100) * 1000
    print(result)
    print("")

def method29():
    print("give turnCoil, diameter, magField, degree, percent, seconds")
    turnCoil = float(input("turnCoil: "))
    diameter = float(input("diameter: "))
    magField = float(input("magField: "))
    degree = float(input("degree: "))
    percent = float(input("percent: "))/100
    seconds = float(input("seconds: "))
    result = abs(turnCoil*math.pi*((diameter/2)**2) * (percent*magField - magField) * math.cos((90-degree)/180*math.pi) / (seconds) / 10000)
    print(result)
    print("")

def method30():
    print("give ohm1, ohm2, ohm3")
    ohm1 = float(input("ohm1: "))
    ohm2 = float(input("ohm2: "))
    ohm3 = float(input("ohm3: "))
    result = 1/(1/ohm1 + 1/ohm2 + 1/ohm3)
    print(result)
    print("")

def method31():
    print("give capacitor")
    capacitor = float(input("capacitor: "))
    result = math.e ** (2 * math.pi * 8.85 / capacitor)
    print(result)
    print("")

def method32():
    print("give rate, distance")
    rate = float(input("rate: "))
    distance = float(input("distance: "))
    result = 2*rate/distance*10
    print(result)
    print("")



def default():
    print("Invalid choice")

def generate_switch_dict():
    switch_dict = {}
    for i in range(1, 33):
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
