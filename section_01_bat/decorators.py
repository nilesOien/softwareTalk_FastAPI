#!/usr/bin/env python

import time

# Introducing the concept of Python decorators.
#
# "timer" is a function that takes a function as an
# argument, and then wraps that function so that we
# print how much time elapsed during the function call.
# We can then "decorate" other functions with this by
# preceeding the function definition with "@timer"
def timer(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()
        # As an aside, the "func.__name__" below is a
        # "dunder" (short for "double underscore") variable.
        print(f"{func.__name__} took {t2-t1} seconds")
        return
    return wrapper

# Define two functions that are "decorated" with timer.
@timer
def first_function():
    time.sleep(1.3)
    return

@timer
def second_function():
    time.sleep(0.5)
    return

# The main program simply calls these decorated functions.
first_function()
second_function()
print("Normal termination")

# This prints something like :
# first_function took 1.3013339042663574 seconds
# second_function took 0.5005264282226562 seconds
# Normal termination

quit()

