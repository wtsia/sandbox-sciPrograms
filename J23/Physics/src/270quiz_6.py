import math

def method1():
    print("give radii, d_lens, d_image")
    R_1 = float(input("radii: "))
    d_o = float(input("d_lens: "))
    d_i = float(input("d_image: "))

    # Given values
    d_i = -d_i  # image distance in cm (virtual image)
    # Calculating the focal length (f) using the lens equation
    f = 1 / ((1 / d_o) + (1 / d_i))
    # Given radii of curvature
    R_2 = -R_1  # radius of curvature in cm for the second surface
    # Solving for n using the lensmaker's equation
    n = 1 + (1/f) * (1 / (1/R_1 - 1/R_2))

    result = n
    print(result)

def method2():
    print("give f, h_0, d_0")
    f = float(input("f: "))
    h_0 = float(input("h_0: "))
    d_o = float(input("d_0: "))

    # Calculating the image distance (d_i)
    d_i = 1 / ((1 / f) - (1 / d_o))

    result = d_i
    print(result)

def method3():
    print("give power, diameter")
    P = float(input("power: "))
    diameter = float(input("diameter: "))

    # Calculating the focal length in meters
    f_meters = 1 / P

    # Converting the focal length to centimeters
    f_cm = f_meters * 100

    result = f_cm
    print(result)

def method4():
    print("give tall, front, real_img")
    tall = float(input("tall: "))
    d_o = float(input("front: "))
    d_i = float(input("real_img: "))

    # Calculating the focal length (f)
    f = 1 / ((1 / d_o) + (1 / d_i))

    result = f
    print(result)

def method5():
    print("give index, tall, left, right")
    n2 = float(input("index: "))
    tall = float(input("tall: "))
    u = float(input("left: "))
    v = float(input("right: "))

    # Given values
    n1 = 1
    u = -u  # object distance in cm

    # Calculating the radius of curvature (R)
    R = (n2 - n1) / ((n2 / v) - (n1 / u))

    result = R
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
