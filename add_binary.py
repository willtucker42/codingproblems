# Given two binary strings a and b, return their sum as a binary string.
class Solution(object):
    def addBinary(self, a, b):
        if b == "0" or not b:
            return a
        ret_string = ""
        i = 0
        len_a = len(a)
        len_b = len(b)
        if len_a > len_b:
            b = self.append_zero(b, len_a - len_b)
        elif len_b > len_a:
            a = self.append_zero(a, len_b - len_a)
        a = self.create_int_list(a)
        b = self.create_int_list(b)
        for i, v in enumerate(a):
            i = i + 1
            if a[-i] + b[-i] > 1:
                if a[-i] + b[-i] == 2:
                    try:
                        a[-i - 1] += 1
                    except:
                        a.insert(0, 1)
                        b.insert(0, 0)
                    ret_string = "0" + ret_string
                elif a[-i] + b[-i] > 2:
                    try:
                        a[-i - 1] += 1
                    except:
                        a.insert(0, 1)
                        b.insert(0, 0)
                    ret_string = "1" + ret_string
            else:
                ret_string = str(a[-i] + b[-i]) + ret_string
        return ret_string

    def create_int_list(self, n):
        ret_list = []
        for c in n:
            ret_list.append(int(c))
        return ret_list

    def append_zero(self, bin_, how_many):
        while how_many != 0:
            bin_ = "0" + bin_
            how_many -= 1
        return bin_


