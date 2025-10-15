"""
Programme that finds all the prime numbers less than or equal to a given integer n by Eratosthenes's method.

A prime number is a natural number that has exactly two distinct natural number divisors: the number 1 and itself.

source: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""

def main():
    n = get_number()

    prime_num = prime_number(n)
    print(f"All prime numbers below {n} are:")
    for i in prime_num:
        print(f"{i}, ", end="")
    print()


def prime_number(n):
    p = 2
    # Create list of consecutive integers from 2 through n: (2, 3, 4, ... n)
    L = []
    for i in range(2, n+1):
        L.append(i)

    # Set smallest prime number
    while True:
        # 3. enumerate the multiples of p by couting in increments of p from 2p
        L = enumerate(p, L)

        # 4. Find smallest number greater than p, that is not marked.
        #.   if no such number, STOP else: p = new number
        p = find_greater_num(p, L)
        
        if p is None or p >= n:
            break

    return L


def get_number():
    # TODO: DON'T ACCEPT NUMBER BELOW 2
    while True:
        try:
            user_num = int(input("Number: "))
            if user_num <= 2:
                print("Please provide a number bigger than 2.")
                continue
            return user_num
        except ValueError:
            print("Please provide a number bigger than 2.")

def enumerate(p, L):
    for i in L[:]:      # Create copy of the list, to avoid index issues
        if i == p:
            continue
        elif i % p == 0:
            L.remove(i)
    return L

def find_greater_num(p, L):
    for i in L:
        if i == p:
            continue
        elif i > p:
            return i
    return None


if __name__ == '__main__':
    main()