#!/usr/bin/env python

# import modules used here -- sys is a standard one
import sys

# Defines a "triple" function that takes 2 arguments.
def triple(s, exclaim):
    """
    Returns the string 's' repeated 3 times.
    If triple is true, add exclamation marks.
    """

    result = s + s + s # can also use "s * 3" which is faster (Why?)
    if exclaim:
        result = result + '!!!'
    return result

def main():
	world = "World"
	print(world[1:4])
	print(world[1:])
	print(world[:])
	print(world[1:100])
	print(world[:-3])
	print(world[-3:])

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()