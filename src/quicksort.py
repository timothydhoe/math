"""
Quicksort programme.
"""


def main():
    arr = [10, 5, 2, 6, 3, 7, 1, 4, 9, 0, 8]   # change the array
    print(quicksort(arr))


def quicksort(array):
    """
    Takes an unsorted array
    Returns a sorted array
    """
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

if __name__ == '__main__':
    main()