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

def taylor_sin(n):
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
    taylor_exp(500) 
    taylor_sin(500) 

if __name__ == '__main__':
    """Main function
        
    """
    benchmark() 
