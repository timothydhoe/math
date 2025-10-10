def main():
    """
    A very useful function that flips a positive or negative integer.
    prints out the result
    """
    n = get_number()

    flip_number(n)

def get_number():
    """
    Take a user input. Assumes the input is an integer.
    Returns the value.
    """
    while True:
        try:
            n = int(input("What's your number? "))
            break
        except ValueError:
            print("Only positive and negative integers are allowed.")

    return str(n)

def flip_number(n):
    sign = False
    flipped = ""
    for i in range(len(n)-1, -1, -1):
        if n[i] == "-":
            sign = True   
            continue 
        flipped += n[i]
    if sign:
        flipped = int(flipped) * -1

    print(flipped)

main()