def main():
    """
    Calculates the factorial of a number (n!) recursively.

    More info: https://en.wikipedia.org/wiki/Factorial
    """
    n = get_number()

    fact_result = factorial_calc(n)
    print(fact_result)

def get_number():
    """
    Asks user for an integer number.
    """
    while True:
        try:
            n = int(input("Gimme your number: "))
            break
        except ValueError:
            print("Now, don't be naughty. Only numbers allowed.")

    return n

def factorial_calc(n):
    """
    Assumes n is an integer.
    returns the result.
    """
    # Base case
    if n == 1:
        return n
    
    # Recursively going through n-1
    result = n * factorial_calc(n-1)

    return result

main()



"""
Iterative factorial for educational purposes:

def factorial(number):
    product = 1
    for i in range(1, number + 1):
        product *= i
    return product
print(factorial(5))
"""