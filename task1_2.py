#!/usr/bin/python

from random import randrange

def letters(big_string):
	str = ''
	for c in big_string:
		if 'A'<=c<='Z':
			str += c
	return str

def palindrome(pali):
	pali2=pali[::1]

	if pali==pali2:
		return 'Paliandrom'
		
	return 'Not paliandrom'

def find_letter(where, letter):
	list = where.split()
	letter_list=[]

	for word in list:
		if letter.lower() == word.lower()[0]:
			letter_list.append(word.lower())
	return letter_list

def mix_words(just_string):
	list = just_string.split()
	l = len(list)
	for i in xrange(l):
		k = randrange(l)
		list[i],list[k] = list[k],list[i] 
	new_str = ' '.join(list)

	return new_str
		

print letters("Trees Are So Kind")

print palindrome("avid diva")

print find_letter("Bears are the best animals ever", 'b')

print mix_words("Bears are the best animals ever")
