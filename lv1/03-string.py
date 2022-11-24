#!/usr/bin/python

# Basic string exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.


# S.1 cubes
# Given an int count of a number of cubes, return a string
# of the form 'Number of cubes: <count>', where <count> is the number
# passed in. However, if the count is 15 or more, then use the word 'many'
# instead of the actual count.
# So cubes(5) returns 'Number of cubes: 5'
# and cubes(23) returns 'Number of cubes: many'
def cubes(count):
  # your code here
	if(count<15):
		s = "Number of cubes: " + str(count)
	else:
		s = "Number of cubes: many"
	return s


# S.2 both_ends
# Given a string s, return a string made of the first 2
# and the last 3 chars of the original string,
# so 'icecream' yields 'iceam'. However, if the string length
# is less than 3, return instead the empty string.
def both_ends(s):
  # your code here
	if(len(s)<3):
		ret = ""
	else:
		ret = s[:2]+s[-3:]
	return ret


# S.3 fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.
def fix_start(s):
  # +++your code here+++
	letter = s[0]
	return letter + s[1:].replace(letter,'*')


# S.4 MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.
def mix_up(a, b):
  # your code here
	letter1 = a[0:2]
	letter2 = b[0:2];
	return letter2+a[2:]+' '+letter1+b[2:]


# S.5 verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
	if(len(s)>=3):
		if(s[-3:]=='ing'):
			ret = s+'ly'
		else:
			ret = s+'ing'
	else:
		ret = s

  # +++your code here+++
	return ret
  


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
	if got == expected:
		prefix = ' OK '
	else:
		prefix = '  X '
	print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))
	return

# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
  print ('cubes')
  # Each line calls donuts, compares its result to the expected for that call.
  test(cubes(4), 'Number of cubes: 4')
  test(cubes(9), 'Number of cubes: 9')
  test(cubes(15), 'Number of cubes: many')
  test(cubes(99), 'Number of cubes: many')

  print
  print ('both_ends')
  test(both_ends('spring'), 'sping')
  test(both_ends('Hello'), 'Hello')
  test(both_ends('a'), '')
  test(both_ends('xyz'), 'xyxyz')

  
  print
  print ('fix_start')
  test(fix_start('babble'), 'ba**le')
  test(fix_start('aardvark'), 'a*rdv*rk')
  test(fix_start('google'), 'goo*le')
  test(fix_start('donut'), 'donut')

  print
  print ('mix_up')
  test(mix_up('mix', 'pod'), 'pox mid')
  test(mix_up('dog', 'dinner'), 'dig donner')
  test(mix_up('gnash', 'sport'), 'spash gnort')
  test(mix_up('pezzy', 'firm'), 'fizzy perm')

  print ('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
