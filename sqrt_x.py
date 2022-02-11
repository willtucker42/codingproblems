# Given a non-negative integer x, compute and return the square root of x.
# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
# Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

def mySqrt(self, x):
    if x < 2:
        if x == 0:
            return 0
        if x == 1:
            return 1
    i = int(x / 2)
    prev_num = 0
    while True:
        if i * i == x:
            return int(i)
        elif i * i >= x:
            prev_num = int(i)
            i = int(i / 2)
        else:
            i = int(i)
            while i != prev_num:
                i += 1
                if i * i > x:
                    return i - 1
                elif i * i == x:
                    return i
            break
