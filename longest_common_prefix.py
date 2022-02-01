# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# My solution:
class Solution(object):
    def longestCommonPrefix(self, strs):
        l_c_p = ""
        str_count = len(strs)
        if str_count == 0:
            return l_c_p
        elif str_count == 1:
            return strs[0]
        for i, c in enumerate(strs[0]):
            for i_ in range(1, str_count):
                # get string and check character of string against character from above
                try:
                    if strs[i_][i] != c:
                        return l_c_p
                except:
                    return l_c_p
            l_c_p = l_c_p + c
        return l_c_p
        
