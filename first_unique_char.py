class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = {}
        chars2 = {}
        i = 0
        for v in s:
            if v in chars:
                del chars[v]
            else:
                if v not in chars2:
                    chars[v] = i
                chars2[v] = True
            i += 1
        if not chars:
            return -1
        for k in chars.values():
            return k
