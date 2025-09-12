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
    unit_distance = str(input())
    print("Please input a value: ")
    value_distance = float(input())
    if unit_distance == "cm":
        cm = value_distance / 100
        print(f"{value_distance} cm in m: {cm:.2f}")
    elif unit_distance == "m":
        m = value_distance
        print(f"")
    elif unit_distance == "km":
    elif unit_distance == "in":
    elif unit_distance == "ft":
    else:
        print("Unsupported unit")



#user asks for mass


#user asks for speed


#user asks for temp
