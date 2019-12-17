# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 13:37:06 2019

@author: Akanksha
"""

# To run this file:
# > python permutation.py input.csv
# or:
# > chmod +x permutation.py
# > ./permutation.py input.csv

import sys
import csv
f = open(sys.argv[1])
r = csv.reader(f, delimiter=',', quotechar='\'', skipinitialspace=True)
data = []
for j in r:
    data.append(j)


output = []

def func(j, t):
    if j == len(data):
        output.append(t)
        return

    for s in data[j]:
        func(j+1, t + s)

func(0, '')

print(*output, sep=', ')