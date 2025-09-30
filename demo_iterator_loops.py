#! /usr/bin/env python3
# Author: BLawson
# Description: This script will demo HOWTO Iterate through a
# collection/sequence (str/tuple/dict/set) using
# an Iterator for loop.
"""
    Docstring:
"""

heroes = ('JFK', 'John Lennon', 'Elvis', 'Pele')

# Iterator through the collection/list using
# an Iterator for loop
for name in heroes:
    print(name)

heroes = ('JFK', 'John Lennon', 'Elvis', 'Pele')

# Iterator through the collection/list using
# an Iterator for loop, double space with \n\n
for name in heroes:
    print(name, end="\n\n")

