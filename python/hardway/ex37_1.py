# Exercise 37
# Some code to review Keywords, Data Types, String Escape Sequences, String formats, Operators

# ToDo Keywords:
# and, del, not, as, or, with, assert, pass, yield, break,except, class, exec, raise, continue, finally, is, lambda, try
#
# DONE Keywords:
# for, in, from, if, else, import, print, def, global, while, sleep, elif
#
# ToDo DataTypes:
# None, lists
#
# Done DataTypes:
# True, False, strings, numbers, floats
#
# ToDo String Escape Seequences
# \\, \', \", \a, \b, \f, \n, \r, \t, \v
#
# Done String Escape Seequences
#
#
# ToDo String Formats
# %i, %o, %u, %x, %e, %E, %f, %F, %g, %G, %c, %r, %%
#
# Done String Formats
# %s, %d
#
# ToDo Operator
# +, -, *, **, /, //, %, <, >, <=, >=, ==, !=, <>, ( ), [ ], { }, @, , :, . , =, ;, +=, -=, *=, /=, //=, %=, **=
#
# Done Operator
# +, ==

from time import sleep
from sys import exit
import sqlite3
import random

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def check_user():
    global user_is_known, you
    if user_is_known == False:
        print "We need to verify who you are before you can use this program."
        you = raw_input("So, tell me, who are you? ")
        youlow = you.lower()
        # print youlow
        print ("Let's check the database if user %s exists ..." % you)
        # Count to 10 simulating database search
        for i in range(0, 10):
                sleep(0.1)
                print("."),
        print " "
        print ("Haha, I found you. OK %s, we can continue with this program" % you)
        user_is_known = True
    else:
        print "Yes, you are already known by the system"

def check_age(age_is_known):
    if age_is_known == False:
        print "It look like you're age is unknown by the system."
        your_age = raw_input("So, tell me, how old are you? ")
        while is_number(your_age) == False:
            print "Don't you know the difference between a string and a number?"
            your_age = raw_input("Let's try again, how old are you? ")
    else:
        print("Your age is known in the database. Great!")
    return(int(your_age))

def math_test():
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    total = num1 + num2
    guess1 = int(raw_input("What is: %d + %d ?" % (num1, num2)))
    if (total == guess1):
        print "Yup!"
    else:
        print "Hahaha."
def start():
    global user_is_known, age_is_known, you
    print "This script contains code on how to use Keywords, Data Types, String Escape Sequences, String formats and Operators"
    check_user()
    check_user() # Just check again
    age_user = check_age(age_is_known)
    if age_user < 18:
        print "Sorry %s, you should be at least 10 years old to use this sophisticated program." % you
        math_test()
        exit(1)
    elif age_user < 21:
        print "I hope you are smart enough to use this program."
        print "Let's perform a math test to verify this ..."
        math_test()
    elif age_user > 99:
        print "Haha, are you realy that old %s. Let's check this out." % you
        math_test()
    else:
        print"So, %s you are %d years old." % (you, age_user)
        print" We are going to perform some tests to verify that you are realy that old"
        math_test()
# main part
user_is_known = False
age_is_known = False
you = "unknown"
conn = sqlite3.connect('sqlite_example1.db')
start()
