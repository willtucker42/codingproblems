# Given in integer area return an array of the largest perfect squares that fit into area
# Problem #1 in googles' "foobar.withgoogle.com"
def solution(area):
    holder = area
    square_array = []
    while sum(square_array) != area:
        new_largest_square = makeLargestSquare(holder)
        square_array.append(new_largest_square)
        holder -= new_largest_square
    return square_array


def makeLargestSquare(n):
    i = 1
    while i * i <= n:
        i += 1
    i -= 1
    return i * i
