def main():
    """
    programme that calculates the Greatest Common Divisor(gcd)
    between two positive integers.

    more info: https://en.wikipedia.org/wiki/Euclidean_algorithm
    """
    x = ask_user_number()
    y = ask_user_number()
    
    result = gcd(x, y)
    print(f"The greatest common dividor between "
           f"{x} and {y} is {format(result, ".2f")}")


def ask_user_number():
    """
    Ask the user for positive integers
    """
    try: 
        value = int(input("Your first number: "))
    except ValueError:
        print("Please enter a positive integer.")
    except ZeroDivisionError:
        print("Can't divide zero or divide by zero.")
    return value

def gcd(x, y):
    product = x * y
    least_common_mult = lcm(x, y)
    return product / least_common_mult

def lcm(x,y):
    """
    Least Common Multiple
    """
    for i in range(1, 11):
        one = x * i
        for j in range(1, 11):
            two = y * j
            if one == two:
                return one


main()