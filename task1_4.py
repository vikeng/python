#!/usr/bin/python

def dict_str_None(d,str):
  if str in d:
    d[str] = None
  return d

def dict_merge(d1,d2):
  set1 = set(d1.keys())
  set2 = set(d2.keys())
  sd = set1 & set2
  
  for s in sd:
    del d1[s]
    del d2[s]
  return dict(d1.items()+d2.items())


def swap_dict(d):
  return dict([value,key] for key,value in d.iteritems())

  
print "Task 4_3"
d = {'a':1,'b':2,'c':3}
str = 'b'
print d
print 'str = ' + str
print dict_str_None(d,str)


print "Task 4_4"
d1 = {'a':1,'b':2,'c':3}
d2 = {'e':4,'b':4,'t':7}
print d1
print d2

print dict_merge(d1,d2)



print "Task 4_6"
d = {'a':1,'b':2,'c':3}
print d

print swap_dict(d)




