def closest_pair_naive(points):
    n = len(points)
    best_pair = None
    best_pair_dist = 0
    
    for i in range(n):
        for j in range(i+1, n):
            p = points[i]
            q = points[j]
            d = dist(p, q)
            if best_pair is None or d < best_pair_dist:
                best_pair = (p, q)
                best_pair_dist = d
    
    return best_pair, best_pair_dist

def closest_pair(points):
    # Sort points
    points_sorted_x = sorted(points, key=lambda p: p[0])
    points_sorted_y = sorted(points, key=lambda p: p[1])

    return __closest_pair_recursive(points, points_sorted_x, points_sorted_y)

def __closest_pair_recursive(points, points_sorted_x, points_sorted_y):
    n = len(points)

    # Base case
    if n <= 1:
        return None, -1
    else if n == 2:
        p, q = points
        return (p, q), dist(p, q)
    
    # Recursive case
    # TODO
    mid_x_index = n // 2
    mid_x_value = points_sorted_x[mid_x_index]
    left_half = points_sorted_x[:mid_x_index]
    right_half = points_sorted_x[mid_x_index:]
    (p1, q1), d_left = closest_pair_recurse(left_half)

def dist(p, q):
#     return np.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)
    return (p[0] - q[0])**2 + (p[1] - q[1])**2

def __test_closest_pair(points, expected_output):
    output = closest_pair(points)
    assert output == expected_output, "Points: {} | Output: {} | Expected output: {}".format(points, output, expected_output)

if __name__ == "__main__":
    pass