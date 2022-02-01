# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

# My solution:

def plusOne(digits):
    i = -1
    if digits[i] == 9:
        try:
            while digits[i] == 9:
                digits[i] = 0
                i -= 1
        except Exception:
            digits.insert(0,1)
            return digits
    digits[i] += 1
    return digits
