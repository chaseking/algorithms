import random

def quicksort(arr, pivot_choice="random", low=0, high=-1):
    """
    Uses the QuickSort algorithm to sort the given array from indices low (inclusive) to high (exclusive).
    Ignores sorting all other elements.
    """
    if high == -1: high = len(arr)
    size = high - low

    # Base case
    if size <= 1:
        return 0
    
    # Recursive case
    # Choose pivot
    if pivot_choice == "random":
        pivot_index = int(random.uniform(low, high))
    elif pivot_choice == "first":
        pivot_index = low
    elif pivot_choice == "last":
        pivot_index = high - 1
    elif pivot_choice == "median_of_three":
        a = low
        b = low + int(size / 2)
        c = high - 1

        if arr[a] > arr[b]:
            if arr[c] > arr[a]: pivot_index = a # c > a > b
            elif arr[b] > arr[c]: pivot_index = b # a > b > c
            else: pivot_index = c # a >= c > b
        else: # b >= a
            if arr[a] > arr[c]: pivot_index = a # b >= a > c
            elif arr[c] > arr[b]: pivot_index = b # c > b >= a
            else: pivot_index = c # b >= c >= a

    else:
        raise Exception("Invalid pivot_choice parameter: {}".format(pivot_choice))
    
    # Partition around pivot
    pivot = arr[pivot_index]
    
    # Move pivot to first spot
    arr[low], arr[pivot_index] = arr[pivot_index], arr[low]
    pivot_index = low
    i = low + 1 # arr[low+1], ..., arr[i-1] are all strictly less than the pivot
    comp = 0

    for j in range(low + 1, high):
        # arr[i], ... arr[j] are all >= pivot
        comp += 1
        if arr[j] < pivot:
            # We've encountered an element less than the pivot, so swap it with the element at index i
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    # Move pivot into correct location
    arr[pivot_index], arr[i - 1] = arr[i - 1], arr[pivot_index]

    n_comparisons_left = quicksort(arr, pivot_choice=pivot_choice, low=low, high=i-1)
    n_comparisons_right = quicksort(arr, pivot_choice=pivot_choice, low=i, high=high)
    
    return n_comparisons_left + n_comparisons_right + (size - 1) # We have done (size - 1) comparisons with our j loop

def __quicksort_test(arr, pivot_choice="random"):
    expected_output = sorted(arr)
    output = arr[:]
    n_comparisons = quicksort(output, pivot_choice=pivot_choice)
    print("{} --> {} (n_comp={}, pivot_choice={}) (passed? {})".format(arr, output, n_comparisons, pivot_choice, "yes" if output == expected_output else "no"))

if __name__ == "__main__":
    __quicksort_test([5, 4, 3, 2, 1], pivot_choice="random")
    __quicksort_test([5, 4, 3, 2, 1], pivot_choice="first")
    __quicksort_test([5, 4, 3, 2, 1], pivot_choice="last")
    __quicksort_test([5, 4, 3, 2, 1], pivot_choice="median_of_three")
    __quicksort_test([1, 8, 2, 7, 3, 6, 4, 5])