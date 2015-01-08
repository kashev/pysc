#!/usr/bin/env python3
# pysc
# Kashev Dalmia | @kashev | kashev.dalmia@gmail.com
# tolower.py

""" Convert a text file to all lower case. To convert
    downloaded dictionaries.
"""

iname = 'dict/TWL06.txt'
oname = 'dict/twl06.txt'

with open(iname, 'r') as ifile:
    with open(oname, 'w') as ofile:
        for line in ifile:
            ofile.write(line.lower())
