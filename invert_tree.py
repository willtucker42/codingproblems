# Given a binary tree, invert it
def invertTree(root):
    if root is None:
        return None
    tmp = root.left
    root.left = root.right
    root.right = tmp
    invertTree(root.left)
    invertTree(root.right)
    return root
