# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        int_string1 = ''
        int_string2 = ''
        while l1 or l2:
            if l1:
                int_string1 += str(l1.val)
                l1 = l1.next
            if l2:
                int_string2 += str(l2.val)
                l2 = l2.next
        dummy = ListNode()
        final_list = dummy
        final_num_string = str(int(int_string1[::-1]) + int(int_string2[::-1]))[::-1]
        for c in final_num_string:
            final_list.next = ListNode(int(c))
            final_list = final_list.next
        return dummy.next
    
