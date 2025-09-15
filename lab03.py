"""
Welcome to Lab 03. This is Brendan speaking.

We WILL be grading for Header, Comments, Formatting.

Follow the instructions in the lab document. <---- very important
Write your code to complete the tests in the Gradescope autograder.

Necessary print statements:

"Please select one of the following to convert to meters: cm m km in ft: "
"Please select one of the following to convert to grams: mg g kg lbs: "
"Please select one of the following to convert to meters per second: m/s km/h ft/s mph: "
"Please select one of the following to convert to Celsius: C F K: "

"Please input a value: "
"Unsupported unit"
"Invalid unit type"

"""

"""
Author: Sophia Sampson
Date: September 15, 2025
Assignment: Lab 03
Course: CPSC 1051
Lab Section: 002

SHORT DESCRIPTION

"""
#welcome user
print("Welcome to the SI units calculator!")

#ask for type of unit
print("Please input a type of unit that you would like to convert. Here are your options: \ndistance \nmass \nspeed \ntemperature\n")
type = str(input())

#user asks for distance
if type == "distance":
    print("Please select one of the following to convert to meters: cm m km in ft: ") 
    unit_distance = str(input())        #user chooses a unit within distance
    print("Please input a value: ")
    value_distance = float(input())     #user inputs a value for conversion
    if unit_distance == "cm":       #cm conversion
        cm = value_distance / 100
        print(f"{value_distance} cm in m: {cm:.2f}")
    elif unit_distance == "m":      #m conversion
        m = value_distance
        print(f"{value_distance} m in m: {m:.2f}")
    elif unit_distance == "km":     #km conversion
        km = value_distance * 1000
        print(f"{value_distance} km in m: {km:.2f}")
    elif unit_distance == "in":     #in conversion
        inch = value_distance * 0.0254
        print(f"{value_distance} in in m: {inch:.2f}")
    elif unit_distance == "ft":     #ft conversion
        ft = value_distance * 0.3048
        print(f"{value_distance} ft in m: {ft:.2f}")
    else:
        print("Unsupported unit")

#user asks for mass
elif type == "mass":
    print("Please select one of the following to convert to grams: mg g kg lbs: ") 
    unit_mass = str(input())        #user chooses unit within mass
    print("Please input a value: ")
    value_mass = float(input())     #user inputs a value for conversion
    if value_mass < 0:         #no negative mass
        print(f"You can't have a negative mass!")
    elif unit_mass == "mg":       #mg conversion
        mg = value_mass / 1000
        print(f"{value_mass} mg in g: {mg:.2f}")
    elif unit_mass == "g":      #g conversion
        g = value_mass
        print(f"{value_mass} g in g: {g:.2f}")
    elif unit_mass == "kg":     #kg conversion
        kg = value_mass * 1000
        print(f"{value_mass} kg in g: {kg:.2f}")
    elif unit_mass == "lbs":        #lbs conversion
        lbs = value_mass * 453.592
        print(f"{value_mass} lbs in g: {lbs:.2f}")
    else:
        print("Unsupported unit")

#user asks for speed
elif type == "speed":
    print("Please select one of the following to convert to meters per second: m/s km/h ft/s mph: ") 
    unit_speed = str(input())       #user chooses unit within speed
    print("Please input a value: ")
    value_speed = float(input())        #user inputs a value for conversion
    if unit_speed == "m/s":         #m/s conversion
        ms = value_speed
        print(f"{value_speed} m/s in m/s: {ms:.2f}")
    elif unit_speed == "km/h":      #km/h conversion
        kmh = value_speed * 0.277778
        print(f"{value_speed} km/h in m/s: {kmh:.2f}")
    elif unit_speed == "ft/s":       #ft/s conversion
        fts = value_speed * 0.3048
        print(f"{value_speed} ft/s in m/s: {fts:.2f}")
    elif unit_speed == "mph":        #mph conversion
        mph = value_speed * 0.44704
        print(f"{value_speed} mph in m/s: {mph:.2f}")
    else:
        print("Unsupported unit")

#user asks for temp
elif type == "temperature":
    print("Please select one of the following to convert to Celsius: C F K: ") 
    unit_temp = str(input())
    print("Please input a value: ")
    value_temp = float(input())
    if unit_temp == "C":
        cel = value_temp
        print(f"{value_temp} C in C: {cel:.2f}")
    elif unit_temp == "F":
        far = (value_temp - 32) * 5/9
        print(f"{value_temp} F in C: {far:.2f}")
    elif unit_temp == "K":
        kal = value_temp - 273.15
        print(f"{value_temp} K in C: {kal:.2f}")
    else:
        print("Unsupported unit")

else:
    print("Invalid unit type")