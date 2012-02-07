'''
Each new term in the Fibonacci sequence is generated by adding the previous two 
terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed 
four million, find the sum of the even-valued terms.

Created on 2012-02-03

@author: aparkin
'''

def prob2(limit):
    '''
    Solution to problem #2.  Sum all the even fibonacci numbers strictly less 
    than limit.
    
    @type limit: int
    
    @return: the sum of all fibonacci numbers less than limit
    @rtype: int 
    '''
    fib1 = 1
    fib2 = 2
    curfib = fib1 + fib2
    total = fib2
    
    while curfib < limit:
        if curfib % 2 == 0:
            total += curfib
            
        fib1 = fib2
        fib2 = curfib
        curfib = fib1 + fib2
    
    return total

if __name__ == "__main__":
    print prob2(4000000)
