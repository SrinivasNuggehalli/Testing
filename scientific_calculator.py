# TDD Exercise Program
# 
# Author: Srinivas Nuggehalli Venkatesh
# 
# Description : This file contains the implementation of a scientific calculator using Python. 
# The calculator provides functions for various mathematical operations, including:
#
# Basic Trigonometric Functions: sin, cos, tan
# Inverse Trigonometric Functions: asin, acos, atan
# Hyperbolic Functions: sinh, cosh, tanh
# Exponential and Logarithmic Functions: exp, log
# Square Root Function: sqrt
# 
# Each function checks for valid numeric input and handles errors appropriately:
# TypeError for non-numeric inputs.
# ValueError for inputs outside the valid range (e.g., log of a negative number, or asin of a value outside [-1, 1])

import math

def check_numeric_input(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a numeric value")
    return x

def sin(x):
    x = check_numeric_input(x)
    return math.sin(math.radians(x))

def cos(x):
    x = check_numeric_input(x)
    return math.cos(math.radians(x))

def tan(x):
    x = check_numeric_input(x)
    return math.tan(math.radians(x))

def sqrt(x):
    x = check_numeric_input(x)
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number")
    return math.sqrt(x)

def log(x):
    x = check_numeric_input(x)
    if x <= 0:
        raise ValueError("Cannot compute logarithm of zero or a negative number")
    return math.log(x)

def exp(x):
    x = check_numeric_input(x)
    return math.exp(x)

def asin(x):
    x = check_numeric_input(x)
    if x < -1 or x > 1:
        raise ValueError("Input must be in the range [-1, 1]")
    return math.asin(x)

def acos(x):
    x = check_numeric_input(x)
    if x < -1 or x > 1:
        raise ValueError("Input must be in the range [-1, 1]")
    return math.acos(x)

def atan(x):
    x = check_numeric_input(x)
    return math.atan(x)

def sinh(x):
    x = check_numeric_input(x)
    return math.sinh(x)

def cosh(x):
    x = check_numeric_input(x)
    return math.cosh(x)

def tanh(x):
    x = check_numeric_input(x)
    return math.tanh(x)
