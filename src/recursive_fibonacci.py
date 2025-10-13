"""
Test with fibonacci to explain recursive calls and returns.

Much of the code's output is to show of the recursive function.


Note: this is not the best integration of fibonacci, but rather used as explanation to recursive calls.
It's weakness is that it repeats the same calculations over and over. So yeah, don't use large numbers... you'll be waiting for millions of years...

"""

def fibonacci(Number):
    print('fibonacci(%s) called.' % (Number))
    if Number == 1 or Number == 2:
        # BASE CASE
        print('call to fibonacci(%s) returning 1.' % (Number))
        return 1
    else:
        # RECURSIVE CASE
        print('Calling fibonacci(%s) and fibonacci(%s).' % (Number - 1, Number - 2))
        result = fibonacci(Number - 1) + fibonacci(Number - 2)
        print('call to fibonacci(%s) returning (%s)' % (Number, result))
        return result

print(fibonacci(10))


"""
Iterative fibonacci

A faster implementation of fibonacci.
"""

def fibonacci(nthNumber):
    a, b, = 1, 1
    print('a = %s, b = %s' % (a, b))
    for i in range(1, nthNumber):
        a, b = b, a + b # Get the next Fibonacci number
        print('a = %s, b = %s' % (a, b))
    return a

print(fibonacci(10))