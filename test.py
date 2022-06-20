def rational(n, d):
    return [n, d]

def numer(x):
    return x[0]

def denom(x):
    return x[1]

def mul_rational(x, y):
    return rational(numer(x) * numer(y), denom(x) * denom(y))
