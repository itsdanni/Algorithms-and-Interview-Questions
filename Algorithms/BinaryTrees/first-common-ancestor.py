from helpers import TreeNode

# find the first common ancestor of two binary tree nodes without links to parents
# Algorithm: if p, q are both on the left of the node, branch left else branch right.
# When they are no longer on the same side, you must have found the common ancestor

def common_ancestor(root, p, q):
    # error check: one node is not in the tree
    if not in_tree(root, p) or not in_tree(root, q):
        return None
    return ancestor_helper(root, p, q)

def ancestor_helper(root, p, q):
    if root is None or root == p or root == q:
        return root

    # stopping condition: if p and q are on different sides, then we have found the common ancestor
    p_in_left = in_tree(root.left, p)
    q_in_left = in_tree(root.left, q)
    if p_in_left != q_in_left:
        return root

    # recursive condition: if p and q are both on the same side, we go into that side and do the same thing again
    which_side = root.left if p_in_left else root.right
    return ancestor_helper(which_side, p, q)


# recursively checks which tree a node is in
def in_tree(root, node):
    if root is None:
        return False
    if root == node:
        return True
    return in_tree(root.left, node) || in_tree(root.right, node)
