from helpers import make_balanced_bst

def pre_order_traversal(root):
    stack = []
    stack.append(root)
    visited = set()
    while stack:
        s = stack.pop()
        if s not in visited:
            print(s.val)
            visited.add(s)
        if s.right:
            stack.append(s.right)
        if s.left:
            stack.append(s.left)












if __name__ == "__main__":
    t = make_balanced_bst([2, 3, 5, 7, 8, 9, 12])
    in_order_traversal(t)


