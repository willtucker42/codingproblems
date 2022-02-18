# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

class Solution(object):
    def longestPalindrome(self, s):
        letters = {}
        for i in range(len(s)):
            if s[i] not in letters:
                letters[s[i]] = 1
            else:
                letters[s[i]] += 1
        total = 0
        is_there_odd = False
        max_odd = 0
        max_odd_char = ''
        for key, value in letters.items():
            if not value % 2 == 0:
                if value > max_odd:
                    max_odd = value
                    max_odd_char = key
                is_there_odd = True
        if is_there_odd:
            total += max_odd
        for key, value in letters.items():
            if value % 2 == 0:
                total += value
            else:
                if value == max_odd and key == max_odd_char:
                    continue
                else:
                    total += value - 1
        return total

        
