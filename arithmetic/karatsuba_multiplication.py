from math import ceil, floor, log10

def karatsuba(x, y):
    # Preprocessing: make sure x, y, are both positive
    if x < 0 and y < 0:
        return karatsuba(-x, -y)
    elif x < 0:
        return -karatsuba(-x, y)
    elif y < 0:
        return -karatsuba(x, -y)

    # Trivial case (avoids log errors)
    if x == 0 or y == 0:
        return 0

    # Base case: both x and y are single-digit numbers
    if x < 10 and y < 10:
        return x * y

    digits_x = floor(log10(x)) + 1
    digits_y = floor(log10(y)) + 1
    digits = max(digits_x, digits_y)
    
    mid = ceil(digits / 2)
    mid_div = 10 ** mid

    a = x // mid_div
    b = x % mid_div
    c = y // mid_div
    d = y % mid_div

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a + b, c + d) - ac - bd
    result = int((10**(mid*2))*ac + (10**mid)*ad_bc + bd)

    # Uncomment this line for debugging:
    # print("mid={}, x={}, y={}, a={}, b={}, c={}, d={}, x*y={}, ac={}, bd={}, ad+bc={}, result={}".format(mid, x, y, a, b, c, d, x*y, ac, bd, ad_bc, result))

    return result


def __karatsuba_test(x, y):
    print("{} * {} = {}    Expected: {}".format(x, y, karatsuba(x, y), x*y))

if __name__ == "__main__":
    __karatsuba_test(100, 100)
    __karatsuba_test(1234, 5678)
    __karatsuba_test(-517, 31)