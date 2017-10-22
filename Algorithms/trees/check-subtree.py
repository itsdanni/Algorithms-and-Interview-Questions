# T1 and T2 are two very large binary trees, T1 much bigger than T2. Determine if T2 is a subtree of T1
# T2's root can occur in t1 multiple times
# Gotchas: pre-order traversal is the only one that garantees a unique tree, represent non-existent
# children with null nodes yields one of the solutions, where you can compare string representations
# of the two trees but this is not space efficient in large trees
# Alternative Algorithm: find t2's root in t1 and check if every node match
# Space complexity: O(log(n) + log(m))
# Time complexity: O(n + km) where k is number of occurances of t2's root in t1

def contains_tree(t1, t2):
    # Empty tree is always a subtree
    if t2 is None:
        return True
    return is_subtree(t1, t2)

# recursively traverse the larger tree to find the smaller tree, when we have a match, call matchtree
def is_subtree(r1, r2):
    # bigger tree is empty and the subtree is still not found
    if r1 is None:
        return False
    # once we found a node in t1 that is the root of t2, start checking if the rest of the tree are the same
    elif r1.val == r2.val and match_tree(r1, r2):
        return True
    # else go to the left or right and do the same thing
    return is_subtree(r1.left, r2) or is_subtree(r1.right, r2)

def match_tree(r1, r2):
    # both trees are empty
    if r1 is None and r2 is None:
        return True
    # one is empty one isn't
    elif r1 is None or r2 is None:
        return False
    elif r1.val != r2.val:
        return False
    else:
        return match_tree(r1.left, r2.left) && match_tree(r1.right, r2.right)
