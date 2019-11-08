def deterministic_select(arr, order_statistic, low=0, high=-1):
    """
    

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
    # TODO
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
        return deterministic_select(arr, order_statistic, low=low, high=pivot_index)
    elif order_statistic > pivot_index: # The element we are searching for is in the subarray to the RIGHT of pivot
        return deterministic_select(arr, order_statistic, low=(pivot_index+1), high=high)
    else: # We have found the element
        return pivot

def __deterministic_select_test(arr, order_statistic):
    expected_output = sorted(arr)[order_statistic]
    output = deterministic_select(arr[:], order_statistic)
    print("{} (order_statistic={}) --> {} (passed? {})".format(arr, order_statistic, output, "yes" if output == expected_output else "no"))

if __name__ == "__main__":
    __deterministic_select_test([5, 4, 3, 2, 1], 0)
    __deterministic_select_test([5, 4, 3, 2, 1], 3)
    __deterministic_select_test([1, 2, 7, 3, 6, 4, 5], 3)