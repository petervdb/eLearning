# Exercise 37
# Some code to review Keywords, Data Types, String Escape Sequences, String formats, Operators

# ToDo Keywords:
# and, del, not, as, elif, or, with, assert, pass, yield, break,except, class, exec, raise, continue, finally, is, lambda, try
#
# DONE Keywords:
# for, in, from, if, else, import, print, def, global, while
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
# %d, %i, %o, %u, %x, %e, %E, %f, %F, %g, %G, %c, %r, %%
#
# Done String Formats
# %s, %d
#
# ToDo Operator
# +, -, *, **, /, //, %, <, >, <=, >=, ==, !=, <>, ( ), [ ], { }, @, , :, . , =, ;, +=, -=, *=, /=, //=, %=, **=
#
# Done Operator
#

from time import sleep
from sys import exit

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

def start():
    global user_is_known, age_is_known, you
    print "This script contains code on how to use Keywords, Data Types, String Escape Sequences, String formats and Operators"
    check_user()
    check_user() # Just check again
    age_user = check_age(age_is_known)
    print"So, %s you are %d years old." % (you, age_user)

# main part
user_is_known = False
age_is_known = False
you = "unknown"
start()
