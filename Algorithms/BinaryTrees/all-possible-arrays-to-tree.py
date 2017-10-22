# A binary search tree was created by traversing through an array from left to right and inserting each element.
# Given a BST with distinct elements, print all possible arrays that could have led to this tree

# Algorithm:
# The key insight is that once you have a root, all elements less than that is going to the left,
# all elements greater than that is going to the right, and the relative sequence in which we insert the greater
# element group first doesn't matter. so as long as we have all the sublists and preserve their relative positions
# to each other, we can yield the same tree, think about weaving elements

def all_possible_arrays(root):

