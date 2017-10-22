# Find the first common ancestor of two nodes in a binary tree (not necessarily a BST)
# if we have links to the parent, this is essentially the question: finding the intersection of two linked lists

class TreeNodeWithParent:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

# Solution 1:
def common_ancestor_parent(node1, node2):
    #find the depth of two nodes
    depth1 = depth(node1)
    depth2 = depth(node2)
    dif = abs(depth1 - depth2)
    deeper = node1 if depth1 - depth2 > 0 else node2
    shallower = node2 if depth1 - depth2 > 0 else node1

    #advance the deeper node pointer dif steps
    for i in range(dif):
        deeper = deeper.parent

    #advance both pointers
    while shallower is not deeper:
        shallower = shallower.parent
        deeper = deeper.parent

    return shallower

def depth(node):
    d = 0
    while node is not None:
        node = node.parent
        d += 1
    return d

# Solution 2:

if __name__ == "__main__":
    t = TreeNodeWithParent(5)
    t.left = TreeNodeWithParent(3)
    t.left.parent = t
    t.right = TreeNodeWithParent(8)
    t.right.parent = t
    ancestor = common_ancestor_parent(t.left, t.right)
    print(ancestor.val)


