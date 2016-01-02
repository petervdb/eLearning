# Exercise 37
# Some code to review Keywords, Data Types, String Escape Sequences, String formats, Operators

# ToDo Keywords:
# and, del, not, while, as, elif, or, with, assert, pass, yield, break,except, class, exec, raise, continue, finally, is, return, lambda, try
#
# DONE Keywords:
# for, in, from, if, else, import, print, def, global
#
# ToDo DataTypes:
# None, strings, numbers, floats, lists
#
# Done DataTypes:
# True, False
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
# %s,
#
# ToDo Operator
# +, -, *, **, /, //, %, <, >, <=, >=, ==, !=, <>, ( ), [ ], { }, @, , :, . , =, ;, +=, -=, *=, /=, //=, %=, **=
#
# Done Operator
#

from time import sleep
from sys import exit

def check_user():
    global user_is_known
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
        
def start():
    print "This script contains code on how to use Keywords, Data Types, String Escape Sequences, String formats and Operators"
    check_user()
    check_user() # Just check again

# main part
user_is_known = False
start()
