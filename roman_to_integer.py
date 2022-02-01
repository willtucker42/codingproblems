# Given a roman numeral, convert it to an integer.

# My solution
class Solution(object):
    def romanToInt(self, s):
        final_num = 0
        skip = False
        for index in range(0, len(s)):
            if skip:
                skip = False
                continue
            if s[index] == 'I':
                try:
                    if s[index + 1] == 'V':
                        skip = True
                        final_num += 4
                        index += 1
                    elif s[index + 1] == 'X':
                        skip = True
                        final_num += 9
                    else:
                        final_num += 1
                except:
                    final_num += 1
            elif s[index] == 'V':
                final_num += 5
            elif s[index] == 'X':
                try:
                    if s[index + 1] == 'L':
                        skip = True
                        final_num += 40
                        index += 1
                    elif s[index + 1] == 'C':
                        skip = True
                        final_num += 90
                        index += 1
                    else:
                        final_num += 10
                except Exception:
                    final_num += 10
            elif s[index] == 'L':
                final_num += 50
            elif s[index] == 'C':
                try:
                    if s[index + 1] == 'D':
                        skip = True
                        final_num += 400
                        index += 1
                    elif s[index + 1] == 'M':
                        skip = True
                        final_num += 900
                        index += 1
                    else:
                        final_num+=100
                except:
                    final_num += 100
            elif s[index] == 'D':
                final_num += 500
            else:
                final_num += 1000
        return final_num
