#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Morgan Holve
# Student ID: 2281337
# Email: holve100@mail.chapman.edu
# Course: MATH220 Fall 2018
# Assignment: CW 7
###

"""Classwork 07
This classwork introduces numpy arrays and compares their performance to
python lists.
"""

import math
import numpy as np

def gen_gaussian_list(a, b, n=1000):
    """gen_gaussian_list(a, b, n=1000)
    Generate a discrete approximation of a Gaussian function, including its
    domain and range, stored as a pair of vanilla python lists.
    
    Args:
        a (float) : Lower bound of domain
        b (float) : Upper bound of domain
        n (int, optional) : Number of points in domain, defaults to 1000.
    
    Returns:
        (x, g) : Pair of lists of floats
            x  : [a, ..., b] List of n equally spaced floats between a and b
            g  : [g(a), ..., g(b)] List of Gaussian values matched to x
    """
    dx = (b-a)/(n-1)                         # spacing between points
    x = [a + k*dx for k in range(n)]         # domain list
    
    # Local implementation of a Gaussian function
    def gauss(x):
        return (1/math.sqrt(2*math.pi))*math.exp(-x**2/2)
    
    g = [gauss(xk) for xk in x]                  # range list
    return (x, g)


def gen_gaussian_array(a, b, n=1000):
    """gen_gaussian_array(a, b, n=1000)
    Generate a discrete approximation of a Gaussian function, including it
        b (float) : Upper bound of domain
        n (int, optional) : Number of points in domain, defaults to 1000.
    
    Returns:
        (x, g) : Pair of numpy arrays of float64
            x  : [a, ..., b] Array of n equally spaced float64 between a and b
            g  : [g(a), ..., g(b)] Array of Gaussian values matched to x
    """
    x = np.linspace(a, b, num=n, endpoint=True)
    g = (1/np.sqrt(2*np.pi))*np.exp(-x**2/2)
    return (x, g)

def gen_sinc_list(a,b,n=1000):
    """
    Generate a discrete approximation of a Sinc function
    
    Args:
        a (float) : Lower bound of domain
        b (float) : Upper bound of domain
        n (int, optional) : Number of points in domain, defaults to 1000.
    
    Returns:
        (x, s) : Pair of lists of floats
            x  : [a, ..., b] List of n equally spaced floats between a and b
            s  : [s(a), ..., s(b)] List of Sinc(x) values
    """
    dx = (b-a)/(n-1)
    x = [a + k*dx for k in range(n)]
    def sin(x):
        return (math.sin(x)/x)
    s = [sin(i) for i in x]
    return (x, s)
    
def gen_sinc_array(a,b,n=1000):
    """
    Generate a discrete approximation of a Sinc function
        b (float) : Upper bound of domain
        n (int, optional) : Number of points in domain, defaults to 1000.
    
    Returns:
        (x, s) : Pair of numpy arrays of float64
            x  : [a, ..., b] Array of n equally spaced float64 between a and b
            s : [s(a), ..., s(b)] Array of Sinc(x) values
    """
    x = np.linspace(a, b, num=n, endpoint=True)
    s = np.ones_like(x)
    np.divide(np.sin(x), x, out=s, where=x!=0)
    return(x,s)

def gen_sinf_list(a,b,n=1000):
    """
    Generate a discrete approximation of a Sinf function
    
    Args:
        a (float) : Lower bound of domain
        b (float) : Upper bound of domain
        n (int, optional) : Number of points in domain, defaults to 1000.
    
    Returns:
        (x, s2) : Pair of lists of floats
            x  : [a, ..., b] List of n equally spaced floats between a and b
            s2  : [s2(a), ..., s2(b)] List of Sinf(x) values
    """
    dx = (b-a)/(n-1)
    x = [a + k*dx for k in range(1,n)]
    def sin(x):
        return (math.sin((1/x)))
    s2 = [sin(i) for i in x]
    return (x, s2)

def gen_sinf_array(a,b,n=1000):
    """
    Generate a discrete approximation of a Sinf function
        b (float) : Upper bound of domain
        n (int, optional) : Number of points in domain, defaults to 1000.
    
    Returns:
        (x, s2) : Pair of numpy arrays of float64
            x  : [a, ..., b] Array of n equally spaced float64 between a and b
            s2 : [s2(a), ..., s2(b)] Array of Sinf(x) values
    """
    x = np.linspace(a, b, num=n, endpoint=True)
    s2 = np.ones_like(x)
    np.divide(np.sin(1/x), 1, out=s2, where=x!=0)
    return(x,s2)
def main(a,b,n=1000):
    """main(a, b, n=1000)
    Main function for command line operation. Prints result of Gaussian to screen.
    
    Args:
        a (float) : Lower bound of domain
        b (float) : Upper bound of domain
        n (int, optional) : Number of points in domain, defaults to 1000.
    
    Returns:
        None
    
    Effects:
        Prints Gaussian to screen.
    """
    # You can unpack tuples as return values easily
    x, g = gen_gaussian_list(a,b,n)
    # The zip function takes two lists and generates a list of matched pairs
    for (xk, gk) in zip(x, g):
        # The format command replaces each {} with the value of a variable
        print("({}, {})".format(xk, gk))


# Protected main block for command line operation
if __name__ == "__main__":
    # The sys module contains features for running programs
    import sys
    # The sys.argv list variable contains all command line arguments
    #    sys.argv[0] is the program name always
    #    sys.argv[1] is the first command line argument, etc
    if len(sys.argv) == 4:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        n = int(sys.argv[3])
        main(a,b,n)
    elif len(sys.argv) == 3:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        main(a,b)
    else:
        print("Usage: cw07.py a b [n]")
        print("  a : float, lower bound of domain")
        print("  b : float, upper bound of domain")
        print("  n : integer, number of points in domain")
        exit(1)

