#!/usr/bin/env python3
# pysc
# Kashev Dalmia | @kashev | kashev.dalmia@gmail.com
# tolower.py

""" Convert a text file to all lower case. To convert
    downloaded dictionaries.
"""

inname = 'dict/TWL06.txt'
outname = 'dict/twl.txt'

with open(inname, 'r') as infile:
    with open(outname, 'w') as outfile:
        for line in infile:
            outfile.write(line.lower())
