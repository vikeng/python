#!/usr/bin/python

from math import sqrt
from random import uniform

x = uniform(-3,5)
try:
    y = sqrt(x)
    print "sqrt('{0: .3f}') = {1: .3f}".format(x,y)
except:
    print "Impossible calculate {: .3f}".format(x)
