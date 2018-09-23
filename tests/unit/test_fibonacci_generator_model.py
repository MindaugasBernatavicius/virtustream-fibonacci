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

def test_cache_debug_when_true(capsys):
    result = fibonacci(5, True)
    out, err = capsys.readouterr()
    assert result == 5 
    assert out == "[5] IS in cache\n"
    
def test_cache_debug_when_false(capsys):
    result = fibonacci(5)
    out, err = capsys.readouterr()
    assert result == 5 
    assert out == ""