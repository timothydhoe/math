"""
Variation(n, k) function that calculates the number of variations of chosen objects (n) in groups of (k).

This programme will calculate all possible orders of (k) objects from (n).
"""

def main():
    n = 5
    k = 2

    outcome = variation(n, k)
    print(outcome)

def variation(n, k):
    result = 1 
    for i in range(k):
        result *= (n - i)
    return result

if __name__ == "__main__":
    main()

    