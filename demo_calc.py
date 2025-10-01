#! /usr/bin/env python3
# Author: BLawson
# Description: This script will demo
"""
    Docstring:
"""
"""
    Basic Calculator App with add, multiply and divide features
"""


def add(*args):
    """ Return SUM of all arguments as a float """
    sum = 0
    for num in args:
        sum += num
    return float(sum)


def mul(*args):
    """ Return PRODUCT of all arguments as a float """
    total = 1
    for num in args:
        total *= num
    return float(total)


def div(x, z):
    """ Return QUOTIENT of x divided by z to 3 decimal places """
    return round(x / z, 3)


#! /usr/bin/env python3
# Author: BLawson
# Description: This script will demo
"""
    Docstring:
"""
