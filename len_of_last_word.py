# Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

# My solution:
def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    counter = 0
    finalCount = 0
    for c in s:
        if c != " ":
            counter += 1
        else:
            if counter != 0:
                finalCount = counter
                counter = 0
    if counter != 0:
        finalCount = counter
    return finalCount
