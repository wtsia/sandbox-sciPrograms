import math
from math import cos, sin, pi, radians
from sympy import symbols, Eq, solve

# Constants
mp = 1.007277  # mass of proton in atomic mass units (u)
mn = 1.008665  # mass of neutron in u
binding_energy_per_nucleon = 7.47  # MeV
c2 = 931.494  # MeV/u conversion factor
Z = 91
N = 111
total_nucleons = Z + N

def method1(): ###
    print("give number and decays")
    num1 = float(input("num: "))
    decays = float(input("decays: "))

    result = num1 - 2 + 1
    print(result)


def method2(): ###
    print("give protons, neutrons, and MeV")
    Z = float(input("protons: "))
    N = float(input("neutrons: "))
    binding_energy_per_nucleon = float(input("MeV: "))


    total_binding_energy = binding_energy_per_nucleon * total_nucleons
    mass_defect = total_binding_energy / c2
    mass_of_atom = Z * mp + N * mn - mass_defect

    result = mass_of_atom
    print(result)

def method3(): ###
    print("give radius")
    radius = float(input("radius: "))

    # Constants
    radius_fm = radius  # radius in femtometers
    radius_m = radius_fm * 10**-15  # convert to meters
    density = 2.3 * 10**17  # density in kg/m^3

    # Calculate the volume of the nucleus
    volume = (4/3) * math.pi * (radius_m**3)

    # Calculate the mass of the nucleus
    mass_kg = density * volume

    # Convert mass to yoctograms (1 kg = 10^24 yg)
    mass_yg = mass_kg * 10**24

    result = mass_yg*1000
    print(result)

def method4(): ###
    print("give protons, neutrons")
    protons = float(input("protons: "))
    neutrons = float(input("neutrons: "))

    R0 = 1.2  # fm
    A = protons + neutrons  # total number of nucleons (protons + neutrons)
    radius_of_nucleus = R0 * (A ** (1/3))

    result = radius_of_nucleus
    print(result)

def method5():
    print("give atomic number, atomic mass, half life, energy, initial atoms, days")
    atomic_num = float(input("atomic_num: "))
    atomic_mass = float(input("atomic_mass: "))
    half_life = float(input("half_life: "))
    energy = float(input("energy: "))
    initial_atm = float(input("initial_atm: "))
    days = float(input("days: "))



    # Constants
    half_life_days = half_life  # half-life in days
    initial_atoms = initial_atm * 10**12  # initial number of atoms
    time_days = days  # time elapsed in days

    # Convert half-life from days to seconds
    half_life_seconds = half_life_days * 24 * 3600

    # Calculate the decay constant
    decay_constant = math.log(2) / half_life_seconds

    # Convert time from days to seconds
    time_seconds = time_days * 24 * 3600

    # Calculate the remaining number of atoms after the given time
    remaining_atoms = initial_atoms * math.exp(-decay_constant * time_seconds)

    # Calculate the activity in becquerels (Bq)
    activity_bq = decay_constant * remaining_atoms

    # Convert activity to microcuries (1 Bq = 2.7 * 10^-5 µCi)
    activity_microcuries = activity_bq * 2.7 * 10**-5

    result = activity_microcuries
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
