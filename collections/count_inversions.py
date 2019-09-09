def count_inversions(arr):
    """
    Count the number of inversions in an array.
    An inversion is a pair (i, j) such that i < j and A[i] > A[j].
    This can be thought of as a discrete measure of how close an array is to being sorted. (n_inversions = 0 ==> array is sorted)
    """
    return count_inversions_sort(arr)[0]

def count_inversions_sort(arr):
    size = len(arr)

    # Base case
    if size <= 1:
        return 0, arr
    
    # Recursive case
    mid = size // 2
    left_inversions, sorted_A = count_inversions_sort(arr[:mid])
    right_inversions, sorted_B = count_inversions_sort(arr[mid:])
    
    # Combine (and also count split inversions)
    a = 0
    b = 0
    split_inversions = 0
    sorted_arr = []

    for i in range(size):
        if a == len(sorted_A):
            sorted_arr.append(sorted_B[b])
            b += 1
        elif b == len(sorted_B):
            sorted_arr.append(sorted_A[a])
            a += 1
        elif sorted_A[a] < sorted_B[b]:
            sorted_arr.append(sorted_A[a])
            a += 1
        else:
            sorted_arr.append(sorted_B[b])
            b += 1

            # If this is reached, then the current element in A is LARGER than the current element in B.
            # Moreover, since A and B are both sorted (ascending), we know that all elements in A after the current element are also greater than the current element in B.
            # Thus, the number of inversions involving the current element in B is the number of elements remaining in A
            split_inversions += len(sorted_A) - a

    return (left_inversions + right_inversions + split_inversions), sorted_arr

def __count_inversions_test(arr, expected_inversions):
    inversions = count_inversions(arr)
    print("{} --> {} (passed? {})".format(arr, inversions, "yes" if inversions == expected_inversions else "no"))

if __name__ == "__main__":
    __count_inversions_test([1, 3, 5, 2, 4, 6], 3)
    __count_inversions_test([6, 5, 4, 3, 2, 1], 15) # If array is sorted descending: n_inversions = (n-1)+(n-2)+(n-3)+...+2+1 = n(n-1)/2