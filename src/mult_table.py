def main():
    """
    Programme that takes a number and prints out the multiplication table.
    """
    base_num = 6

    multiplication_table(base_num)


def multiplication_table(num, multiplier=10):
    """
    Takes a num and multiplier as argument.
    Default is base-ten, but can be changed using the keyword argument.
    """
    for i in range(1, multiplier+1):
        mult = num * i
        print(f"{i} * {num} = {mult}")

main()