#!/usr/bin/python

def repeat_list(list):
  r = []
  list.sort()
  for l in set(list[1:]):
    if list.count(l)>1:
      r.append(l)
  return r

def print_type_stat(list_var):
  stat = {}
  for v in list_var:
    s = str(type(v)).split("'")[1]
    if s in stat:
       stat[s] += 1
    else:
      stat[s] = 1
  for s in stat:
    print s + ' => ' + str(stat[s])

def sort_end(str_list):
  str_list2 = []

  for s in str_list:
    str_list2.append(s[::-1])

  str_list2.sort()
  
  str_list3 = []
  for s in str_list2:
    str_list3.append(s[::-1])

  return str_list3


def insert_str(list,str):
  f = 1
  for l in list:
    if str<l:
      k = list.index(l)
      list.insert(k,str)
      f = 0 
      break
  if f:
    list.append(str)
      
  return list

def search_insert(list1,list2,x):
  count = list1.count(x)
  for i in xrange(count):
    k = list1.index(x)
    list1[k] = str(x)+'!'
    list2.insert(k,x)
  return list2

def del_odd(list):
  list2 = []
  for s in list:
    if len(s)%2==0:
      list2.append(s)
  return list2

def len_max_list(list):
  prev = list[0]
  list.append(list[-1]-1)
  list_split = []
  tmp_list = [prev]
  max_len = 0
  for l in list[1:]:
    if l != prev+1:
      if len(tmp_list) > max_len:
        max_len = len(tmp_list)
        max_list = tmp_list
      tmp_list = []        
    tmp_list.append(l)
    prev = l
    

  return max_list

a = [1,5,6,5,3,3,3,2,23,4,55,2]
print "N1"
print a
print repeat_list(a)


a = [1,'Hello',[1,4,7],'Yes',5,7,9+8j,['ya.ru','google.ru'],{1:'python',2:'php',3:'awk'}]
print "\nN2"
print a
print_type_stat(a)


a = ['Hello','yandex','gmail','python','RU']
print "\nN3"
print a
print sort_end(a)


list = ['asdf','bbb','ddd']
print "\nN4"
print list
print insert_str(list,'ccc')

list1 = [1,2,3,4,3,6,7,8,3]
list2 = ['a','b','c','d','e']

print "\nN5 "
print list1
print list2
print search_insert(list1,list2,3)

list = ['asdf','bbb','ddd','1234','NG']
print "\nN6"
print list
print del_odd(list)

list = [1,2,5,5,6,7,9,1,11,12,3,13,14,15,16]
print "\nN7"
print list
print len_max_list(list)
