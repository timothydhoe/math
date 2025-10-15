"""
Programme that finds all the prime numbers less than or equal to a given integer n by Eratosthenes's method.

A prime number is a natural number that has exactly two distinct natural number divisors: the number 1 and itself.

source: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""

def main():
    pass

def prime_number(n):
    pass
    # 1. Create a list of consecture integers from 2 through n: (2, 3, 4, ... n)

    # 2. p = 2 -> smallest prime number

    # 3. enumearte the multiples of p by couting in increments of p from 2p to n
    #    Mark them in a list without p (2p, 3p, 4p ...)

    # 4. Find smallest number greater than p, that is not marked.
    #    if no such number, STOP
    #    else, let p = new number

    # 5.  repeat step 3. enumerate

    # 6. When algortihmm terminates, the number remaining not marked in the list are all the primes below n.

def get_number():
    pass

main()