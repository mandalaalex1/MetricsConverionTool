print("Options:")
print("[P] Print Options")
print("[C] Convert from Celsius")
print("[F] Convert from Fahrenheit")
print("[M] Convert from Miles")
print("[KM] Convert from Kilometers")
print("[In] Convert from Inches")
print("[CM] Convert from Centimeters")
print("[Q] Quit")
while True:
    Option1 = input("Option: ")

    if Option1 == "C":
        Celsius = int(input("Celsius Temperature: "))
        F1 = float(Celsius*9//5 +32)
        print("Fahrenheit: " + str(F1))

    elif Option1 == "F":
        Fahrenheit = int(input("Fahrenheit Temperature: "))
        C1 = float((Fahrenheit-32)*5//9)
        print("Celcius: " + str(C1))

    elif Option1 == "M":
        Miles = int(input("Miles Distance: "))
        M1 = float((Miles//1.609))
        print("Kilometers: " + str(M1))

    elif Option1 == "KM":
        Kilometers = int(input("Kilometers Distance: "))
        KM1 = float((Kilometers*1.609))
        print("Miles: " + str(KM1))

    elif Option1 == "In":
        Inches = int(input("Inches: "))
        In = float((Inches*2.54))
        print("Centimeters: " + str(In))

    elif Option1 == "CM":
        Centimeters = float(input("Centimeters: "))
        CM1 = float((Centimeters//2.54))
        print("Inches: " + str(CM1))

    elif Option1 == "Y":
        Yard = float(input("Yard: "))
        Y1 = float((Yard//1.094))
        print("Meters: " + str(Y1))

    elif Option1 == "MT":
        Meters = float(input("Meters: "))
        MT1 = float((Meters*1.094))
        print("Yard: " + str(MT1))

    elif Option1 == "Q":
        print("Good bye!! :)")
        break