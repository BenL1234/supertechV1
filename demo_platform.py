#! /usr/bin/env python3
# Author: BLawson
# Description: This script will demo
"""
    Docstring:
"""

import sys

print(sys.platform)

if sys.platform == 'win32':
    print("Running on Windows")
elif sys.platform == 'darwin':
    print("Running on Mac")
elif sys.platform == 'linux':
    print("Running on Linux")
else:
    print("Other platform")


import sys
import os

my_home = None

if sys.platform == "win32":
    my_home = os.environ['HOMEPATH']
elif sys.platform == "darwin" or sys.platform == "linux":
    my_home = os.environ['HOME']
else:
    print("On some other OS")

print("Home is", my_home)
