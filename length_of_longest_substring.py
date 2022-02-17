# Given a string s, find the length of the longest substring without repeating characters.
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        temp_s = ''
        longest_temp = 0
        longest = 0
        start = 0
        while True:
            if start == len(s):
                break
            for c in s[start:]:
                if c not in temp_s:
                    temp_s += c
                    longest_temp += 1
                else:
                    if longest_temp >= longest:
                        longest = longest_temp
                    temp_s = ''
                    start += 1
                    longest_temp = 0
                    break
        return longest
# ^^^ very shitty solution this new one much better

def longestSubstringWithoutRepeating(s):
    final_num = 0
    chars = ''
    for c in s:
        if c not in chars:
            chars += c
            ret_num = len(chars)
            if ret_num >= final_num:
                final_num = ret_num
        else:
            chars = chars.split(c)[1] 
            chars += c
    return final_num
