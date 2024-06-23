import math
def Interest(p,r,t):
    #A = Pe^(rt) formula to calculate compound interest

    p = float(p)
    r = float(r)
    t = float(t)
    e = math.exp(r * t)

    #calculation
    a = p * e  # future value of your investment

    return a
