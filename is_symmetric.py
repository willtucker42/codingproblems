# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

class Solution(object):
    def isSymmetric(self, root):
        return self.helper(root.left,root.right)
    
    def helper(self, left, right):
        if left is None or right is None:
            return left == right
        if left.val != right.val:
            return False
        if self.helper(left.left,right.right) and self.helper(left.right,right.left):
            return True
        else:
            return False
        
  
