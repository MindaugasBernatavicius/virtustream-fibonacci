#! /usr/bin/env python3

"""
A function that returns n-th fibonacci number
using the fast doubling method and a simple
caching mechanism
"""

__author__  = "Mindaugas Bernatavičius"
__date__    = "2018-09-23"

from ...models.fibonacci_generator import fibonacci


def test_negative_number():
    assert fibonacci(-1) == "Negative number entered: -1. Please use numbers that above 0."

def test_zero():
    assert fibonacci(0) == 0
    
def test_possitive_number():
    assert fibonacci(1) == 1
    
def test_large_number():
    assert fibonacci(50) == 12586269025

def test_cache_debug_when_true():  
    assert fibonacci(5, True) == 5