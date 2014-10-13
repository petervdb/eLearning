#!/usr/bin/python3
# some experiments with functions

def my_values(value1):
	print ("My_values    : Value of value1 in function my_values: %s" % value1)
	print ("My_values    : Value of value2 in function my_values: %s" % value2)
	print ("==========================================================")

def my_values2(newvalue):
	print ("My_values2   : Value of newvalue in function my_values2: %s" % newvalue) # newvalue will be lost when we return to the main part
	print ("My_values2   : Value of value1 in function my_values2: %s" % value1)
	print ("My_values2   : Value of value2 in function my_values2: %s" % value2)
	print ("==========================================================")

def add10(x):
	print ("Add10 def    : Value of x: %s" % x)
	x = x + 10
	print ("Add10 def    : Value of x: %s" % x)
	return(x)

def add100():
	print ("Add100 def   : I am in add100 part and value1 is: %s" % value1)
	print ("Add100 def   : I am in add100 part and value2 is: %s" % value2)
	print ("==========================================================")
	# value1 = value1 + 100 # This generates an error message

value1 = 10
value2 = 20
print ("Main def     : This is a script for testing functions in Python3.")
print ("Main def     : I am in the main part and value1 is: %s" % value1)
print ("Main def     : I am in the main part and value2 is: %s" % value2)
print ("==========================================================")

my_values(value1)
my_values2(value1)
# This generates an error message
# print ("Main def: Value of newvalue in main part: %s" % newvalue)

print ("Main def     : I am in the main part and value1 is: %s" % value1)
print ("Main def     : I am in the main part and value2 is: %s" % value2)
print ("==========================================================")

newvalue2 = add10(value1)
print ("Main def     : I am in the main part and newvalue2 is: %s (it should be value1 + 10) " % newvalue2)
print ("==========================================================")

print ("Main def     : Now adding 10 to both value1 and value2")
value1 = value1 + 10
value2 = value2 + 10
print ("Main def     : I am in the main part and value1 is: %s" % value1)
print ("Main def     : I am in the main part and value2 is: %s" % value2)
print ("==========================================================")
add100()

print ("Main def     : I am in the main part and value1 is: %s" % value1)
print ("Main def     : I am in the main part and value2 is: %s" % value2)
print ("==========================================================")

