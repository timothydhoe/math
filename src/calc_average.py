L = []


def main():
    """
    Programme that calculates the average of an indefinite list of integers.
    """
    user_list()

    average = calc_average(L)
    print(f"The average of your list is: {average}")


def user_list():
    """
    Asks user for input.
    Adds integer to a global list.
    """
    user_L = ""
    counter = 1
    print("\n")
    print(f"=== Let's calculate the average ===")
    print(f"     ~~ Press 'q' to exit ~~")
    print(f"               ~~~~")
    print("\n")
    while True:
        user_L = input(f"{counter}. Give a number: ")
        if user_L == 'q':
            print("\n")
            break
        try:
            L.append(int(user_L))
        except ValueError:
            print("No! Only integers allowed in this list!")
            print("Try again!")
            print("\n")  


def calc_average(L):
    """
    Takes a list of integers and calculates the average.
    Returns "NaN" with an empty list, else Returns average value
    """
    result = 0

    if not L:
        return "NaN"
    
    for num in L:
        result += num
    result = result / len(L)

    return result


main()