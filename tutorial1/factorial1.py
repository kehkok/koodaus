"""
This module consists of basic factorial, exponential factorial and taylor
series of sin functions
"""


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


if __name__ == '__main__':
    """Main function
        
    """
    print ("Start...")

    benchmark()

    print ("End...")
