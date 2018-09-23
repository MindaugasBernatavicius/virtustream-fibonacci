#! /usr/bin/env python3

"""
A function that returns n-th fibonacci number
using the fast doubling method and a simple
caching mechanism
"""

__author__  = "Mindaugas Bernatavičius"
__date__    = "2018-09-22"

cache = dict()

def fibonacci(n = 0, debug = False):
    if n < 0:
        return "Negative number entered: {}. Please use numbers that above 0.".format(n)
    if n not in cache:
        if debug:
            print("[{}] NOT in cache".format(n))
        if n == 0:
            fib = 0
        elif (n < 3):
            fib = 1
        elif (n % 2 == 0):
            k = n / 2
            fib = (fibonacci(k) * (2 * fibonacci(k + 1) - fibonacci(k)))
        else:
            k = (n - 1) / 2
            fib = (fibonacci(k + 1) * fibonacci(k + 1) + fibonacci(k) * fibonacci(k))
        cache[n] = fib
    else:
        if debug:
            print("[{}] IS in cache".format(n))

    return cache.get(n)
    
if __name__ == "__main__":
    fibonacci()