// Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

// My solution
class Solution {
    fun strStr(haystack: String, needle: String): Int {
        if (needle.isEmpty()) return 0
        if (haystack.isEmpty() || (needle.length > haystack.length)) return -1
        haystack.forEachIndexed { index, c ->
            if (c == needle[0]) {
                if (checkTheFollowingChars(index, needle, haystack)) return index
            }
        }
        return -1
    }
    fun checkTheFollowingChars(startIndex: Int, needle: String, haystack: String): Boolean {
        val lenToCheck = needle.length
        var i = 0
        while (i != lenToCheck) {
            try {
                if (haystack[startIndex + i] != needle[i]) {
                    return false
                }
                i++
            }catch (e: Exception) {
                return false
            }
        }
        return true
    }
}
