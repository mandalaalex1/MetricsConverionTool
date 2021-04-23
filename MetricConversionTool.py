print("Options:")
print("[P] Print Options")
print("[C] Convert from Celsius")
print("[F] Convert from Fahrenheit")
print("[M] Convert from Miles")
print("[KM] Convert from Kilometers")
print("[In] Convert from Inches")
print("[CM] Convert from Centimeters")
print("[Y] Convert from Yard")
print("[Me] Convert from Meters")
print("[Q] Quit")
Option1 = ''
while Option1 != 'Q':
    Option1 = input("Option: ")

    operations = {"C":{"message":"Celsius Temperature: ","formula":"float(input_value*9//5 +32)","print":"Fahrenheit: "},
                  "F":{"message":"Fahrenheit Temperature: ","formula":"float((input_value-32)*5//9)","print":"Celcius: "}}
    operations = {"M":{"message":"Miles Distance: ","formula":"float((input_value//1.609))","print":"Kilometers: "},
                  "KM":{"message":"Kilometers Distance: ","formula":"float((input_value*1.609))","print":"Miles:  "}}
    operations = {"In":{"message":"Inches: ","formula":"float((input_value*2.54))","print":"Centimeters: "},
                  "CM":{"message":"Centimeters: ","formula":"float((input_value//2.54))","print":"Inches: "}}
    operations = {"Y":{"message":"Yard: ","formula":"float((input_value//1.094))","print":"Meters: "},
                  "Me":{"message":"Meters: ","formula":"float((input_value*1.094))","print":"Yard: "}}

    opt = operations.get(Option1, None)

    if opt:
        input_value = int(input(operations[Option1]['message']))
        out = eval(operations[Option1]['formula'])
        print(operations[Option1]['print'] + str(out))