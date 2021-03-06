# Problem #2 in googles' "foobar.withgoogle.com"
# | 7 
# | 4 8
# | 2 5 9
# | 1 3 6 10
# Given the above triangle of ID's calculate the ID given any x,y coordinate.
# for example solution(2,2) should return 5. solution(1,4) should return 7. solution(3450,222) should return 6739735

def solution (x,y):
    return getYFromIdOfX(justGetIdFromX(x),y,x)

def justGetIdFromX(x):
    last_num = 0
    curr_num = 0
    i = 0
    while i <= x:
        curr_num = i + last_num
        last_num = curr_num
        i += 1
    return curr_num

def getYFromIdOfX(id_of_x,y,x):
    i = 0
    add_num = 0
    last_num = id_of_x
    curr_num = id_of_x
    while i < y:
        curr_num = add_num + last_num
        last_num = curr_num
        add_num = x + i
        i += 1
    return curr_num
