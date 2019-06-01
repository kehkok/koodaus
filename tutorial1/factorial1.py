"""
This module consists of basic factorial, exponential factorial and taylor
series of sin functions
"""

import math


def factorial(n):
    """Compute basic factorial function
        
        Parameters
        ----------
        n  : integer
        Specifies the number to be factorial
        
        Returns
        -------
        Float value of the product for all n
    """
    if n == 0: 
        return 1.0 
    else: 
        return float(n) * factorial(n-1) 


def exp_factorial(n):
    """Compute exponential of factorial
        
        Parameters
        ----------
        n  : integer
        Specifies the number to be exponentially factorial
        
        Returns
        -------
        float value of the product for all n
    """
    return [1.0/factorial(i) for i in range(n)] 


def sin_factorial(n):
    """Compute taylor series of sin for a list
        
        Parameters
        ----------
        n  : integer
        Specifies the number to be taylor of sin
        
        Returns
        -------
        list of float values
    """
    res = [] 
    for i in range(n): 
        if i % 2 == 1: 
           res.append((-1)**((i-1)/2)/float(factorial(i))) 
        else: 
           res.append(0.0) 
    return res 


def func_cos(x, n):
    """Estimate the value of cos(x) using a Taylor Series

        Parameters
        ----------
        x  : integer
        Specifies the number of x value of cos function
        n  : integer
        Specifies the number to be taylor of sin

        Returns
        -------
        Estimate of factorial of n for cox(x) value
    """
    cos_approx = 0
    for i in range(n):
        coef = (-1)**i
        num = x**(2*i)
        denom = math.factorial(2*i)
        cos_approx += ( coef ) * ( (num)/(denom) )
    
    return cos_approx


def benchmark():
    """Benchmark function
       
       Returns
       -------
       None
    """
    sum_ef = sum(exp_factorial(500))

    print("Sum of exponential factorial is {:.6f}.".format(sum_ef))

    sum_sin = sum(sin_factorial(500))

    print("Sum of sin factorial is {:.6f}.".format(sum_sin))

    print("Estimated of cos(x) value is {:.3f}".format(func_cos(5, 3)))


if __name__ == '__main__':
    """Main function
        
    """
    print ("Start...")

    benchmark()

    print ("End...")
