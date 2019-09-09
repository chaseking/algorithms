def add(X, Y):
    # Check dimensions
    # Xshape = len(X), len(X[0])
    # Yshape = len(Y), len(Y[0])

    # if Xshape != Yshape:
    #     raise ValueError("Matrix multiplication dimension mismatch: ({} x {})+({} x {})".format(Xshape[0], Xshape[1], Yshape[0], Yshape[1]))
    
    return [[x+y for x, y in zip(X_row_i, Y_row_i)] for X_row_i, Y_row_i in zip(X, Y)]


def subtract(X, Y):
    return [[x-y for x, y in zip(X_row_i, Y_row_i)] for X_row_i, Y_row_i in zip(X, Y)]

def negate(X):
    return [[-x for x in X_row_i] for X_row_i in X]

def matmul_naive(X, Y):
    """
    Naive matrix multiplication; O(n^3) time
    """
    # Check dimensions
    Xr, Xc = len(X), len(X[0])
    Yr, Yc = len(Y), len(Y[0])

    if Xc != Yr:
        raise ValueError("Matrix multiplication dimension mismatch: ({} x {})*({} x {})".format(Xr, Xc, Yr, Yc))

    Z = [] # Z = X*Y

    for i in range(Xr):
        Z_row_i = [0] * Yc

        for j in range(Yc):
            # Z[i, j] = (ith row of X) dot (jth column of Y)
            for n in range(Xc):
                Z_row_i[j] += X[i][n] * Y[n][j]
        
        Z.append(Z_row_i)

            
    return Z