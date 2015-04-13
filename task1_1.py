#!/usr/bin/python

from math import sqrt,fmod

def multipliers(number):
	s = int(sqrt(number))
	r = []
	for a in xrange(2,s+1):
		while fmod(number,a) == 0:
			r.append(a)
			number = number / a
	return r

def equation(a, b, c):
	r = []
	d = b**2-4*a*c
	if d>0:
		r.append((-b+sqrt(d))/(2*a))
		r.append((-b-sqrt(d))/(2*a))
	elif d == 0:
		r.append(-b/2*a)
	return r


def simple(number):
 	s = int(sqrt(number))
	for a in xrange(2,s+1):
		if fmod(number,a) == 0:
			return "No"
	return "Yes" 

# atm uses only 100, 50, 20, 10, 5 and 1 notes.
def atm(summ):
	banknot = {100:0, 50:0, 20:0, 10:0, 5:0, 1:0}
	keys = banknot.keys()
	keys.sort()
	keys.reverse()
	for key in keys:
		count = 0
		while summ>=key:
			summ -= key
			count += 1
		banknot[key] = count
	
	b_str = ''
	for key in keys:
		b_str += str(key) + ' => ' + str(banknot[key]) + '\n'


	return b_str

print multipliers(30030)

print equation(2, 19, 35) # 2x^2 + 19x + 35 = 0

print simple(11)

print atm(287)
