#! /usr/bin/env python3
# Author: BLawson
# Description: This script will demo
"""
    Docstring:
"""
import random

lotto = [] #  create empty list

while len(lotto) < 6:
    num = random.randint(1, 50)
    if num not in lotto:
        lotto.append(num)
    else:
        print("duplicate number =", num)



print(lotto)
