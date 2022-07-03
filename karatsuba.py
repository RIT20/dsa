import math

def karatsuba(x, y):
    if len(str(x)) and len(str(y)):
        return x*y
    n = max(len(str(x)), len(str(y)))
    m = math.ceil(n/2)
    r = 10                                               #radix r= 2, 10
    x_h =  math.floor(x/10**m)
    x_l = x % 10**m

    y_h = math.floor(y/10**m)
    y_l = y % 10**m

    z0 = karatsuba(x_l, y_l)
    z2 = karatsuba(x_h, y_h)
    z1 = karatsuba(x_h + x_l, y_h + y_l) - z0 - z2

    return int(z2*(m**(2*m)) + (z1 * (r**m)) + z0)

# print(karatsuba(1098765, 456789))
# print(karatsuba(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627))

# time complexity = 3(T(n/2)) + theta(n) ==>theta(n^log3) = theta(n^1.58)
# (if dividing it in three parts, for four parts, the complexity will be n^2)
#  link to understand code = https://brilliant.org/wiki/karatsuba-algorithm/
# for algo..., MIT lectures


# division--