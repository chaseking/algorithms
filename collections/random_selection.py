import random

def random_select(arr, order_statistic, low=0, high=-1):
    """
    An alteration of the QuickSort "partition around pivot" algorithm to provide a linear O(n) runtime to
    the array selection problem. This method returns the element in the order_statistic position if the
    array were sorted (i.e. the "order_statistic th lowest element"). Useful for computing the median.

    Note: array contents are modified.
    Note: order_statistic starts at 0. (e.g. if order_statistic=0, then the minimum element is returned)
    """
    if high == -1: high = len(arr)
    size = high - low

    # Base case
    if size <= 1:
        return arr[low]
    
    # Recursive case
    # Partition around pivot
    pivot_index = int(random.uniform(low, high))    
    pivot = arr[pivot_index]
    
    # Move pivot to first spot
    arr[low], arr[pivot_index] = arr[pivot_index], arr[low]
    pivot_index = low
    i = low + 1 # arr[low+1], ..., arr[i-1] are all strictly less than the pivot

    for j in range(low + 1, high):
        # arr[i], ... arr[j] are all >= pivot
        if arr[j] < pivot:
            # We've encountered an element less than the pivot, so swap it with the element at index i
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    # Move pivot into correct location
    arr[pivot_index], arr[i - 1] = arr[i - 1], arr[pivot_index]
    pivot_index = i - 1

    # print("arr={} --> {}, low={}, high={}, order_stat={}, pivot={} [{}]".format(arr, arr[low:high], low, high, order_statistic, pivot, pivot_index))

    if order_statistic < pivot_index: # The element we are searching for is in the subarray to the LEFT of pivot
        return random_select(arr, order_statistic, low=low, high=pivot_index)
    elif order_statistic > pivot_index: # The element we are searching for is in the subarray to the RIGHT of pivot
        return random_select(arr, order_statistic, low=(pivot_index+1), high=high)
    else: # We have found the element
        return pivot

def random_select_median(arr):
    n = len(arr)
    
    if n % 2 == 0:
        # Even; compute average of two middle elements at indices (n/2)-1 and n/2
        mid_left = random_select(arr, order_statistic=(n/2 - 1))
        mid_right = random_select(arr, order_statistic=(n/2))

        return (mid_left + mid_right) / 2
    else:
        # Odd; there is a unique middle element at index floor(n/2)
        return random_select(arr, order_statistic=int(len(arr) / 2))

def __random_select_test(arr, order_statistic):
    expected_output = sorted(arr)[order_statistic]
    output = random_select(arr[:], order_statistic)
    print("{} (order_statistic={}) --> {} (passed? {})".format(arr, order_statistic, output, "yes" if output == expected_output else "no"))

if __name__ == "__main__":
    __random_select_test([5, 4, 3, 2, 1], 0)
    __random_select_test([5, 4, 3, 2, 1], 3)
    __random_select_test([1, 2, 7, 3, 6, 4, 5], 3)