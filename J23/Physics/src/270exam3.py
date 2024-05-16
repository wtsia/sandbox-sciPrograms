import math
import sympy as sp
import scipy.constants as const
import numpy as np
from scipy.constants import c, physical_constants
from scipy.constants import h, proton_mass
import numpy as np
from scipy.constants import physical_constants
from scipy.constants import e, epsilon_0, h, pi


# Constants
m = const.proton_mass
c = const.c

def method1(): ###
    print("give initial_spd, final_spd")
    init_spd = float(input("init: "))
    final_spd = float(input("final: "))


    # Initial and final speeds
    v_i = init_spd * c
    v_f = final_spd * c

    # Relativistic kinetic energy calculation
    def kinetic_energy(m, v):
        return (1 / (1 - v**2 / c**2)**0.5 - 1) * m * c**2

    E_i = kinetic_energy(m, v_i)
    E_f = kinetic_energy(m, v_f)
    delta_E = (E_f - E_i) / 1.60218e-13  # Convert from Joules to MeV

    
    result = delta_E
    print(result)

def method2(): ###
    print("give particle1, particle2, msLater")
    particle1 = float(input("particle1: "))
    particle2 = float(input("particle2: "))
    msLater = float(input("msLater: "))

    # Velocities
    v1x = particle1 * c
    v1y = 0
    v2x = 0
    v2y = particle2 * c

    v_rel_corrected = np.sqrt(v1x**2 + v2y**2 - (v1x * v2y / c)**2) / c
    result = v_rel_corrected
    print(result)

def method3(): ###
    print("give speed, lifetime")
    speed = float(input("speed: "))
    lifetime = float(input("lifetime: "))

    # Given data for Question 3
    v_particle = speed*10**8  # speed in m/s
    tau_lab = lifetime*10**-6  # lifetime in seconds

    # Lorentz factor calculation for the particle
    gamma_particle = 1 / np.sqrt(1 - (v_particle / c)**2)

    # Proper lifetime calculation
    tau_rest = tau_lab / gamma_particle

    result = tau_rest * 1e6
    print(result)

def method4(): ###
    print("give times")
    times = float(input("times: "))

    # Constants
    m_e = physical_constants['electron mass energy equivalent in MeV'][0]  # Electron mass in MeV/c^2

    # Total energy of the electron
    E = times * m_e

    # Momentum calculation using the energy-momentum relation
    p_corrected = np.sqrt(E**2 - m_e**2)  # in MeV/c
    result = p_corrected*1000
    print(result)

def method5(): ###
    print("give speed")
    speed = float(input("speed: "))

    # Convert speed from km/s to m/s
    v_proton = speed * 10**3  # m/s

    # Momentum of the proton
    p_proton = proton_mass * v_proton  # kg*m/s

    # de Broglie wavelength in meters
    lambda_proton = h / p_proton

    # Convert wavelength to picometers (1m = 1e12 pm)
    lambda_proton_pm = lambda_proton * 1e12
    result = lambda_proton_pm

    print(result)

def method6(): ###
    print("give degrees")
    degrees = float(input("degrees: "))

    # Constants
    compton_wavelength = physical_constants['Compton wavelength'][0]  # in meters

    # Convert angle to radians
    theta = np.deg2rad(degrees)

    # Compton shift calculation in meters
    compton_shift = compton_wavelength * (1 - np.cos(theta))

    # Convert shift to picometers
    compton_shift_pm = compton_shift * 1e12
    result = compton_shift_pm
    print(result)

def method7(): ###
    print("give emits, wavelength, time")
    emits= float(input("emits: "))
    wavelength= float(input("wavelength: "))
    time= float(input("time: "))

    # Constants and given values
    power = emits*10**-3  # Power in watts
    time = time*10**-3  # Time in seconds
    wavelength_nm = wavelength  # Wavelength in nanometers
    wavelength_m = wavelength_nm * 1e-9  # Convert nm to m

    # Energy of a single photon (E = hc/λ)
    E_photon = h * c / wavelength_m  # Energy in joules

    # Number of photons emitted
    N_photons = (power * time) / E_photon

    # Convert number of photons to peta photons (1 Peta = 1e15)
    N_photons_peta = N_photons / 1e15
    result = N_photons_peta

    print(result)

def method8():
    print("give n, energy, state")
    n = float(input("n: "))
    energy = float(input("energy: "))
    state = float(input("state: "))
    
    # Given energies and states
    E_n5 = energy  # Energy at n=5 in keV

    # Using the proportional relationship (n^2 law)
    n5 = n
    n12 = state

    # Calculate E_n12 using proportionality
    E_n12 = E_n5 * (n12**2 / n5**2)

    # Calculate the energy difference
    delta_E = E_n12 - E_n5

    result = delta_E
    print(result)

def method9(): ###
    print("give energy, u, w")
    energy = float(input("energy: "))
    u = float(input("u: "))
    w = float(input("w: "))

    # Given values for Question 9
    K_energy = energy  # Kinetic energy in eV
    U_barrier = u  # Potential energy barrier in eV
    width = w*10**-9  # Barrier width in meters

    # Constants
    m_e_kg = physical_constants['electron mass'][0]  # Electron mass in kg
    k1 = np.sqrt(2 * m_e_kg * K_energy * 1.60218e-19) / physical_constants['Planck constant'][0]  # in 1/m
    k2 = np.sqrt(2 * m_e_kg * (U_barrier - K_energy) * 1.60218e-19) / physical_constants['Planck constant'][0]  # in 1/m

    # Tunneling probability using the quantum mechanical tunneling formula
    T = np.exp(-2 * k2 * width)

    # Constants in Joules and meters for precise computation
    hbar = physical_constants['Planck constant over 2 pi'][0]  # Reduced Planck's constant in J*s

    # Recalculate k2 more precisely
    k2_precise = np.sqrt(2 * m_e_kg * (U_barrier * 1.60218e-19 - K_energy * 1.60218e-19)) / hbar  # in 1/m

    # Recalculate the tunneling probability using the precise value of k2
    T_precise = np.exp(-2 * k2_precise * width)
    T_precise_percent = T_precise * 100  # Convert to percentage
    result = T_precise_percent
    print(result)

def method10(): ###
    print("give momentum, plusMinus, location")
    momentum = float(input("momentum: "))
    plusMinus = float(input("plusMinus: "))
    location = float(input("location: "))

    # Given uncertainty in momentum in eV/c
    delta_p_eVc = plusMinus # in eV/c

    # Convert delta_p from eV/c to kg*m/s
    delta_p = delta_p_eVc * 1.60218e-19 / c  # Converting eV/c to kg*m/s using eV to J conversion

    # Calculate the minimum uncertainty in position using Heisenberg's principle
    hbar = physical_constants['Planck constant over 2 pi'][0]
    delta_x_min = hbar / (2 * delta_p)

    # Convert delta_x_min from meters to nanometers
    delta_x_min_nm = delta_x_min * 1e9
    result = delta_x_min_nm
    print(result)

def method11():  ###
    print("give potDiff, uncertainty")
    potDiff = float(input("potDoff: "))
    uncertainty = float(input("uncertainty: "))

    V = potDiff*10**3  # Potential difference in volts

    # Energy gained by the proton (eV), then converted to Joules
    E_kinetic = V * 1.60218e-19  # Proton charge in Coulombs times voltage

    # Momentum of the proton using p = sqrt(2mE)
    p_proton_joules = np.sqrt(2 * proton_mass * E_kinetic)  # in kg*m/s

    # Given uncertainty in position in meters
    delta_x = uncertainty*10**-15  # in meters

    # Calculate the minimum uncertainty in momentum using Heisenberg's principle
    hbar = physical_constants['Planck constant over 2 pi'][0]
    delta_p_min = hbar / (2 * delta_x)

    # Calculate the minimum percent uncertainty in momentum
    delta_p_percent = (delta_p_min / p_proton_joules) * 100
    result = delta_p_percent
    print(result)

def method12():
    print("give n, energy")
    n = float(input("n: "))
    energy = float(input("energy: "))

    # Constants
    hbar_Js = physical_constants['Planck constant over 2 pi'][0]  # in J*s
    m_proton_kg = physical_constants['proton mass'][0]  # Proton mass in kg

    # Given energy for n=14 in MeV converted to Joules
    E_n14 = energy * 1.60218e-19

    # Quantum number for n=14
    n14 = n

    # Calculate the length of the box L from the energy formula rearranged
    L = np.sqrt((n14**2 * np.pi**2 * hbar_Js**2) / (2 * m_proton_kg * E_n14))

    # Calculate the wavelength lambda for n=14
    lambda_n14 = 2 * L / n14

    # Convert lambda from meters to femtometers (1 m = 1e15 fm)
    lambda_n14_fm = lambda_n14 * 1e12
    result = lambda_n14_fm
    print(result)

def method13(): 
    print("give n")
    n = float(input("n: "))

    # Quantum number n=7
    n7 = n

    # Speed of the electron in the Bohr model for hydrogen
    v_n7 = (e**2) / (2 * epsilon_0 * h) / n7

    # Convert speed from m/s to km/s
    v_n7_kms = v_n7 / 1000
    result = v_n7_kms
    print(result)

def method14(): 
    print("give atomic_num, mass")
    atomic_num = float(input("atomic_num: "))
    mass = float(input("mass: "))
    
    # Initial atomic number and mass
    atomic_number_initial = atomic_num
    mass_initial = mass

    # After alpha decay
    atomic_number_after_alpha = atomic_number_initial - 2
    mass_after_alpha = mass_initial - 4

    # After subsequent beta-minus decay
    atomic_number_final = atomic_number_after_alpha + 1

    result = atomic_number_final
    print(result)

def method15():
    print("give protons, neutrons, nucleon")
    protons = float(input("protons: "))
    neutrons = float(input("neutrons: "))
    nucleon = float(input("nucleon: "))

    # Constants and given values
    Z = protons  # Number of protons
    N = neutrons  # Number of neutrons
    BE_per_nucleon = nucleon  # Binding energy per nucleon in MeV

    # Masses in atomic mass units (u)
    m_p_u = physical_constants['proton mass'][0] / physical_constants['atomic mass constant'][0]
    m_n_u = physical_constants['neutron mass'][0] / physical_constants['atomic mass constant'][0]

    # Total binding energy in MeV
    total_BE = BE_per_nucleon * (Z + N)  # Total binding energy for all nucleons

    # Conversion of total binding energy from MeV to atomic mass units (u)
    BE_u = total_BE / 931.494  # Convert MeV to u

    # Calculate the mass of the neutral atom in atomic mass units (u)
    M = Z * m_p_u + N * m_n_u - BE_u
    result = M
    print(result)

def method16(): ###
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
