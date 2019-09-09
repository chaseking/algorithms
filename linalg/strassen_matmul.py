from matrix_helpers import add, subtract

def strassen_matmul(X, Y):
    # Check dimensions
    Xr, Xc = len(X), len(X[0])
    Yr, Yc = len(Y), len(Y[0])

    if Xc != Yr:
        raise ValueError("Matrix multiplication dimension mismatch: ({} x {})*({} x {})".format(Xr, Xc, Yr, Yc))

    if Xr == 1 and Xc == 1 and Yr == 1 and Yc == 1:
        return [[X[0][0] * Y[0][0]]]

    A, B, C, D = __get_quadrants(X)
    E, F, G, H = __get_quadrants(Y)

    P1 = strassen_matmul(A, subtract(F, H))
    P2 = strassen_matmul(add(A, B), H)
    P3 = strassen_matmul(add(C, D), E)
    P4 = strassen_matmul(D, subtract(G, E))
    P5 = strassen_matmul(add(A, D), add(E, H))
    P6 = strassen_matmul(subtract(B, D), add(G, H))
    P7 = strassen_matmul(subtract(A, C), add(E, F))

    Z1 = add(subtract(add(P5, P4), P2), P6)
    Z2 = add(P1, P2)
    Z3 = add(P3, P4)
    Z4 = subtract(subtract(add(P1, P5), P3), P7)

    Z_top = [left_row_i + right_row_i for left_row_i, right_row_i in zip(Z1, Z2)]
    Z_bottom = [left_row_i + right_row_i for left_row_i, right_row_i in zip(Z3, Z4)]

    return Z_top + Z_bottom


def __get_quadrants(X):
    rm = len(X) // 2
    cm = len(X[0]) // 2

    A = [row[:cm] for row in X[:rm]] # Upper left
    B = [row[cm:] for row in X[:rm]] # Upper right
    C = [row[:cm] for row in X[rm:]] # Lower left
    D = [row[cm:] for row in X[rm:]] # Lower right

    return A, B, C, D

def __strassen_matmul_test(X, Y):
    from matrix_helpers import matmul_naive
    product = strassen_matmul(X, Y)
    expected_product = matmul_naive(X, Y)
    passed = product == expected_product
    print("{}*{} --> {} (passed? {})".format(X, Y, product, "yes" if passed else "no"))
    if not passed:
        print("  Expected product: {}".format(expected_product))

if __name__ == "__main__":
    __strassen_matmul_test([[1, 0], [0, 1]], [[1, 2], [3, 4]])
    __strassen_matmul_test([[4, 3], [2, 1]], [[1, 2], [3, 4]])