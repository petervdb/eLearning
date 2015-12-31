# Exercise 37
# Some code to review Keywords, Data Types, String Escape Sequences, String formats, Operators
# ToDo
# Keywords:
# and, del, from, not, while, as, elif, global, or, with, assert, else, if
# pass, yield, break,except, import, print, class, exec, in, raise, continue
# finally, is, return, def, for, lambda, try
#
# DataTypes:
# True, False, None, strings, numbers, floats, lists
#
# String Escape Seequences
# \\, \', \", \a, \b, \f, \n, \r \t, \v
#
# String Formats
# %d, %i, %o, %u, %x, %e, %E, %f, %F, %g, %G, %c, %r, %s, %%
#
# Operator
# +, -, *, **, /, //, %, <, >, <=, >=, ==, !=, <>, ( ), [ ], { }, @, , :, . , =, ;, +=, -=, *=, /=, //=, %=, **=


from time import sleep

def check_user():
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
        
def start():
        print "This script contains code on how to use Keywords, Data Types, String Escape Sequences, String formats and Operators"
        check_user()

# main part

start()
