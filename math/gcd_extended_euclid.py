def gcd(a, b):
    steps = []

    while b != 0:
        q = int(a/b)
        r = a % b

        print("{} = {}*{} + {}".format(a, b, q, r))
        steps.append((a, b, q, r))
        a, b = b, r
    
    gcd = steps[-1][1]
    x, y = 0, 1

    for i in range(len(steps) - 2, -1, -1):
        step = steps[i]
        x, y = y, x - y*step[2]
        print("{} = {}({}) + {}({})".format(gcd, step[0], x, step[1], y))

    return gcd, x, y

if __name__ == "__main__":
    print(gcd(146, 32))