#!/usr/bin/python

from math import sqrt
from random import uniform

class OneSolution(Exception):pass
class NotSolution(Exception):pass
class NotQudraticEquation(Exception):pass

a = uniform(-10,10)
b = uniform(-10,10)
c = uniform(-10,10)

try:
    print "Equation {0: .3f}x^2 + {1: .3f}x +{2: .3f}".format(a,b,c)

    if a == 0:
        raise NotQudraticEquation

    d = b**2-4*a*c    
    if d == 0:
        raise OneSolution
    if d<0:
        raise NotSolution

    x1 = (-b-sqrt(d))/(2*a)
    x2 = (-b+sqrt(d))/(2*a)

except OneSolution:
    x = -b/(2*a)
    print "x = {: .3f}".format(x)
except NotSolution:
    print "Not Solution"
except:
    print "Unknown Error"
else:
    print "x1 = {0: .3f}".format(x1)
    print "x2 = {0: .3f}".format(x2)

finally:
    print "Goodbye!"
