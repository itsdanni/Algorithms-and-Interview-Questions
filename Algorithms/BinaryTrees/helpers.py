import math
# Implementations of basic data structures

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def make_balanced_bst(arr):
    return balanced_bst(arr, 0, len(arr) - 1)

def balanced_bst(arr, start, end):
    if (start == end):
        return TreeNode(arr[start])
    else:
        mid = (start + end + 1)//2
        node = TreeNode(arr[mid])
        node.left = balanced_bst(arr, start, mid - 1)
        node.right = balanced_bst(arr, mid + 1, end)
        return node
