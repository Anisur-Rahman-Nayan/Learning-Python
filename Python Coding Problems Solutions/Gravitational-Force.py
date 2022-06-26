print("Gravitational Force Calculation.....")

mass1= float(input("Enter 1st mass: "))
mass2 = float(input("Enter 2nd mass: "))
r = float(input("Distance Between the Objects: "))
G = 6.673 *(10**-11)

force = (G*mass1*mass2)/(r**2)

print(f"The Gravitational force is {round(force,5)} N")