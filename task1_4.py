#!/usr/bin/python

def dict_str_None(d,str):
  d[str] = None
  return d

print "Task 4_1"
d = {'a':1,'b':2,'c':3}
str = 'b'
print dict_str_None(d,str)




