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


a = [1,5,6,5,3,3,3,2,23,4,55,2]
print repeat_list(a)

a = [1,'Hello',[1,4,7],'Yes',5,7,9+8j,['ya.ru','google.ru'],{1:'python',2:'php',3:'awk'}]
print_type_stat(a)


a = ['Hello','yandex','gmail','python','RU']
print sort_end(a)


  

