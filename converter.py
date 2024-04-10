#
# converter.py – module with functions to convert between our temperature formats #
# You can input to convert among Fahrenheit, Celsius and Kelvin .
#

import numpy as ny
from conversions import *
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
UNDERLINE = '\033[4m'
BOLD = '\033[1m'
RESET = '\033[0m'
LINE_CLEAR = '\x1b[2K'
LINE_UP = '\033[1A'

print("\nWelcome to the conversions of three types of temperature!\n")


treats = [["#", "Name", "type"],
         [1, "Fahrenheit", "fahr to cel"],
	     [2, "Celsius", "cel to fahr"],
         [3, "Fahrenheit", "fahr to kelvin"],
         [4, "Celsius", "cel to kelvin"],
         [5, "Kelvin", "kelvin to fahr"],
         [6, "Kelvin", "kelvin to cel"]
         ]



more = 'Y'
#more = input(print(YELLOW, '\nWould you like a treat (Y/N)... ', RESET))
while more != 'N':
    #print(BOLD, '\nWould you like a treat (Y/N)... ')
    more = input('\033[1m\nWould you like to convert \033[0m')
    #print('\r', end=LINE_CLEAR)
    #more = input(inputask)
    print("Which temperature would you like?")
    for rindex, row in enumerate(treats):
        for cindex, element in enumerate(row):
            print(str(treats[rindex][cindex]).center(23," "), end="|")
        print()

    selection = int(input("    Enter your selection:  "))
    temperature = int(input("    Enter your temperature:  "))

    if selection == 1:
        print(f" {treats[selection][1]} is  {temperature}, {treats[selection][2]} is , {fahr2cel(temperature)}")
    elif selection == 2:
        print(f" {treats[selection][1]} is  {temperature}, {treats[selection][2]} is , {cel2fahr(temperature)}")
    elif selection == 3:
        print(f" {treats[selection][1]} is  {temperature}, {treats[selection][2]} is , {fahr2kelvin(temperature)}")
    elif selection == 4:
        print(f" {treats[selection][1]} is  {temperature}, {treats[selection][2]} is , {cel2kelvin(temperature)}")
    elif selection == 5:
        print(f" {treats[selection][1]} is  {temperature}, {treats[selection][2]} is , {kelvin2fahr(temperature)}")
    elif selection == 6:
        print(f" {treats[selection][1]} is  {temperature}, {treats[selection][2]} is , {kelvin2cel(temperature)}")
    else:
        print(RED, "Oh dear! you are out of order")
        more = 'N'

    # if selection <= 0 or selection >6 :
    #     print(RED, "Oh dear! you are out of order")
    #     more = 'N'   



print()