#! /usr/bin/env python3
# Author: BLawson
# Description: This is a calculator app
"""
    Calculator App with basic and advanced functions
"""
import sys

import basic
import adv

from calculator.app.basic import *
from calculator.app.adv import *

menu = """
    Menu Options
    -------------
    1. Calculator
    2. Advanced Calculator
    3. Quit
"""

print("********** Calc APP ***********")
print(menu)
option = input("Enter your option: 1-2, q=quit: ")

if option == "1":
    print(f"9 * 8 * 7 = {add(9 * 8 * 7)}")
    print(f"9 * 8 * 7 = {mul(9 * 8 * 7)}")
    print(f"9 / 8 = {div(9 / 8)}")
elif option == "2":
    print(f"9 % 8 = {mod(9 % 8)}")
    print(f"9**8 = {power(9 / 8)}")
    print(f"\N{square root}98 = {sqrt(98)}")
elif option == "q":
    brake

print("Done")
sys.exit(0)