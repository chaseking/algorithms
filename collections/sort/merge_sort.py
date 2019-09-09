def merge_sort(arr):
    size = len(arr)

    # Base case
    if size <= 1:
        return arr
    
    # Recursive case
    mid = size // 2
    sorted_A = merge_sort(arr[:mid])
    sorted_B = merge_sort(arr[mid:])
    
    # Combine
    a = 0
    b = 0
    output = []

    for i in range(size):
        if a == len(sorted_A):
            output.append(sorted_B[b])
            b += 1
        elif b == len(sorted_B):
            output.append(sorted_A[a])
            a += 1
        elif sorted_A[a] < sorted_B[b]:
            output.append(sorted_A[a])
            a += 1
        else:
            output.append(sorted_B[b])
            b += 1

    return output

def __merge_sort_test(arr):
    output = merge_sort(arr)
    expected_output = sorted(arr)
    print("{} --> {} (passed? {})".format(arr, output, "yes" if output == expected_output else "no"))

if __name__ == "__main__":
    __merge_sort_test([5, 4, 3, 2, 1])